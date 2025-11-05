import json
from models.avaliacao import Avaliacao
from models.DAO import DAO

class AvaliacaoDAO(DAO):
    _objetos = []

    @classmethod
    def abrir(cls):
        cls._objetos = []
        try:
            with open("avaliacoes.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    cls._objetos.append(Avaliacao.from_json(dic))
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("avaliacoes.json", mode="w") as arquivo:
            json.dump(cls._objetos, arquivo, default=Avaliacao.to_json)
