# QuickCaption

Small, fast, and useful: drop an image, get a crisp accessibility caption powered by a Hugging Face vision-language model.

## Features
- 🖼️ Drag-and-drop image captioning
- 📊 Confidence scoring for caption reliability
- 🔍 Image quality analysis (brightness, contrast, sharpness)
- 📦 Batch processing with ZIP uploads
- 📄 CSV export for bulk operations
- 🚀 Powered by Salesforce BLIP model
- ☁️ Ready for Hugging Face Spaces deployment

## Installation
```bash
pip install -r requirements.txt
```

## Usage

### Local Development
```bash
python app.py
```
Then open your browser to the provided URL and start captioning images!

### Deploy to Hugging Face Spaces
1. Create a new Space on Hugging Face
2. Choose "Gradio" as the SDK
3. Upload all files to your Space repository
4. Your app will automatically deploy!

## Model Information
This application uses the Salesforce BLIP (Bootstrapping Language-Image Pre-training) model for image captioning. The model generates human-readable descriptions that are perfect for accessibility purposes.

## Advanced Features
- **Confidence Scoring**: Each caption comes with a confidence percentage indicating the model's certainty
- **Image Quality Analysis**: Automatic assessment of brightness, contrast, sharpness, and resolution
- **Detailed Analysis Tab**: Comprehensive view combining captions with quality metrics for professional use