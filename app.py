import gradio as gr
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

def create_interface():
    """Create and return the Gradio interface"""
    interface = gr.Interface(
        fn=generate_caption,
        inputs=gr.Image(type="pil", label="Upload an image"),
        outputs=gr.Textbox(label="Generated Caption", lines=3),
        title="QuickCaption",
        description="Drop an image and get an instant accessibility caption powered by AI. Perfect for alt-text generation!",
        examples=None,
        theme=gr.themes.Soft()
    )
    return interface

if __name__ == "__main__":
    print("Loading caption model...")
    interface = create_interface()
    print("Starting Gradio interface...")
    interface.launch(share=False, server_name="0.0.0.0")