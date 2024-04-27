# CIFAR-10
This project implements a simple web API for classifying images using a Convolutional Neural Network (CNN) trained on the CIFAR-10 dataset. The API allows users to upload an image and receive a prediction of the image's class label from the CIFAR-10 dataset. This repository also consists of a jupyter notebook with a walkthrough of the model details. 
## Getting Started

To run the API locally, follow these steps:

1. Clone this repository:
<pre>
   git clone https://github.com/your-username/CIFAR-10-API.git
</pre>
2. Install the requied python packages:
<pre>
   pip install -r requirements.txt
</pre>
3. Run the Flask application:
<pre>
   python app.py
</pre>
4. Access the API at http://127.0.0.1:5000 in your web browser.
# Usage
## Uploading an image
1. Navigate to the home page of the API (http://127.0.0.1:5000) in your web browser.
2. Click on the "Choose File" button to select an image file for upload.
3. Click the "Upload" button to submit the image.
## Viewing the prediction
After uploading an image, the API will display the uploaded image along with the predicted class label from the CIFAR-10 dataset.

# Dependencies
* Flask: Web framework for Python
* Torch, torchvision: Libraries for machine learning and computer vision

# Acknowledgments
* The CIFAR-10 dataset is used for training the image classification model.
* The model architecture is based on a Convolutional Neural Network (CNN).
