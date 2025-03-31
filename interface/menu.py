from PyQt6.QtWidgets import QApplication , QMainWindow , QStatusBar
from PyQt6.QtGui import QAction , QIcon
import sys
from etiquetas import abs_path

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        menu= self.menuBar()
        self.setStatusBar(QStatusBar())
        menu=self.menuBar()
        menu_archivo = menu.addMenu('archivo')
        menu_archivo.addAction('abrir')
        print(abs_path('Satoru.jpg'))
        menu_archivo.addAction(QIcon(abs_path('Satoru.jpg')), 'salir','ctrl+Q', self.close)

        accion_mostrar=QAction('mostrar',self)
        accion_mostrar.setShortcut('ctrl+f')
        accion_mostrar.setIcon(QIcon(abs_path('Satoru.jpg')))
        accion_mostrar.triggered.connect(self.mi_Funcion_super_importante)
        accion_mostrar.setStatusTip('comando importante')

        menu_editar = menu.addMenu('editar')
        menu_editar.addAction(accion_mostrar)
        menu_ayuda = menu.addMenu('ayuda')

    def mi_Funcion_super_importante(self):
        print('seesta realizandouna accion')


        self.resize(400 , 350)

def main():
    print ("dentro del main")
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
if __name__== "__main__":
    main()