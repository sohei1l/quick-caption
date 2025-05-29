from transformers import Blip2Processor, Blip2ForConditionalGeneration
from PIL import Image
import torch
import torch.nn.functional as F
import numpy as np

class CaptionGenerator:
    def __init__(self):
        self.model = None
        self.processor = None
        self._load_model()
    
    def _load_model(self):
        model_name = "Salesforce/blip2-opt-2.7b"
        self.processor = Blip2Processor.from_pretrained(model_name)
        self.model = Blip2ForConditionalGeneration.from_pretrained(model_name, torch_dtype=torch.float16)
        
        if torch.cuda.is_available():
            self.model = self.model.to("cuda")
    
    def _calculate_image_quality_metrics(self, image):
        """Calculate basic image quality metrics"""
        img_array = np.array(image)
        
        # Brightness (mean pixel value)
        brightness = np.mean(img_array) / 255.0
        
        # Contrast (standard deviation)
        contrast = np.std(img_array) / 255.0
        
        # Sharpness approximation using Laplacian variance
        gray = np.mean(img_array, axis=2) if len(img_array.shape) == 3 else img_array
        laplacian_var = np.var(np.gradient(gray))
        sharpness = min(laplacian_var / 1000.0, 1.0)  # Normalize
        
        # Resolution score
        width, height = image.size
        resolution_score = min((width * height) / (1920 * 1080), 1.0)
        
        return {
            'brightness': round(brightness, 3),
            'contrast': round(contrast, 3),
            'sharpness': round(sharpness, 3),
            'resolution_score': round(resolution_score, 3)
        }
    
    def generate_caption(self, image):
        if isinstance(image, str):
            image = Image.open(image).convert('RGB')
        elif hasattr(image, 'convert'):
            image = image.convert('RGB')
        
        inputs = self.processor(image, return_tensors="pt")
        
        if torch.cuda.is_available():
            inputs = {k: v.to("cuda") for k, v in inputs.items()}
        
        with torch.no_grad():
            outputs = self.model.generate(**inputs, max_length=100, num_beams=8, do_sample=True, temperature=0.7, return_dict_in_generate=True, output_scores=True)
            
        caption = self.processor.decode(outputs.sequences[0], skip_special_tokens=True)
        
        # Calculate confidence score from generation scores
        if hasattr(outputs, 'scores') and outputs.scores:
            # Average the log probabilities and convert to confidence percentage
            scores = torch.stack(outputs.scores, dim=1)
            probs = F.softmax(scores, dim=-1)
            max_probs = torch.max(probs, dim=-1)[0]
            confidence = torch.mean(max_probs).item()
        else:
            confidence = 0.8  # Default confidence if scores unavailable
        
        return caption, round(confidence, 3)
    
    def generate_caption_with_metrics(self, image):
        """Generate caption with confidence and image quality metrics"""
        if isinstance(image, str):
            image = Image.open(image).convert('RGB')
        elif hasattr(image, 'convert'):
            image = image.convert('RGB')
        
        caption, confidence = self.generate_caption(image)
        quality_metrics = self._calculate_image_quality_metrics(image)
        
        return {
            'caption': caption,
            'confidence': confidence,
            'quality_metrics': quality_metrics
        }