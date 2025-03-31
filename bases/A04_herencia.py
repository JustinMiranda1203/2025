from A02_utils import nuevo_tema

class Padre:
    def __init__(self):
        print("soy padre")

    def saludar(self):
        print("hola dentro de padre")

class Madre:
    def __init__(self):
       print("soy madre")
    def comer(self):
        print("dentro de comer")


class Hijo(Padre,Madre):
    def __init__(self):
        #super().__init__()
        Padre.__init__(self)
        Madre.__init__(self)
        print("soy hijo") 
    def saludar(self):
        super().saludar()
        print("dentro de hijo")   

nuevo_tema("Herencias")
#padre = Padre()
hijo = Hijo()
hijo.saludar()
hijo.comer()