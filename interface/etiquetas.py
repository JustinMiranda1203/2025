from PyQt6.QtWidgets import QApplication , QMainWindow , QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap ,QFont
from pathlib import Path
import sys

def abs_path(nombre):
    return str(Path(__file__).parent.absolute() / nombre)

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        etiqueta = QLabel('saludos')
        etiqueta.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)
        fuente = QFont('manjari', 20)
        etiqueta.setFont(fuente)
        self.setCentralWidget(etiqueta)
        imagen = QPixmap(abs_path("Satoru.jpg"))
        etiqueta.setPixmap(imagen)
        etiqueta.setScaledContents(True)
        #self.resize(400 , 250)
        #self.setFixedSize(400 , 290)

def main():
    print ("dentro del main")
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
if __name__== "__main__":
    main()