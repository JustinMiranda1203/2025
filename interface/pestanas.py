from PyQt6.QtWidgets import QApplication , QMainWindow , QTabWidget
import sys
from layoutsBasicos import caja

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        contenedor = QTabWidget()
        caja1=caja('green')
        caja2=caja('yellow')
        caja3=caja('Red')

        contenedor.addTab(caja1,'verde')
        contenedor.addTab(caja2,'amarillo')
        contenedor.addTab(caja3,'rojo')
        contenedor.setTabPosition(QTabWidget.TabPosition.West)
        contenedor.setMovable(True)
       
        self.setCentralWidget(contenedor)
   
def main():
    print ("dentro del main")
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
if __name__== "__main__":
    main()