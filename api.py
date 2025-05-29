from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
import base64
import io
from caption_model import CaptionGenerator

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize caption generator
caption_gen = CaptionGenerator()

@app.route('/api/caption', methods=['POST'])
def generate_caption():
    """Generate caption for uploaded image"""
    try:
        # Get image data from request
        data = request.get_json()
        if not data or 'image' not in data:
            return jsonify({'error': 'No image data provided'}), 400
        
        # Decode base64 image
        image_data = data['image'].split(',')[1]  # Remove data:image/jpeg;base64, prefix
        image_bytes = base64.b64decode(image_data)
        image = Image.open(io.BytesIO(image_bytes))
        
        # Generate caption
        caption, confidence = caption_gen.generate_caption(image)
        
        return jsonify({
            'caption': caption,
            'confidence': confidence
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/caption-analysis', methods=['POST'])
def generate_caption_with_analysis():
    """Generate caption with detailed analysis"""
    try:
        # Get image data from request
        data = request.get_json()
        if not data or 'image' not in data:
            return jsonify({'error': 'No image data provided'}), 400
        
        # Decode base64 image
        image_data = data['image'].split(',')[1]  # Remove data:image/jpeg;base64, prefix
        image_bytes = base64.b64decode(image_data)
        image = Image.open(io.BytesIO(image_bytes))
        
        # Generate caption with metrics
        result = caption_gen.generate_caption_with_metrics(image)
        
        return jsonify({
            'caption': result['caption'],
            'confidence': result['confidence'],
            'quality_metrics': result['quality_metrics']
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    print("Loading caption model...")
    print("Starting API server...")
    app.run(host='0.0.0.0', port=5000, debug=True)