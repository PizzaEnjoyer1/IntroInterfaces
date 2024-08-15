import streamlit as st
from PIL import Image

st.title("Razas del mundo: pug")

st.header("Realizado por JCBG")
st.text("Un pug")
imagePug = Image.open("pugo.png")
st.image(imagePug, caption = "Perro")

texto = st.text_input("Escribe algo: ", "Este es mi texto")
st.write("El texto escrito es: ", texto)

col1, col2 = st.columns(2)

with col1:
  st.subheader("Este es una descripción de la raza")
  st.write("El perro proviene de la China")
  resp = st.checkbox("Estoy de acuerdo")
  if resp:
    st.write("Correcto")
