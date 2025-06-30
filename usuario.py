from listado_respuestas import Respuestas
from encuesta import Encuesta, EncuestaEdadLimitada, EncuestaRegionLimitada

class Usuario:
    def __init__(self, correo, edad, region):
        self.__correo = correo
        self.__edad = edad
        self.__region = region

    ## GETTER Y SETTER CORREO ##
    @property
    def correo(self):
        return self.__correo
    
    @correo.setter
    def correo(self, nuevo_correo):
        self.__correo = nuevo_correo

    ## GETTER Y SETTER EDAD ##
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, nueva_edad):
        self.__edad = nueva_edad

    ## GETTER Y SETTER REGION ##
    @property
    def region(self):
        return self.__region
    
    @region.setter
    def region(self, nueva_region):
        self.__region = nueva_region
    


    def responder_encuesta(self, encuesta):
        respuestas = []
        
        for pregunta in encuesta.listado_preguntas:
            print(pregunta.mostrar_pregunta())
            respuesta = int(input("Ingresa el número con el indice de tu respuesta:\n    >>> "))
            respuestas.append(respuesta)

        verificar_agregar = encuesta.agregar_respuestas(self, respuestas)
        if not verificar_agregar:
            print("No estaás habilitado para responder la encuesta")
        else:
            print("Respuestas agregadas")
        