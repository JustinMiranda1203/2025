from PyQt6.QtWidgets import QApplication , QMainWindow , QCheckBox
from PyQt6.QtCore import Qt
import sys

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()

        casilla = QCheckBox('activar')
        casilla.setTristate(True)
        casilla.stateChanged.connect(self.modificar_estado)
        casilla.setCheckState(Qt.CheckState.PartiallyChecked)

        self.setCentralWidget(casilla)

    def modificar_estado(self , valor):
        print(valor)
        if valor == Qt.CheckState.Checked.value:
            print("casilla activada")
        elif valor == Qt.CheckState.Unchecked.value:
            print("casilla desactivada")
        elif valor == Qt.CheckState.PartiallyChecked.value:
            print("casilla parcialmente desactivada")

def main():
    print ("dentro del main")
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
if __name__== "__main__":
    main()