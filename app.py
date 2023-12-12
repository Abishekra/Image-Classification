import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from flask import Flask, request, render_template_string
import mysql.connector

# Initialize Flask application
app = Flask(__name__)

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Abi@123aws",
    database="predicted_logs"  
)

# Create cursor
cursor = db.cursor()

# Load the trained model
model = tf.keras.models.load_model('c:/Users/ABISHEK/Downloads/abi/cat_dog_classifier.h5')  

# Function to predict the class of an image
def predict_image_class(image_path):
    img = image.load_img(image_path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    prediction = model.predict(img_array)
    if prediction[0] > 0.5:
        return "It's a dog"
    else:
        return "It's a cat"

# HTML template directly within the Python script
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Image Classification</title>
</head>
<body>
    <h1>Image Classification</h1>
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" value=" Predict">
    </form>
    {% if prediction %}
    <h2>Result:</h2>
    <p>{{ prediction }}</p>
    <img src="{{ image_path }}" alt="Uploaded Image" >
    {% endif %}
</body>
</html>
"""

# Configure a route to handle the image upload
@app.route('/', methods=['GET', 'POST'])
def upload_and_predict():
    if request.method == 'POST':
        # Check if a file was uploaded
        if 'file' not in request.files:
            return render_template_string(html_template, message='No file part')

        file = request.files['file']

        # Check if the file has a valid name and extension
        if file.filename == '':
            return render_template_string(html_template, message='No selected file')

        if file:
            # Save the uploaded file to a temporary folder
            upload_folder = 'uploads'
            os.makedirs(upload_folder, exist_ok=True)
            uploaded_file_path = os.path.join(upload_folder, file.filename)
            file.save(uploaded_file_path)

            # Use the model to predict the image class
            prediction = predict_image_class(uploaded_file_path)
            
            # Store prediction result in the database
            with open(uploaded_file_path, 'rb') as f:
                image_data = f.read()

            query = "INSERT INTO prediction_data (image, predicted_result, prediction_time) VALUES (%s, %s, NOW())"
            values = (image_data, prediction)
            cursor.execute(query, values)
            db.commit()

            # Return the prediction result
            return render_template_string(html_template, prediction=prediction, image_path=uploaded_file_path)

    return render_template_string(html_template)

if __name__ == '__main__':
    app.run(debug=True)