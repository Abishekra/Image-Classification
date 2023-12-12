# Image-Classification
This repository contains a simple Flask web application for image classification using a pre-trained neural network model. Users can upload an image through the web interface, and the application will predict whether the image contains a cat or a dog. Additionally, the prediction results are stored in a MySQL database along with the uploaded image.

Prerequisites:
Before running the application, ensure you have the following prerequisites installed:

>Python 
>Flask
>TensorFlow
>NumPy
>MySQL Connector
>Other dependencies as listed in the README file

You can install the dependencies using the following command:

>bash
>Copy code
>pip install -r requirements.txt
>Setup
>MySQL Database Setup:

Make sure you have MySQL installed and running on your system:

>Create a database named predicted_logs.
>Update the database connection details in the app.py file (host, user, password).
>Model File:

Ensure that you have a trained model file (cat_dog_classifier.h5) available. You can use your own pre-trained model or train one using relevant data.
Run the Application:

Execute the app.py script to start the Flask application:

>bash
>Copy code
>python app.py
>The application will be accessible at http://127.0.0.1:5000/ in your web browser.

Usage:

>Access the web interface at http://127.0.0.1:5000/.
>Upload an image using the provided form.
>Click the "Predict" button to submit the image for classification.
>The result will be displayed on the web page along with the uploaded image.

Project Structure:

>app.py: The main Flask application script containing the web application logic.
>uploads: A folder where uploaded images are temporarily stored.
>cat_dog_classifier.h5: Pre-trained neural network model for cat and dog classification.
>templates: Folder containing HTML templates for rendering the web interface.
>Database Schema

The MySQL database (predicted_logs) has a table named prediction_data with the following columns:

>id: Auto-incremented primary key.
>image: Binary data of the uploaded image.
>predicted_result: The predicted result (e.g., "It's a cat").
>prediction_time: Timestamp indicating when the prediction was made.

License:

This project is licensed under the MIT License.
