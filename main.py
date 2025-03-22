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

st.title("Feedback & Suggestions")

# Input fields
name = st.text_input("Your Name")
email = st.text_input("Your Email")
feedback = st.text_area("Your Feedback or Suggestion")

# Submit button
if st.button("Submit"):
    if name and email and feedback.strip():
        # Save the feedback to a file
        with open("feedback.txt", "a") as f:
            f.write(f"Name: {name}\nEmail: {email}\nFeedback: {feedback}\n")
            f.write("-" * 40 + "\n")

        st.success("Thank you for your feedback!")
    else:
        st.warning("Please fill in all fields before submitting.")




