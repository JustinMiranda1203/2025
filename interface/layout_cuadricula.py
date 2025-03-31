from PyQt6.QtWidgets import QApplication , QMainWindow , QGridLayout,QWidget
import sys

from layoutsBasicos import caja

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        layout=QGridLayout()
        widget = QWidget()
        widget.setLayout(layout)

        caja1 = caja('#484589')
        caja2 = caja('#348904')
        caja3 = caja('blue')

        layout.addWidget(caja1 , 0 ,0)
        layout.addWidget(caja2 , 1 , 1, 1, 2)
        layout.addWidget(caja3 , 0 , 3, 3, 1)

        self.setCentralWidget(widget)
        self.resize(350 , 250)

def main():
    print ("dentro del main")
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
if __name__== "__main__":
    main()