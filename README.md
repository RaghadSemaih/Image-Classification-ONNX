# Image-Classification-ONNX

Car Image Classification using Azure Custom Vision

Overview

This project demonstrates a simple image classification model built using Microsoft Azure Custom Vision. The objective is to classify whether an image contains a car or not a car.

After training, the model was exported in ONNX format to allow it to run locally on different operating systems using Python.

⸻

Project Goal

Develop a basic image classification model while learning the complete workflow of Azure Custom Vision, including:

* Data collection
* Model training
* Performance evaluation
* Model export
* Local inference using ONNX

⸻

Dataset

A public dataset was not used.

Instead, a small custom dataset was manually collected containing:

* 15 images of cars
* 15 images of non-car objects

This limited dataset was intentionally used as a learning project to understand the end-to-end machine learning workflow.

⸻

Technologies Used

* Microsoft Azure Custom Vision
* Python
* ONNX Runtime
* ONNX Model Format

⸻

Project Workflow

1. Created an Azure Custom Vision resource.
2. Created a new image classification project.
3. Collected and labeled the dataset manually.
4. Trained the model using Azure Custom Vision.
5. Evaluated the model using the provided metrics.
6. Exported the trained model in ONNX format.
7. Ran the exported model locally using Python.

⸻

Results

Due to the small training dataset, the model achieved limited Precision and Recall scores, which was expected.

However, the Average Precision (AP) indicated that the model was able to distinguish between the two classes within the available data. Increasing the dataset size and diversity would likely improve the model’s overall performance and generalization.

⸻

Repository Contents

* model.onnx — Exported trained model.
* inference.py — Python script for local inference.
* requirements.txt — Required Python packages.
* sample_image.jpg — Example image for testing.
* screenshots/ — Training process and evaluation screenshots.

⸻

Future Improvements

* Increase the dataset size.
* Add more diverse images.
* Improve Precision and Recall.
* Deploy the model as a web API or cloud service.
* Compare the exported ONNX model with other deployment methods.

⸻

What I Learned

Through this project, I gained practical experience with:

* Azure Custom Vision
* Image classification workflow
* Data labeling
* Model evaluation

* 
* ONNX model export
* Running AI models locally with Python
* Understanding the impact of dataset size on model performance
