import streamlit as st
from PIL import Image

st.title("Mi primera página")

st.header("Si")
st.write("pug")
st.text("Hola Mundo aaaaa")
imagePug = Image.open('pug.jpeg')
st.imagen(imagen, caption = "Perro")
