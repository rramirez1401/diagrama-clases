from pregunta import Preguntas

class Encuesta:
    def __init__(self, nombre:str):
        self.nombre = nombre
        self.__listado_preguntas = self.agregar_preguntas()
        self.__listado_respuestas = self.agregar_respuestas()


    ## GETTER LISTADO_PREGUNTAS ##
    @property
    def listado_preguntas(self):
        return self.__listado_preguntas

    ## GETTER LISTADO_RESPUESTAS ##
    @property
    def listado_respuestas(self):
        return self.__listado_respuestas


    def agregar_preguntas(self):
        preguntas = []

        cantidad_preguntas = int(input("Cuantas preguntas quieres agregar?\n    >>> "))
        ayuda = input("Quieres agregar ayuda?(Enter para omitir\n    >>> ")
        requerida = input("Es requerida? SI/NO\n    >>> ").lower()

        for i in range(1, (cantidad_preguntas + 1)):
            enunciado = input(f"Ingrese el enunciado de la pregunta {i}: ")

            if ayuda != "" and requerida == "si":
                preguntas.append(Preguntas(enunciado, ayuda, requerida))
            elif ayuda == "" and requerida == "si":
                preguntas.append(Preguntas(enunciado, requerida))
            elif ayuda != "" and requerida == "no":
                preguntas.append(Preguntas(enunciado, ayuda))
            else:
                preguntas.append(Preguntas(enunciado))

        return preguntas
    
    def agregar_respuestas(self):
        pass

    def mostrar_encuesta(self):
        encuesta = ""
        for pregunta in self.listado_preguntas:
            encuesta += f"{pregunta.mostrar_preguntas()}\n"
        
        return encuesta

class EncuestaEdadLimitada(Encuesta):
    def __init__(self, nombre, regiones):
        super().__init__(nombre)
        self.regiones = regiones
    pass


class EncuestaRegionLimitada(Encuesta):
    pass