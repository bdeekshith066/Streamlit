#sidebar image 
import streamlit as st
import base64

def set_sidebar_background(image_file):
    st.markdown(
        f"""
        <style>
        [data-testid="stSidebar"] {{
            background-image: url(data:image/jpeg;base64,{image_file});
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def app():
    # Load the background image for the sidebar
    with open("back.jpg", "rb") as file:
        encoded_image = base64.b64encode(file.read()).decode()

    # Set the sidebar background
    set_sidebar_background(encoded_image)

    # Your app content goes here
    st.title("Your Main Content")

if __name__ == "__main__":
    app()
