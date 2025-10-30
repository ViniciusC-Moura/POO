from models.cliente import Cliente
from models.clienteDAO import ClienteDAO

from models.servico import Servico
from models.servicoDAO import ServicoDAO

from models.horario import Horario
from models.horarioDAO import HorarioDAO

from models.profissional import Profissional
from models.profissionalDAO import ProfissionalDAO

class View:

    def cliente_criar_admin():
        for c in View.cliente_listar():
            if c.get_email() == "admin": return
        View.cliente_inserir("admin", "admin", "fone", "1234")

    def cliente_autenticar(email, senha):
        for c in View.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id": c.get_id(), "nome": c.get_nome()}
        return None

    def cliente_listar():
        return ClienteDAO.listar()
    def cliente_listar_id(id):
        c = ClienteDAO.listar_id(id)
        return c
    def cliente_inserir(nome, email, fone, senha):
        if not nome or not email or not fone or not senha: raise ValueError("Nenhum valor pode ser nulo.")
        if email == "admin": raise PermissionError("Email 'admin' não pode ser criado.")
        for i in View.cliente_listar():
            if email == i.get_email(): raise ValueError("Já existe alguém com esse email.")
        for i in View.profissional_listar():
            if email == i.get_email(): raise ValueError("Já existe alguém com esse email.")
        
        cliente = Cliente(0, nome, email, fone, senha)
        ClienteDAO.inserir(cliente)
    def cliente_atualizar(id, nome, email, fone, senha):
        if not id or not nome or not email or not fone or not senha: raise ValueError("Nenhum valor pode ser nulo.")
        if email == "admin": raise PermissionError("Email 'admin' não pode ser criado.")
        for i in View.cliente_listar():
            if email == i.get_email(): raise ValueError("Já existe alguém com esse email.")
        for i in View.profissional_listar():
            if email == i.get_email(): raise ValueError("Já existe alguém com esse email.")

        cliente = Cliente(id, nome, email, fone, senha)
        ClienteDAO.atualizar(cliente)
    def cliente_excluir(id):
        for i in View.horario_listar():
            if id == i.get_id_cliente():
                raise PermissionError("Cliente já tem um horário agendado.")
        cliente = Cliente(id, "", "", "", "")
        ClienteDAO.excluir(cliente)

    def servico_listar():
        return ServicoDAO.listar()
    def servico_listar_id(id):
        c = ServicoDAO.listar_id(id)
        return c
    def servico_inserir(descricao, valor):
        servico = Servico(0, descricao, valor)
        ServicoDAO.inserir(servico)
    def servico_atualizar(id, descricao, valor):
        servico = Servico(id, descricao, valor)
        ServicoDAO.atualizar(servico)
    def servico_excluir(id):
        servico = Servico(id, "", 0)
        ServicoDAO.excluir(servico)

    def horario_listar():
        return HorarioDAO.listar()
    def horario_listar_id(id):
        horario = HorarioDAO.listar_id(id)
        return horario
    def horario_inserir(data, confirmado, id_cliente, id_servico, id_profissional):
        for h in View.horario_listar():
            if data == h.get_data() and id_profissional == h.get_id_profissional:
                raise PermissionError("Profissional já tem esse horário agendado")
        c = Horario(0, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        c.set_id_profissional(id_profissional)
        HorarioDAO.inserir(c)
    def horario_atualizar(id, data, confirmado, id_cliente, id_servico, id_profissional):
        for h in View.horario_listar():
            if data == h.get_data() and id_profissional == h.get_id_profissional:
                raise PermissionError("Profissional já tem esse horário agendado")
        c = Horario(id, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        c.set_id_profissional(id_profissional)
        HorarioDAO.atualizar(c)
    def horario_excluir(id):
        if View.horario_listar_id(id).get_id_cliente():
            raise PermissionError("Não é possível deletar horários com cliente")        
        c = Horario(id, None)
        HorarioDAO.excluir(c)

    def profissional_autenticar(email, senha):
        for p in View.profissional_listar():
            if p.get_email() == email and p.get_senha() == senha:
                return {"id": p.get_id(), "nome": p.get_nome()}
        return None

    def profissional_listar():
        return ProfissionalDAO.listar()
    def profissional_listar_id(id):
        profissional = ProfissionalDAO.listar_id(id)
        return profissional
    def profissional_inserir(nome, especialidade, conselho, email, senha):
        if not nome or not email or not especialidade or not senha or not conselho: raise ValueError("Nenhum valor pode ser nulo.")
        if email == "admin": raise PermissionError("Email 'admin' não pode ser criado.")
        for i in View.cliente_listar():
            if email == i.get_email(): raise ValueError("Já existe alguém com esse email.")
        for i in View.profissional_listar():
            if email == i.get_email(): raise ValueError("Já existe alguém com esse email.")
        c = Profissional(0, nome, especialidade, conselho, email, senha)
        ProfissionalDAO.inserir(c)
    def profissional_atualizar(id, nome, especialidade, conselho, email, senha):
        if not nome or not email or not especialidade or not senha or not conselho: raise ValueError("Nenhum valor pode ser nulo.")
        if email == "admin": raise PermissionError("Email 'admin' não pode ser criado.")
        for i in View.cliente_listar():
            if email == i.get_email(): raise ValueError("Já existe alguém com esse email.")
        for i in View.profissional_listar():
            if email == i.get_email(): raise ValueError("Já existe alguém com esse email.")
        c = Profissional(id, nome, especialidade, conselho, email, senha)
        ProfissionalDAO.atualizar(c)
    def profissional_excluir(id):
        for i in View.horario_listar():
            if id == i.get_id_profissional():
                raise PermissionError("Profissional já tem um horário agendado.")
        c = Profissional(id, "", "", "", "", "")
        ProfissionalDAO.excluir(c)

