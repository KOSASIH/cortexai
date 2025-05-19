from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
import os
import numpy as np
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'cortexai_secret_key'

# Configure upload folder
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Mock classification function (to be replaced with actual ML model)
def classify_tumor(image_path):
    # In a real application, this would use a trained model
    # For now, we'll return a mock result
    tumor_types = ['Meningioma', 'Glioma', 'Pituitary Tumor', 'No Tumor']
    confidences = np.random.rand(4)
    confidences = confidences / np.sum(confidences)  # Normalize to sum to 1
    
    results = []
    for tumor_type, confidence in zip(tumor_types, confidences):
        results.append({
            'type': tumor_type,
            'confidence': float(confidence)
        })
    
    # Sort by confidence (highest first)
    results.sort(key=lambda x: x['confidence'], reverse=True)
    return results

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Classify the uploaded image
        results = classify_tumor(file_path)
        
        return render_template('result.html', 
                              image_path=os.path.join('uploads', filename),
                              results=results)
    
    flash('Invalid file type. Please upload an image (png, jpg, jpeg).')
    return redirect(url_for('index'))

@app.route('/api/classify', methods=['POST'])
def api_classify():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Classify the uploaded image
        results = classify_tumor(file_path)
        
        return jsonify({
            'image_path': os.path.join('uploads', filename),
            'results': results
        })
    
    return jsonify({'error': 'Invalid file type'}), 400

@app.route('/forum')
def forum():
    # Mock forum data
    posts = [
        {
            'id': 1,
            'title': 'Differentiating Glioma from Meningioma',
            'author': 'Dr. Sarah Johnson',
            'date': '2025-05-15',
            'content': 'I have noticed that in some cases, distinguishing between Glioma and Meningioma can be challenging...'
        },
        {
            'id': 2,
            'title': 'New research on Pituitary Tumors',
            'author': 'Dr. Michael Chen',
            'date': '2025-05-10',
            'content': 'Recent studies have shown improved detection rates for pituitary tumors using...'
        }
    ]
    return render_template('forum.html', posts=posts)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)