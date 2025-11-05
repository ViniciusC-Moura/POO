from templates.manterclienteUI import ManterClienteUI
from templates.manterservicoUI import ManterServicoUI
from templates.manterhorarioUI import ManterHorarioUI
from templates.manterprofissionalUI import ManterProfissionalUI
from templates.alterarsenhaadminUI import AlterarSenhaUI

from templates.abrircontaUI import AbrirContaUI
from templates.loginUI import LoginUI

from templates.perfilclienteUI import PerfilClienteUI
from templates.meusservicos import MeusServicosUI
from templates.avaliarprofissionalUI import AvaliarProfissionalUI

from templates.perfilprofissionalUI import PerfilProfissionalUI
from templates.abriragendaUI import AbrirAgendaUI
from templates.minhaagendaUI import MinhaAgendaUI
from templates.confirmarservicoUI import ConfirmarServicoUI



from views import View

import streamlit as st

class IndexUI:

    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()

    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Meus Serviços", "Avaliar Profissional"])
        if op == "Meus Dados": PerfilClienteUI.main()
        if op == "Meus Serviços": MeusServicosUI.main()
        if op == "Avaliar Profissional": AvaliarProfissionalUI.main()

    def menu_profissional():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Abrir Minha Agenda", "Ver Minha Agenda", "Confirmar Serviço"])
        if op == "Meus Dados": PerfilProfissionalUI.main()
        if op == "Abrir Minha Agenda": AbrirAgendaUI.main()
        if op == "Ver Minha Agenda": MinhaAgendaUI.main()
        if op == "Confirmar Serviço": ConfirmarServicoUI.main()

    def menu_admin():            
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Serviços", "Cadastro de Horários", "Cadastro de Profissionais", "Alterar Senha"])
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Serviços": ManterServicoUI.main()
        if op == "Cadastro de Horários": ManterHorarioUI.main()
        if op == "Cadastro de Profissionais": ManterProfissionalUI.main()
        if op == "Alterar Senha": AlterarSenhaUI.main()

    def sidebar():
        if "usuario_id" not in st.session_state: IndexUI.menu_visitante()
        else:
            admin = st.session_state["usuario_nome"] == "admin"
            st.sidebar.write("Bem-vindo(a), " + st.session_state["usuario_nome"])
            if admin: IndexUI.menu_admin()
            if st.session_state["usuario_nivel"] == "cliente" and not admin: IndexUI.menu_cliente()
            if st.session_state["usuario_nivel"] == "profissional": IndexUI.menu_profissional()
            IndexUI.sair_do_sistema()

    def main():
        IndexUI.sidebar()

    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["usuario_id"]
            del st.session_state["usuario_nome"]
            st.rerun()

IndexUI.main()