from usuario import Usuario

class Respuestas:
    def __init__(self, usuario:Usuario, lista_respuestas:list[int]):
        self.usuario = usuario
        self.__lista_respuestas = lista_respuestas

    ## GETTER USUARIO ##
    @property
    def usuario(self):
        return self.__usuario


    ## GETTER LISTADO_RESPUESTAS ##
    @property
    def lista_respuestas(self):
        return self.__lista_respuestas


