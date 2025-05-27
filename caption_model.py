from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

class CaptionGenerator:
    def __init__(self):
        self.model = None
        self.processor = None
        self._load_model()
    
    def _load_model(self):
        model_name = "Salesforce/blip-image-captioning-base"
        self.processor = BlipProcessor.from_pretrained(model_name)
        self.model = BlipForConditionalGeneration.from_pretrained(model_name)
        
        if torch.cuda.is_available():
            self.model = self.model.to("cuda")
    
    def generate_caption(self, image):
        if isinstance(image, str):
            image = Image.open(image).convert('RGB')
        elif hasattr(image, 'convert'):
            image = image.convert('RGB')
        
        inputs = self.processor(image, return_tensors="pt")
        
        if torch.cuda.is_available():
            inputs = {k: v.to("cuda") for k, v in inputs.items()}
        
        with torch.no_grad():
            out = self.model.generate(**inputs, max_length=50, num_beams=5)
        
        caption = self.processor.decode(out[0], skip_special_tokens=True)
        return caption