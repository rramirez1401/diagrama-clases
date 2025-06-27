

class Alternativas:
    def __init__(self, contenido:str, ayuda:str=""):
        self.contenido = contenido
        self.ayuda = ayuda

    
    def mostrar_alternativa(self):
        if self.ayuda != "":
            return f"Alternativas: {self.contenido}"
        else:
            return f"""
        Alternativas: {self.contenido}
        Ayuda: {self.ayuda}
        """