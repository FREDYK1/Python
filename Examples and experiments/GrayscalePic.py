import streamlit as sl
from PIL import Image

uploaded_image = sl.file_uploader("Upload Image")
if uploaded_image:
    image = Image.open(uploaded_image)
    grayscale = image.convert("L")
    sl.image(grayscale)

with sl.expander("Start Camera"):
    camera_image = sl.camera_input("Camera")

if camera_image:
    img = Image.open(camera_image)
    gray_image = img.convert("L")
    sl.image(gray_image)

