from alternativa import Alternativas

class Preguntas:
    def __init__(self, enunciado:str, ayuda:str, indicacion_requerida:str):
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.indicaion_requerida = indicacion_requerida
        self.__lista_alternativas = [Alternativas()]

    @property
    def lista_alternativas(self):
        return self.__lista_alternativas

    def mostrar_preguntas(self):
        if self.ayuda != "":
            return f"""
            Enunciado de la pregunta: {self.enunciado}
            Ayuda: {self.ayuda}
            Alternativas: {self.lista_alternativas}
        """

        else:
            return f"""
            Enunciado de la pregunta: {self.enunciado}
            Alternativas: {self.lista_alternativas}
        """