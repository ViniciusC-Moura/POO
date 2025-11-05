class Avaliacao:
    def __init__(self, id, id_cliente, id_profissional, nota):
        self.set_id(id)
        self.set_id_cliente(id_cliente)
        self.set_id_profissional(id_profissional)
        self.set_nota(nota)

    def __str__(self):
        return f"Avaliacao({self.__id}) - Cliente {self.__id_cliente} → Profissional {self.__id_profissional}: {self.__nota}"

    def get_id(self): return self.__id
    def get_id_cliente(self): return self.__id_cliente
    def get_id_profissional(self): return self.__id_profissional
    def get_nota(self): return self.__nota

    def set_id(self, id):
        if id is None: raise ValueError("Avaliacao.__id não pode ser nulo")
        self.__id = id

    def set_id_cliente(self, id_cliente):
        if id_cliente is None: raise ValueError("Avaliacao.__id_cliente não pode ser nulo")
        self.__id_cliente = id_cliente

    def set_id_profissional(self, id_profissional):
        if id_profissional is None: raise ValueError("Avaliacao.__id_profissional não pode ser nulo")
        self.__id_profissional = id_profissional

    def set_nota(self, nota):
        if nota is None or nota < 0 or nota > 5:
            raise ValueError("Avaliacao.__nota deve estar entre 0 e 5")
        self.__nota = nota


    def to_json(self):
        return {
            "id": self.__id,
            "id_cliente": self.__id_cliente,
            "id_profissional": self.__id_profissional,
            "nota": self.__nota
        }

    @staticmethod
    def from_json(dic):
        return Avaliacao(dic["id"], dic["id_cliente"], dic["id_profissional"], dic["nota"])
