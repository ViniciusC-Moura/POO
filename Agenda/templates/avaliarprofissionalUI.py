import streamlit as st
from views import View
import time

class AvaliarProfissionalUI:
    def main():
        st.header("Avaliar Profissional")
        op = st.session_state["usuario_id"]
        horarios = View.horario_listar()
        profissionais_dict = {}

        estrelas = {
            "★★★★★": 5.0,
            "★★★★": 4.0,
            "★★★": 3.0,
            "★★": 2.0,
            "★": 1.0
        }

        for h in horarios:
            if h.get_id_cliente() == op:
                p = View.profissional_listar_id(h.get_id_profissional())
                if p is not None:
                    profissionais_dict[p.get_id()] = p

        profissionais = list(profissionais_dict.values())

        if len(profissionais) == 0: st.write("Nenhum profissional a ser avaliado")
        else:
            profissional = st.selectbox("Informe o profissional", list(profissionais))
            avaliacao = st.selectbox("Avaliação", ["★★★★★", "★★★★", "★★★", "★★", "★"])

            if st.button("Avaliar"):
                nota = estrelas[avaliacao]
                avaliacoes = View.avaliacao_listar()
                existente = None

                for a in avaliacoes:
                    if a.get_id_cliente() == op and a.get_id_profissional() == profissional.get_id():
                        existente = a
                        break

                if existente:
                    View.avaliacao_atualizar(existente.get_id(), op, profissional.get_id(), nota)
                else:
                    View.avaliacao_inserir(op, profissional.get_id(), nota)

                st.success("Avaliação registrada com sucesso.")
                time.sleep(2)
                st.rerun()