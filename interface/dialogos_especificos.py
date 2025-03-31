from PyQt6.QtWidgets import QApplication , QMainWindow , QFileDialog , QInputDialog , QColorDialog , QPushButton , QFontDialog
import sys

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.boton=QPushButton('presioname')
        self.boton.clicked.connect(self.mostrar_dialogo)

        self.setCentralWidget(self.boton)
    
    def mostrar_dialogo(self):
        print('se mostrara el dialogo')
        #archivo,_=QFileDialog.getOpenFileName(self, 'abrir archivo','.') busca archivos
        #print(archivo)
        #archivo,_= QFileDialog.getSaveFileName(self, 'guardar archivo', '.')indica guardar archivos
        #print(archivo)
        #valor,confirmado= QInputDialog.getText(self,'se leera texto', 'texto') texto
        #print(valor,confirmado)
        #valor,confirmado= QInputDialog.getInt(self,'se leera un entero', 'texto') numeros
        #print(valor,confirmado)
        #valor,confirmado= QInputDialog.getDouble(self,'se leera un elemento', 'texto')
        #print(valor,confirmado)
        #valor,confirmado= QInputDialog.getItem(self,'se leera un elemento', 'colores', ['rojo','verde','azul'],editable=False)
        #print(valor,confirmado)

        fuente, confirmado = QFontDialog.getFont(self)
        if confirmado:
            self.boton.setFont(fuente)

        color=QColorDialog.getColor()
        if color.isValid():
            self.boton.setStyleSheet(f'background-color:{color.name()}')
def main():
    print ("dentro del main")
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
if __name__== "__main__":
    main()