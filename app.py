import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load the trained model
model = tf.keras.models.load_model('mnist_cnn_model.keras')

st.title("🧠 MNIST Digit Classifier")
st.write("Upload a handwritten digit image (28x28 grayscale).")

uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('L')  # convert to grayscale
    image = image.resize((28, 28))
    img_array = np.array(image) / 255.0
    img_array = img_array.reshape(1, 28, 28, 1)
    
    st.image(image, caption='Uploaded Image', width=150)
    
    # Predict
    prediction = model.predict(img_array)
    predicted_class = np.argmax(prediction)
    confidence = np.max(prediction)
    
    st.write(f"### 🧩 Predicted Digit: {predicted_class}")
    st.write(f"**Confidence:** {confidence:.2f}")

st.markdown("---")
st.caption("Built with TensorFlow + Streamlit")
