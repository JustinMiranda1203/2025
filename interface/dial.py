from PyQt6.QtWidgets import QApplication , QMainWindow , \
QDial
import sys

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        dial=QDial()
        dial.valueChanged.connect(self.valor_cambiado)
        dial.setRange(-10 , 10)
        self.setCentralWidget(dial)
    
    def valor_cambiado(self , valor):
        print(valor)
def main():
    print ("dentro del main")
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
if __name__== "__main__":
    main()