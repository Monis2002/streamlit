from tensorflow.keras import layers,models
import tensorflow as tf
import numpy as np

def predict(model, img):
    class_names = ['Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy']

    img_array = tf.keras.preprocessing.image.img_to_array(img.numpy())
    img_array = tf.expand_dims(img_array, 0)  # Create a batch

    predictions = model.predict(img_array)

    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = round(100 * (np.max(predictions[0])), 2)
    return predicted_class, confidence