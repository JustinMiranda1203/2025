from PyQt6.QtWidgets import QApplication , QMainWindow ,QComboBox 
import sys

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        desplegable = QComboBox()
        desplegable.addItems(['opcion 1 ' , 'opcion 2'])

        desplegable.currentIndexChanged.connect(self.indice_cambiado)
        desplegable.currentTextChanged.connect(self.indice_seleccionado)
        self.setCentralWidget(desplegable)


    def indice_cambiado(self , indice):
        print(f'el indice seleccionado es {indice}')
    def indice_seleccionado(self, texto):
        print(f'el texto seleccionado es {texto}')

def main():
    print ("dentro del main")
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
if __name__== "__main__":
    main()