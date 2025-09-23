class Servico:
    def __init__(self, id, descricao, valor):
        self.set_id(id)
        self.set_descricao(descricao)
        self.set_valor(valor)

    def set_id(self, v): self.__id = v
    def set_descricao(self, v): self.__descricao = v
    def set_valor(self, v): self.__valor = v

    def get_id(self): return self.__id
    def get_descricao(self): return self.__descricao
    def get_valor(self): return self.__valor

    def __str__(self):
        return f"Serviço {self.__id} | {self.__descricao} | Valor: {self.__valor}"

    def to_json(self):
        dic = {"id":self.__id, "descricao":self.__descricao, "valor":self.__valor}
        return dic

    @staticmethod
    def from_json(dic):
        return Servico(dic["id"], dic["descricao"], dic["valor"])