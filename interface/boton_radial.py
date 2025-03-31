from PyQt6.QtWidgets import QApplication , QMainWindow , QRadioButton , QWidget , QVBoxLayout
import sys

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.Boton_Rojo=QRadioButton('rojo')
        self.Boton_amarillo=QRadioButton('amarillo')
        self.Boton_verde=QRadioButton('verde')
        layout=QVBoxLayout()
        widget=QWidget()
        widget.setLayout(layout)

        layout.addWidget(self.Boton_Rojo)
        layout.addWidget(self.Boton_amarillo)
        layout.addWidget(self.Boton_verde)
        self.Boton_Rojo.toggled.connect(self.cambiado)
        self.Boton_amarillo.toggled.connect(self.cambiado)
        self.Boton_verde.toggled.connect(self.cambiado)

        self.setCentralWidget(widget)

    def cambiado(self , Valor):
      boton:QRadioButton=self.sender()
      if boton.isChecked():
       print(Valor , boton.text())

def main():
    print ("dentro del main")
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
if __name__== "__main__":
    main()