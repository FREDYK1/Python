import streamlit as sl
from PIL import Image


with sl.expander("Start Camera"):
    camera_image = sl.camera_input("Camera")

if camera_image:
    img = Image.open(camera_image)
    gray_image = img.convert("L")
    sl.image(gray_image)

