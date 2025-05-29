# QuickCaption

Small, fast, and useful: drop an image, get an accessibility caption powered by a Hugging Face vision-language model.

## 🚀 Live Demo

Try QuickCaption now: **[https://sohei1l.github.io/quick-caption/](https://sohei1l.github.io/quick-caption/)**

## Features

- Drag-and-drop image captioning
- Confidence scoring for caption reliability
- Image quality analysis (brightness, contrast, sharpness)
- Powered by Salesforce BLIP model

## To Build Locally

```bash
pip install -r requirements.txt
```

```bash
python app.py
```

## Model Information

This application uses the Salesforce BLIP (Bootstrapping Language-Image Pre-training) model for image captioning. The model generates human-readable descriptions that are perfect for accessibility purposes.

## Advanced Features

- **Confidence Scoring**: Each caption comes with a confidence percentage indicating the model's certainty
- **Image Quality Analysis**: Automatic assessment of brightness, contrast, sharpness, and resolution
- **Detailed Analysis Tab**: Comprehensive view combining captions with quality metrics for professional use
