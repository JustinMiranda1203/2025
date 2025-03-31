from PyQt6.QtWidgets import QApplication , QMainWindow ,QLabel , \
    QHBoxLayout , QWidget , QVBoxLayout
import sys

class caja(QLabel):
    def __init__(self , color):
        super().__init__()
        self.setStyleSheet(f"background-color: {color}")


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()

        layout=QVBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)

        Caja1 = caja("red")
        Caja2 = caja("magenta")
        Caja3 = caja("yellow")
        Caja4 = caja("green")

        layout.addWidget(Caja1)
        layout.addWidget(Caja2)
        layout.addWidget(Caja3)
        layout.addWidget(Caja4)
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

def main():
    print ("dentro del main")
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
if __name__== "__main__":
    main()