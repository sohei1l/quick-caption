# QuickCaption

Small, fast, and useful: drop an image, get an accessibility caption powered by a Hugging Face BLIP vision-language model.

## 🚀 Live Demo

Try QuickCaption now: **[https://sohei1l.github.io/quick-caption/](https://sohei1l.github.io/quick-caption/)**

_The demo runs entirely in your browser using Transformers.js - no server required!_

## Features

- **Drag-and-drop image captioning** - Instant AI-powered descriptions
- **Confidence scoring** - Know how reliable each caption is
- **Image quality analysis** - Brightness, contrast, sharpness metrics
- **Browser-based AI** - Runs locally with no data upload

### Local Python App (Full features)

```bash
pip install -r requirements.txt
python app.py
```

Includes batch processing and the full Gradio interface.

### ☁️ Cloud Deployment

Deploy to Hugging Face Spaces or other cloud platforms using the included `Dockerfile`.

## Model Information

This application uses the Salesforce BLIP (Bootstrapping Language-Image Pre-training) model for image captioning. The model generates human-readable descriptions that are perfect for accessibility purposes.

## Advanced Features

- **Confidence Scoring**: Each caption comes with a confidence percentage indicating the model's certainty
- **Image Quality Analysis**: Automatic assessment of brightness, contrast, sharpness, and resolution
- **Detailed Analysis Tab**: Comprehensive view combining captions with quality metrics for professional use
