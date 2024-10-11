import os
import time
import streamlit as st
from PIL import Image

# Create a folder to save uploaded images
image_dir = "uploaded_images"
if not os.path.exists(image_dir):
    os.makedirs(image_dir)

# File uploader
uploaded_files = st.file_uploader("Choose images", accept_multiple_files=True, type=['png', 'jpg', 'jpeg'])

# Save uploaded images to the folder
if uploaded_files:
    st.write("Images uploaded successfully! Starting slideshow...")
    
    # Save each uploaded image to the directory
    for file in uploaded_files:
        with open(os.path.join(image_dir, file.name), "wb") as f:
            f.write(file.getbuffer())
    
    # Slideshow
    for file in uploaded_files:
        # Open and display the image
        image = Image.open(os.path.join(image_dir, file.name))
        st.image(image, caption=file.name)
        
        # Add a delay of 2 seconds before showing the next image
        time.sleep(2)
        
        # Clear the previous image before displaying the next one
        st.experimental_rerun()
else:
    st.write("No images uploaded yet.")
