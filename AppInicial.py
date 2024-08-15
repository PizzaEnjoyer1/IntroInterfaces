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
    

with col2:
  st.subheader("Esta es la segunda columna")
  modo = st.radio("Qué es la comida favorita de un pug", ("Lechuga", "Tomate", "Carne"))

if modo == "Lechuga":
  st.write("Solo si tiene salsa BBQ")

if modo == "Tomate":
  st.write("Si también viene con una hamburguesa")

if modo == "Carne":
  st.write("Correcto, los pugs, al igual que cualquier otro perro, son animales carnívoros")

st.subheader("Uso de botones")
if st.button("Presiona el botón"):
  st.write("Gracias por presionar")
else:
  st.write("Presione el botón o este perro no recibirá cuido")

with st.sidebar:
  st.subheader("Configura la contextura del perro")
  mod_radio = st.radio(
    "Escoge la modalidad a usar",
    ("Flaco", "Rellenito", "Obeso")
  )
