from pregunta import Preguntas
from usuario import Usuario
from listado_respuestas import Respuestas

class Encuesta:
    def __init__(self, nombre:str):
        self.nombre = nombre
        self.__listado_preguntas = self.agregar_preguntas()
        self.__listado_respuestas = []


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
    

    def mostrar_encuesta(self):
        encuesta = ""
        for pregunta in self.listado_preguntas:
            encuesta += f"{pregunta.mostrar_pregunta()}\n"
        
        return encuesta
    
    
    def agregar_respuestas(self, usuario, respuestas):
        listado = Respuestas(usuario, respuestas)
        self.listado_respuestas.append(listado)
        return True


class EncuestaRegionLimitada(Encuesta):
    def __init__(self, nombre:str, regiones:list[int]):
        super().__init__(nombre)
        self.__regiones = regiones

    

    ## GETTER Y SETTER LISTADO_REGIONES ##
    @property
    def regiones(self):
        return self.__regiones
    
    @regiones.setter
    def regiones(self, regiones:list[int]):
        self.__regiones = regiones

    def agregar_respuestas(self, usuario:Usuario, respuestas):
        if usuario.region not in self.regiones:
            return False
        else:
            print("Usuario habilitado para realizar la encuesta")
            return super().agregar_respuestas(usuario, respuestas)




class EncuestaEdadLimitada(Encuesta):
    def __init__(self, nombre, edad_min, edad_max):
        super().__init__(nombre)
        self.__edad_min = edad_min
        self.__edad_max = edad_max

    ## GETTER Y SETTER EDAD_MIN ##
    @property
    def edad_min(self):
        return self.__edad_min
    
    @edad_min.setter
    def edad_min(self, edad_min:int):
        self.__edad_min = edad_min
    
    ## GETTER Y SETTER EDAD_MAX ##
    @property
    def edad_max(self):
        return self.__edad_max
    
    @edad_max.setter
    def edad_max(self, edad_max:int):
        self.__edad_max = edad_max

    def agregar_respuestas(self, usuario:Usuario, respuestas):
        if usuario.edad not in range(self.edad_min, self.edad_max + 1):
            return False
        else:
            print("Usuario habilitado para realizar la encuesta")
            return super().agregar_respuestas(usuario, respuestas)