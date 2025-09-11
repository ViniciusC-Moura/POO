import streamlit as st
from retangulo import Retangulo

class RetanguloUI:
    def main():
        st.header("Cálculos com retângulo")
        base = st.text_input("Medida da base")
        altura = st.text_input("Medida da altura")

        if st.button("Calcular"):
            b = float(base)
            h = float(altura)
            r = Retangulo(b,h)
            st.write(r)
            st.write(r.calc_area())
            st.write(r.calc_diagonal())