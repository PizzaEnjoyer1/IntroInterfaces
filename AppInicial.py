import streamlit as st
from PIL import Image

st.title("Mi primera página")

st.header("Si")
st.write("pug")
st.text("Hola Mundo aaaaa")
imagePug = Image.open("pugo.png")
st.image(imagePug, caption = "Perro")
