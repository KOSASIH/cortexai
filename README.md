# CortexAI - Brain Tumor Classification System

CortexAI is an innovative application that employs deep learning techniques to classify brain tumors from MRI scans. It features a collaborative platform for healthcare professionals to share insights and improve diagnostic practices collectively.

## Features

- **MRI Scan Analysis**: Upload brain MRI scans for AI-assisted tumor classification
- **Multi-class Classification**: Identifies different types of brain tumors (Meningioma, Glioma, Pituitary)
- **Confidence Metrics**: Provides confidence levels for each classification result
- **Healthcare Professional Forum**: Collaborative platform for sharing insights and discussing cases
- **Research Integration**: Based on the latest research in medical imaging and deep learning

## Technical Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **AI Model**: Deep learning model for image classification (currently using a mock model)

## Getting Started

1. Install the required dependencies:
   ```
   pip install flask numpy werkzeug
   ```

2. Run the application:
   ```
   python app.py
   ```

3. Access the application at http://localhost:8080

## Future Enhancements

- Integration with a real deep learning model trained on brain MRI datasets
- User authentication and profile management
- Advanced forum features with search and filtering
- Integration with medical record systems
- Mobile application for on-the-go access