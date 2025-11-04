import streamlit as st
from views import View
import time

class AvaliarProfissionalUI:
    def main():
        st.header("Avaliar Profissional")
        op = View.cliente_listar_id(st.session_state["usuario_id"])
        horarios = View.horario_listar()
        profissionais = []

        estrelas = {
            "★★★★★": 5.0,
            "★★★★": 4.0,
            "★★★": 3.0,
            "★★": 2.0,
            "★": 1.0
        }

        if len(horarios) == 0: st.write("Nenhum horário cadastrado")
        for h in horarios:
            if h.get_id_cliente() == op and h.get_id_profissional():
                profissionais.append(View.profissional_listar_id(h.get_id_profissional()))
        else:
            profissional = st.selectbox("Informe o profissional", profissionais)
            avaliacao = st.selectbox("Avaliação", ["★★★★★", "★★★★", "★★★", "★★", "★"])

            if st.button("Avaliar"):
                av = profissional.get_avaliacoes()
                av.append(estrelas[avaliacao])
                profissional.set_avaliacoes(av)
                time.sleep(2)
                st.rerun()

