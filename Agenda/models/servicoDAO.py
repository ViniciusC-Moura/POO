import json
from models.servico import Servico
from models.DAO import DAO

class ServicoDAO(DAO):
    _objetos = []
    @classmethod
    def abrir(cls):
        cls._objetos = []
        try:
            with open("servicos.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Servico.from_json(dic)
                    cls._objetos.append(obj)

        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("servicos.json", mode="w") as arquivo:
            json.dump(cls._objetos, arquivo, default = Servico.to_json)