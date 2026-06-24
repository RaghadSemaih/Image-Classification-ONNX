import cv2
import numpy as np
import onnxruntime as ort

# تحميل المودل
session = ort.InferenceSession("model.onnx")
input_name = session.get_inputs()[0].name

# إدخال مسار الصورة
image_path = input("Enter image path: ")

# قراءة الصورة
image = cv2.imread(image_path)

if image is None:
    print("Image not found!")
    exit()

# Preprocessing
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image = cv2.resize(image, (224, 224))
image = image.astype(np.float32) / 255.0
image = np.transpose(image, (2, 0, 1))
image = np.expand_dims(image, axis=0)

# تشغيل المودل
outputs = session.run(None, {input_name: image})

# استخراج التصنيف ونسبة الثقة
prediction = outputs[0][0][0]
probabilities = outputs[1][0]
confidence = probabilities[prediction] * 100

# عرض النتيجة
print("\nPrediction:", prediction)
print("Confidence:", round(confidence, 2), "%")