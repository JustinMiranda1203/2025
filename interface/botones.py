from PyQt6.QtWidgets import QApplication , QMainWindow , QPushButton
import sys
class Ventana(QMainWindow):
    def __init__(self):
     super().__init__()
     boton=QPushButton('precione el boton')
    #  boton.clicked.connect(self.boton_clickeado)
    #  boton.pressed.connect(self.boton_precionado)
    #  boton.released.connect(self.boton__liberado)
     boton.setCheckable(True)
     boton.clicked.connect(self.boton_con_estado)
     self.setCentralWidget(boton)
     self.setWindowTitle('botones')
     #self.resize(300 , 250)
     #self.setMinimumSize(200 , 250)
     #self.setMaximumSize(500 , 350)
     self.setFixedSize(400 , 200)
     print('dentro del constructor')
    def boton_precionado(self):
       print('se ha precionado el boton')
    def boton__liberado(self):
       print('se ha liberado el boton')
    def boton_clickeado(self):
       print('se ha clickeado el boton')
    def boton_con_estado(self , valor):
       print(valor)

def main():
    print ("dentro del main")
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
if __name__== "__main__":
    main()

