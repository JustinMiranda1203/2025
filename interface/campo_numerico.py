from PyQt6.QtWidgets import QApplication , QMainWindow, QSpinBox , QDoubleSpinBox
from PyQt6.QtGui import QFont
import sys

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()

        campo_numerico=QDoubleSpinBox()
        #campo_numerico.setMaximum(30)
        #campo_numerico.setMinimum(-10)
        campo_numerico.setRange(-10 , 30)
        campo_numerico.setPrefix('temp:')
        campo_numerico.setSuffix('°c')
        campo_numerico.setSingleStep(0.5)

        fuente = QFont('Arial', 50)
        campo_numerico.setFont(fuente)
        campo_numerico.valueChanged.connect(self.cambiar_valor)

        self.setCentralWidget(campo_numerico)

    def cambiar_valor(self , value):
         print(value)

def main():
    print ("dentro del main")
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
if __name__== "__main__":
    main()

