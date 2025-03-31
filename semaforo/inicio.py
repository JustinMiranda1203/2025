from PyQt6.QtWidgets import QApplication
import sys

from interface import Ventana
from control import Semaforo

class inicio(Ventana):
    def __init__(self):
        super().__init__()
        semaforo=Semaforo()
        semaforo.iniciar()
        semaforo.establecer_worker(self.obtener_worker())


def main():
    print('Dentro de main')
    app = QApplication(sys.argv)
    ventana = Ventana ()
    ventana.show()
    sys.exit(app.exec())

if __name__=='main_':
    main()