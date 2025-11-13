import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow import keras
import cv2
import os
from datetime import datetime

# Set page configuration
st.set_page_config(
    page_title="Fruit Quality Classifier",
    page_icon="🍎",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #2E8B57;
        text-align: center;
        margin-bottom: 1rem;
    }
    .prediction-box {
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        text-align: center;
        font-size: 1.2rem;
    }
    .good-fruit {
        background-color: #90EE90;
        border: 2px solid #32CD32;
    }
    .bad-fruit {
        background-color: #FFB6C1;
        border: 2px solid #DC143C;
    }
    .upload-section {
        border: 2px dashed #ccc;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

class FruitQualityClassifier:
    def __init__(self):
        self.model = None
        self.class_names = ['Not Good', 'Good']
    
    def load_model(self, model_path):
        """Load your trained model"""
        try:
            if model_path and os.path.exists(model_path):
                self.model = keras.models.load_model(model_path)
                return True
            return False
        except Exception as e:
            st.error(f"Error loading model: {e}")
            return False
    
    def preprocess_image(self, image):
        """Preprocess the image for prediction"""
        try:
            # Convert to numpy array
            img_array = np.array(image)
            
            # Resize image to match your model's expected input
            img_size = (224, 224)  # Adjust based on your model
            img_array = cv2.resize(img_array, img_size)
            
            # Normalize pixel values
            img_array = img_array / 255.0
            
            # Add batch dimension
            img_array = np.expand_dims(img_array, axis=0)
            
            return img_array
        except Exception as e:
            st.error(f"Error preprocessing image: {e}")
            return None
    
    def predict(self, image):
        """Make prediction on the image"""
        try:
            # For demo - replace this with your actual model prediction
            return self.demo_prediction(image)
            
        except Exception as e:
            st.error(f"Prediction error: {e}")
            return None, 0.0
    
    def demo_prediction(self, image):
        """Demo prediction - REPLACE THIS WITH YOUR ACTUAL MODEL"""
        # This is a dummy function - replace with your model's prediction logic
        img_array = np.array(image)
        
        # Simple demo logic based on image properties
        # Replace this with your actual model inference
        avg_brightness = np.mean(img_array)
        color_variance = np.var(img_array)
        
        # Demo logic (replace with your model)
        if avg_brightness > 100 and color_variance > 500:
            predicted_class = 1  # Good
            confidence = min(0.85 + (avg_brightness - 100) / 500, 0.95)
        else:
            predicted_class = 0  # Not Good
            confidence = min(0.75 + (100 - avg_brightness) / 500, 0.90)
            
        return predicted_class, confidence

def main():
    # Initialize classifier
    classifier = FruitQualityClassifier()
    
    # Header
    st.markdown('<h1 class="main-header">🍎 Fruit Quality Classifier</h1>', 
                unsafe_allow_html=True)
    st.markdown("### Upload an image or capture using camera to check fruit quality")
    
    # Create two columns for the two options
    col1, col2 = st.columns(2)
    
    uploaded_image = None
    image_source = None
    
    with col1:
        st.subheader("📁 Option 1: Upload Image")
        st.markdown('<div class="upload-section">', unsafe_allow_html=True)
        uploaded_file = st.file_uploader(
            "Choose a fruit image", 
            type=['jpg', 'jpeg', 'png'],
            key="uploader",
            label_visibility="collapsed"
        )
        if uploaded_file is not None:
            uploaded_image = Image.open(uploaded_file)
            image_source = "Uploaded"
        st.markdown('</div>', unsafe_allow_html=True)
        
        if uploaded_file is not None:
            st.success("✅ Image uploaded successfully!")
            st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
    
    with col2:
        st.subheader("📷 Option 2: Capture Image")
        st.markdown('<div class="upload-section">', unsafe_allow_html=True)
        camera_image = st.camera_input(
            "Take a picture of fruit",
            key="camera",
            label_visibility="collapsed"
        )
        if camera_image is not None:
            uploaded_image = Image.open(camera_image)
            image_source = "Camera"
        st.markdown('</div>', unsafe_allow_html=True)
        
        if camera_image is not None:
            st.success("✅ Image captured successfully!")
            st.image(uploaded_image, caption="Captured Image", use_column_width=True)
    
    # Prediction section
    if uploaded_image is not None:
        st.markdown("---")
        st.header("🔍 Prediction Results")
        
        # Display image info
        st.write(f"**Image Source:** {image_source}")
        st.write(f"**Image Size:** {uploaded_image.size}")
        st.write(f"**Image Mode:** {uploaded_image.mode}")
        
        # Make prediction
        with st.spinner("Analyzing fruit quality..."):
            predicted_class, confidence = classifier.predict(uploaded_image)
        
        if predicted_class is not None:
            # Display results
            class_name = classifier.class_names[predicted_class]
            confidence_percent = confidence * 100
            
            # Result box
            if predicted_class == 1:
                st.markdown(
                    f'<div class="prediction-box good-fruit">'
                    f'<h2>✅ GOOD FRUIT</h2>'
                    f'<h3>Confidence: {confidence_percent:.1f}%</h3>'
                    f'</div>', 
                    unsafe_allow_html=True
                )
                st.balloons()
            else:
                st.markdown(
                    f'<div class="prediction-box bad-fruit">'
                    f'<h2>❌ NOT GOOD FRUIT</h2>'
                    f'<h3>Confidence: {confidence_percent:.1f}%</h3>'
                    f'</div>', 
                    unsafe_allow_html=True
                )
            
            # Detailed information
            st.subheader("Detailed Analysis")
            col_a, col_b = st.columns(2)
            
            with col_a:
                st.metric("Quality", class_name)
                st.metric("Confidence Score", f"{confidence:.3f}")
                
            with col_b:
                status = "Excellent" if confidence > 0.9 else "Good" if confidence > 0.7 else "Moderate"
                st.metric("Confidence Level", status)
                
                if image_source == "Camera":
                    st.metric("Capture Mode", "Live Camera")
                else:
                    st.metric("Upload Mode", "File Upload")
            
            # Interpretation
            st.subheader("Interpretation")
            if predicted_class == 1:
                st.success("""
                **This fruit appears to be in good condition!** 
                - Fresh appearance
                - Good color and texture
                - Suitable for consumption
                """)
            else:
                st.error("""
                **This fruit may not be in optimal condition!**
                - Possible signs of spoilage
                - May be overripe or damaged
                - Consider inspection before consumption
                """)
        
        else:
            st.error("Could not process the image. Please try again with a clearer image.")
    
    else:
        # Instructions when no image is selected
        st.markdown("---")
        st.info("👆 **Please choose one of the options above to get started!**")
        
        # Instructions
        st.subheader("How to use:")
        col_i1, col_i2 = st.columns(2)
        
        with col_i1:
            st.write("**📁 Upload Image:**")
            st.write("1. Click 'Browse files'")
            st.write("2. Select a clear fruit image")
            st.write("3. Wait for analysis")
            
        with col_i2:
            st.write("**📷 Capture Image:**")
            st.write("1. Allow camera access")
            st.write("2. Position fruit in frame")
            st.write("3. Click 'Take Photo'")
        
        # Supported fruits
        st.subheader("🍓 Supported Fruits")
        fruits = ["Apples", "Oranges", "Bananas", "Grapes", "Strawberries", "Mangoes"]
        cols = st.columns(3)
        for i, fruit in enumerate(fruits):
            cols[i % 3].write(f"• {fruit}")

    # Footer
    st.markdown("---")
    st.markdown("*Built with Streamlit • Fruit Quality Classification*")

if __name__ == "__main__":
    main()