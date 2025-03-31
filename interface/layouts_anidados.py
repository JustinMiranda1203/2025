from PyQt6.QtWidgets import QApplication , QMainWindow ,QLabel , \
    QHBoxLayout , QWidget , QVBoxLayout , QPushButton ,QCheckBox ,QSpinBox
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
import sys

class Caja(QLabel):
    def __init__(self , color):
        super().__init__()
        self.setStyleSheet(f"background-color: {color}")

class Ventana(QMainWindow):
     def __init__(self):
        super().__init__()

        layout_vertical_1 = QVBoxLayout()

        caja1= Caja('red')
        caja2= Caja('blue')
        caja3= Caja('yellow')

        textto_titulo=QLabel('proyecto')
        fuente =QFont('manjari',18)
        textto_titulo.setFont(fuente)
        textto_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #para los elementos centrales 
        layout_horizontal_2 = QVBoxLayout()
        layout_vertical_2 = QHBoxLayout()
        layout_vertical_2.addLayout(layout_horizontal_2)

        checkbox_activar= QCheckBox('activar')
        estiqueta_temperatura= QLabel('temp')
        spin_temperatura = QSpinBox()

        layout_horizontal_2.addWidget(checkbox_activar)  
        layout_horizontal_2.addWidget(estiqueta_temperatura)
        layout_horizontal_2.addWidget(spin_temperatura)
        

       

        layout_horizontal_1=QHBoxLayout()

        layout_vertical_1.addWidget(textto_titulo)
        layout_vertical_1.addLayout(layout_horizontal_2)
        layout_vertical_1.addLayout(layout_horizontal_1)

        boton_aceptar = QPushButton('aceptar')
        boton_cancelar = QPushButton('cancelar')
        boton_aplicar = QPushButton('aplicar')

        layout_horizontal_1.addWidget(boton_aceptar)
        layout_horizontal_1.addWidget(boton_cancelar)
        layout_horizontal_1.addWidget(boton_aplicar)
        
        
        widget= QWidget()
        widget.setLayout(layout_vertical_1)

        self.setCentralWidget(widget)
        

def main():
     print ("dentro del main")
     app = QApplication(sys.argv)
     ventana = Ventana()
     ventana.show()
     sys.exit(app.exec())
if __name__== "__main__":
    main()
