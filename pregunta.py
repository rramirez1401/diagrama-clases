from alternativa import Alternativas

class Preguntas:
    def __init__(self, enunciado:str, ayuda:str="", indicacion_requerida:str="No"):
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.indicacion_requerida = indicacion_requerida
        self.__lista_alternativas = self.agregar_alternativas()

    @property
    def lista_alternativas(self):
        return self.__lista_alternativas
    
    def __len__(self):
        return len(self.lista_alternativas)


    def agregar_alternativas(self):
        alternativas = []
        print("Quieres agregar ayuda?(Enter para omitir)")
        ayuda = input("    >>> ")
        for i in range(1, 5):
            texto = input(f"Ingrese el texto de la alternativa {i}: ")
            if i == 1 and ayuda != "":
                alternativas.append(Alternativas(texto, ayuda))
            else:
                alternativas.append(Alternativas(texto))
        return alternativas


    def mostrar_pregunta(self):
        pregunta = ""
        if self.ayuda != "":
            pregunta += f"""
            Enunciado de la pregunta: {self.enunciado}
            Ayuda: {self.ayuda}
            Es requerida: {self.indicacion_requerida}
        """

        else:
            pregunta += f"""
            Enunciado de la pregunta: {self.enunciado}
            Es requerida: {self.indicacion_requerida}
        """
        for alternativa in self.lista_alternativas:
            pregunta += f"{alternativa.mostrar_alternativa()}"

        return pregunta

