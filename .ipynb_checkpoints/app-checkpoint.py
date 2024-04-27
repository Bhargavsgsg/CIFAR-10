from flask import Flask, render_template, request, jsonify
import torch
from PIL import Image
import torchvision.transforms as transforms
from my_module import Net
import io
import base64

app = Flask(__name__)

# Load the model
model = Net()  # Assuming Net is your model class
model.load_state_dict(torch.load('model.pth'))
model.eval()

def transform_image(image_bytes):
    my_transforms = transforms.Compose([
        transforms.Resize((32, 32)),
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])
    image = Image.open(io.BytesIO(image_bytes))
    return my_transforms(image).unsqueeze(0)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    image_bytes = file.read()
    image_tensor = transform_image(image_bytes)
    model.eval()
    classes = ['airplane', 'automobile', 'bird', 'cat', 'deer',
           'dog', 'frog', 'horse', 'ship', 'truck']
    with torch.no_grad():
        output = model(image_tensor)
        _, predicted = torch.max(output, 1)
        prediction = classes[predicted.item()]
    # Convert image to base64
    image_base64 = base64.b64encode(image_bytes).decode('utf-8')

    return render_template('result.html', prediction=prediction, image_base64=image_base64)

if __name__ == '__main__':
    app.run(debug=True)