import zipfile
import os
import pandas as pd
from PIL import Image
import tempfile
from caption_model import CaptionGenerator

def process_zip_file(zip_file, caption_gen):
    """Process a ZIP file containing images and return CSV data"""
    results = []
    
    with tempfile.TemporaryDirectory() as temp_dir:
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
        
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp')):
                    file_path = os.path.join(root, file)
                    try:
                        image = Image.open(file_path)
                        caption = caption_gen.generate_caption(image)
                        results.append({
                            'filename': file,
                            'caption': caption
                        })
                    except Exception as e:
                        results.append({
                            'filename': file,
                            'caption': f"Error: {str(e)}"
                        })
    
    df = pd.DataFrame(results)
    csv_path = tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False)
    df.to_csv(csv_path.name, index=False)
    csv_path.close()
    
    return csv_path.name