from PyQt6.QtWidgets import QApplication, QMainWindow, \
    QLabel, QWidget, \
    QGridLayout, QHBoxLayout, QVBoxLayout


from PyQt6.QtCore import QRunnable, QThreadPool, pyqtSignal as Signal, \
    QObject, Qt


import sys 

class Caja(QLabel):
    def _init_(self, color):
        super()._init_() 
        self.setStyleSheet(f"background-color:  {color}")

class WorkerSignals(QObject):
    luz_roja = Signal(bool)
    luz_amarillo = Signal(bool)
    luz_verde = Signal(bool)

    def _init_(self):
        super()._init_()

class Worker(QRunnable):
    def _init_(self):
        super()._init_()

class Ventana(QMainWindow):
    def _init_(self):
        super()._init_()
        self.Signals = WorkerSignals

        def prender_luz_roja(self, estado:bool = False):
            try:
                self.signals.luz_roja.emit(estado)
            except Exception as e:
                print ("se obtuvo un error al emitir l señal ")


        contenedor0 = QGridLayout()

        widget = QWidget()
        widget.setLayout(contenedor0)
        self.setCentralWidget(widget)

        caja0 = Caja('red')
        caja1 = Caja('blue')
        caja2 = Caja('gray')

        Layout_vertical1 = QVBoxLayout()
        self.indicador_rojo = self.crear_indicador('red')
        self.indicador_amarillo = self.crear_indicador('yellow')
        self.indicador_verde = self.crear_indicador('green')
        Layout_vertical1.addWidget(self.indicador_rojo)
        Layout_vertical1.addWidget(self.indicador_amarillo)
        Layout_vertical1.addWidget(self.indicador_verde)

        contenedor0.addLayout(Layout_vertical1, 0, 0)
        contenedor0.addWidget(caja1, 0, 1)
        contenedor0.addWidget(caja2, 1, 0, 1, 2)

        self.setWindowTitle("Semaforo")
        self.resize(350, 250)

        #enlazar con el worker
        self.threadpool=QThreadPool()
        self.worker = Worker()
        self.worker.signals.luz_roja.connect(self.cambiar_indicador_rojo)
        self.worker.signals.luz_amarillo.connect(self.cambiar_indicador_amarillo)
        self.worker.signals.luz_verde.connect(self.cambiar_indicador_verde)
        def cambiar_indicador_Rojo(self , estado:bool):
            if estado:
              self.modificar_indicador(self.indicador_rojo , 'red')
            else:
               self.modificar_indicador(self.indicador_rojo,'gray')
        
        def cambiar_indicador_amarillo(self , estado:bool):
            if estado:
              self.modificar_indicador(self.indicador_rojo , 'red')
            else:
               self.modificar_indicador(self.indicador_rojo,'gray')
        
        def cambiar_indicador_verde(self , estado:bool):
            if estado:
              self.modificar_indicador(self.indicador_rojo , 'red')
            else:
               self.modificar_indicador(self.indicador_rojo,'gray')


        def crear_indicador(self, color:str = "gray"):
           mi_caja = QLabel()
           mi_caja.setStyleSheet(f"""
            background-color:  {color};
            border-radius: 30
             """)

        def modificar_indicador(self, indicador ,color):
           indicador.setStyleSheet(f"""backround-color:{color};border-radius:38""")

        mi_caja = QLabel()
        mi_caja.setFixedSize(60,60)
        return mi_caja
    
        def obtener_worker(self):
            return self.worker

        
def main():
    print('Dentro de main')
    app = QApplication(sys.argv)
    ventana = Ventana ()
    ventana.show()
    sys.exit(app.exec())

if __name__=='main_':
    main()