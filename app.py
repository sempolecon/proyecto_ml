import streamlit as st
import pickle
import numpy as np

st.title("Primer modelo")

with open("model.pickle", "rb") as f:
    modelo = pickle.load(f)

# seleccionar la educación

educ = st.slider("Años de educación", 0, 25)

# seleccionar la experiencia

exper = st.slider("Años de experiencia", 0, 45)

vec = np.array([[educ, exper]])

if st.button("Predecir"):
    res = modelo.predict(vec)[0]
    st.write(f"Su salario en 1976 sería de {round(res,1)} por hora.")

