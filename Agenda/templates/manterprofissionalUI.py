import streamlit as st
import pandas as pd
import time
from views import View

class ManterProfissionalUI:

    def main():
        st.header("Cadastro de Profissionais")

        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterProfissionalUI.listar()
        with tab2: ManterProfissionalUI.inserir()
        with tab3: ManterProfissionalUI.atualizar()
        with tab4: ManterProfissionalUI.excluir()

    def listar():
        profissionais = View.profissional_listar()
        if len(profissionais) == 0:
            st.write("Nenhum profissional cadastrado")

        else:
            list_dic = []
            for obj in profissionais:
                list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    def inserir():
        email = st.text_input("Informe o email")
        senha = st.text_input("Informe a senha")
        nome = st.text_input("Informe o nome")
        especialidade = st.text_input("Informe a especialidade")
        conselho = st.text_input("Informe o conselho")
        if st.button("Inserir"):
            try:
                View.profissional_inserir(email, senha, nome, especialidade, conselho)
                st.success("Profissional inserido com sucesso")
                time.sleep(2)
                st.rerun()
            except ValueError:
                st.write("Email já registrado ou campo vazio.")
            except PermissionError:
                st.write("Não é permitido criar um email 'admin'")

    def atualizar():
        profissionais = View.profissional_listar()
        if len(profissionais) == 0: st.write("Nenhum profissional cadastrado")
        else:
            op = st.selectbox("Atualização de Profissionais", profissionais)
            nome = st.text_input("Informe o novo nome", op.get_nome())
            especialidade = st.text_input("Informe o nova especialidade", op.get_especialidade())
            conselho = st.text_input("Informe o novo conselho", op.get_conselho())
            if st.button("Atualizar"):
                try:
                    id = op.get_id()
                    View.profissional_atualizar(id, nome, especialidade, conselho)
                    st.success("Profissional atualizado com sucesso")
                    time.sleep(2)
                    st.rerun()
                except ValueError:
                    st.write("Email já registrado ou campo vazio.")
                except PermissionError:
                    st.write("Não é permitido criar um email 'admin'")


    def excluir():
        profissionais = View.profissional_listar()
        if len(profissionais) == 0: st.write("Nenhum profissional cadastrado")
        else:
            op = st.selectbox("Exclusão de Profissionais", profissionais)
            if st.button("Excluir"):
                try:
                    id = op.get_id()
                    View.profissional_excluir(id)
                    st.success("Profissional excluído com sucesso")
                    time.sleep(2)
                    st.rerun()
                except PermissionError:
                    st.write("Não é possível excluir profissional com horário agendado.")