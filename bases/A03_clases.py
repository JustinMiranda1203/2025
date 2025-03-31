from A02_utils import nuevo_subtema


class persona:
    #constructor
    def __init__(self ,nombre,apellido):
        pass
        self.nombre = nombre
        self.apellido = apellido
        self.edad = 0
        self.altura = None
        self.altura = None
        self.color_de_ojos = ""

    def saludar(self):
     print (f"¡hola <3!, mi nombre es {self.nombre} {self.apellido} ¿como estas?")

    def ir_a_cenar(self,con_quien):
       print(f"hola: {con_quien}! me invitas a cenar esta noche ")

    def establecer_altura(self, valor):
       self.altura=valor
    def establecer_ojos(self,color:str):
       self.color_de_ojos = color
    #metodo tostr
    def __str__(self):
        pass

Daniela = persona("Daniela","De Miranda")
Daniela.establecer_altura(1.76)
Daniela.establecer_ojos("miel")
Daniela.saludar()
Daniela.ir_a_cenar("justin")

nuevo_subtema("Ahora con victor")
amayrani = persona("Amayrani", "Fuentes")
amayrani.ir_a_cenar("victor")

