from caption_model import CaptionGenerator

caption_gen = CaptionGenerator()

def generate_caption(image):
    """Generate caption for a single image"""
    if image is None:
        return "Please upload an image."
    
    try:
        caption = caption_gen.generate_caption(image)
        return caption
    except Exception as e:
        return f"Error generating caption: {str(e)}"

if __name__ == "__main__":
    print("Caption model loaded successfully!")
    print("Ready to generate captions...")