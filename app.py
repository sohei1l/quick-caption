import gradio as gr
from caption_model import CaptionGenerator
from batch_processor import process_zip_file

caption_gen = CaptionGenerator()

def generate_caption(image):
    """Generate caption for a single image"""
    if image is None:
        return "Please upload an image.", ""
    
    try:
        caption, confidence = caption_gen.generate_caption(image)
        return caption, f"Confidence: {confidence:.1%}"
    except Exception as e:
        return f"Error generating caption: {str(e)}", ""

def generate_caption_with_analysis(image):
    """Generate caption with detailed analysis"""
    if image is None:
        return "Please upload an image.", "", ""
    
    try:
        result = caption_gen.generate_caption_with_metrics(image)
        caption = result['caption']
        confidence = result['confidence']
        metrics = result['quality_metrics']
        
        confidence_text = f"Confidence: {confidence:.1%}"
        
        analysis_text = f"""Image Quality Analysis:
• Brightness: {metrics['brightness']:.1%}
• Contrast: {metrics['contrast']:.1%} 
• Sharpness: {metrics['sharpness']:.1%}
• Resolution: {metrics['resolution_score']:.1%}"""
        
        return caption, confidence_text, analysis_text
    except Exception as e:
        return f"Error generating caption: {str(e)}", "", ""

def process_batch(zip_file):
    """Process a ZIP file of images and return CSV"""
    if zip_file is None:
        return None, "Please upload a ZIP file containing images."
    
    try:
        csv_path = process_zip_file(zip_file, caption_gen)
        return csv_path, "Batch processing completed! Download the CSV file."
    except Exception as e:
        return None, f"Error processing batch: {str(e)}"

def create_interface():
    """Create and return the Gradio interface"""
    with gr.Blocks(theme=gr.themes.Soft(), title="QuickCaption") as interface:
        gr.Markdown("# QuickCaption")
        gr.Markdown("Drop an image and get an instant accessibility caption powered by AI. Perfect for alt-text generation!")
        
        with gr.Tab("Single Image"):
            with gr.Row():
                image_input = gr.Image(type="pil", label="Upload an image")
                with gr.Column():
                    caption_output = gr.Textbox(label="Generated Caption", lines=3, show_copy_button=True)
                    confidence_output = gr.Textbox(label="Confidence Score", lines=1)
            
            image_input.change(fn=generate_caption, inputs=image_input, outputs=[caption_output, confidence_output])
        
        with gr.Tab("Detailed Analysis"):
            gr.Markdown("Get comprehensive image analysis including caption confidence and quality metrics.")
            with gr.Row():
                analysis_image_input = gr.Image(type="pil", label="Upload an image")
                with gr.Column():
                    analysis_caption_output = gr.Textbox(label="Generated Caption", lines=3, show_copy_button=True)
                    analysis_confidence_output = gr.Textbox(label="Confidence Score", lines=1)
                    quality_metrics_output = gr.Textbox(label="Image Quality Metrics", lines=6)
            
            analysis_image_input.change(fn=generate_caption_with_analysis, inputs=analysis_image_input, outputs=[analysis_caption_output, analysis_confidence_output, quality_metrics_output])
        
        with gr.Tab("Batch Processing"):
            gr.Markdown("Upload a ZIP file containing images to get captions for all of them in a CSV file.")
            with gr.Row():
                zip_input = gr.File(label="Upload ZIP file", file_types=[".zip"])
                with gr.Column():
                    batch_status = gr.Textbox(label="Status", lines=2)
                    csv_download = gr.File(label="Download CSV")
            
            zip_input.change(fn=process_batch, inputs=zip_input, outputs=[csv_download, batch_status])
    
    return interface

if __name__ == "__main__":
    print("Loading caption model...")
    interface = create_interface()
    print("Starting Gradio interface...")
    interface.launch(share=False, server_name="0.0.0.0")