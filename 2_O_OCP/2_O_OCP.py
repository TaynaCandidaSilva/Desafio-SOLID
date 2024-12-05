from abc import ABC, abstractmethod


class AprovaExame(ABC):
    @abstractmethod
    def aprovar_solicitacao_exame(self, exame):
        pass

    @abstractmethod
    def verifica_condicoes_exame_sangue():
        pass


class AprovaExameSangue(AprovaExame):
    def aprovar_solicitacao_exame(self, exame):
        if self.verifica_condicoes_exame():
            print("Exame de sangue aprovado")

    def verifica_condicoes_exame(self, exame):
        pass


class AprovaRaioX(AprovaExame):
    def aprovar_solicitacao_exame(self, exame):
        if self.verifica_condicoes_exame(exame):
            print("Raio-X aprovado")

    def verifica_condicoes_exame(self, exame):
        pass


class Exame:
    def __init__(self, tipo):
        self.tipo = tipo


exame_sangue = Exame("sangue")
exame_raio_x = Exame("raio-x")

aprovar_sangue = AprovaExameSangue()
aprovar_raio_x = AprovaRaioX()

aprovar_sangue.aprovar_solicitacao_exame(exame_sangue)
aprovar_raio_x.aprovar_solicitacao_exame(exame_raio_x)
