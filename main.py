import streamlit as st
from PIL import Image

st.title('Image Converter')
st.subheader('Welcome To SOLVIX ')
st.image("https://i.postimg.cc/PrNYgcmB/Screenshot-20250322-132053-Samsung-Internet.jpg",
         caption="SOLVIX",use_container_width=True)
st.write('This page allows you to convert your live images to grey colour')


with st.expander('Start camera'):
    camera_image=st.camera_input('camera')

if camera_image:
    img = Image.open(camera_image)
    grey_img = img.convert("L")
    st.image(grey_img)

