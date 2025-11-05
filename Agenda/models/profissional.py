class Profissional:
    def __init__(self, id, nome, especialidade, conselho, email, senha, avaliacoes):
        self.set_id(id)
        self.set_nome(nome)
        self.set_especialidade(especialidade)
        self.set_conselho(conselho)
        self.set_email(email)
        self.set_senha(senha)
        self.set_avaliacoes(avaliacoes)
        self.set_get_nota()

    def __str__(self):
        return f" {self.__id} - {self.__nome} - {self.__especialidade} - {self.__conselho} - {self.__nota}"

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_especialidade(self): return self.__especialidade
    def get_conselho(self): return self.__conselho
    def get_email(self): return self.__email
    def get_senha(self): return self.__senha
    def get_avaliacoes(self): return self.__avaliacoes
    def get_nota(self): return self.__nota

    def set_id(self, id): 
        if not id: raise ValueError("Profissional.__id não pode ser nulo")
        else: self.__id = id
    def set_nome(self, nome):
        if not nome: raise ValueError("Profissional.__nome não pode ser nulo")
        else: self.__nome = nome
    def set_especialidade(self, especialidade):
        if not especialidade: raise ValueError("Profissional.__especialidade não pode ser nulo")
        else: self.__especialidade = especialidade
    def set_conselho(self, conselho):
        if not conselho: raise ValueError("Profissional.__conselho não pode ser nulo")
        else: self.__conselho = conselho
    def set_email(self, email):
        if not email: raise ValueError("Profissional.__email não pode ser nulo")
        else: self.__email = email
    def set_senha(self, senha):
        if not senha: raise ValueError("Profissional.__senha não pode ser nulo")
        else: self.__senha = senha
    def set_avaliacoes(self, avaliacoes: list):
        self.__avaliacoes = avaliacoes

    def set_get_nota(self):
        if not self.__avaliacoes: self.__nota = 0.0
        else: self.__nota = sum(self.__avaliacoes) / len(self.__avaliacoes)
        return self.__nota

    def to_json(self):
        dic = {"id":self.__id, "nome":self.__nome, "especialidade":self.__especialidade, "conselho":self.__conselho, "email":self.__email, "senha":self.__senha, "avaliacoes":self.__avaliacoes, "nota":self.__nota}
        return dic

    @staticmethod
    def from_json(dic):
        return Profissional(dic["id"], dic["nome"], dic["especialidade"], dic["conselho"], dic["email"], dic["senha"], dic["avaliacoes"])