import streamlit as st
from PIL import Image

st.title("Mi primera página")

st.header("Si")
st.write("pug")
st.text("Hola Mundo aaaaa")
imagePug = Image.open("pugo.png")
st.image(imagePug, caption = "Perro")

texto = st.text_input("Escribe algo: ", "Este es mi texto")
st.write("El texto escrito es: ", texto)
