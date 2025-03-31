import threading
import time
from temporizador import Temporizador
from interface import Worker

class Semaforo():

    def __init__(self):
        print("dentro de semaforo")

        self.TON_0= Temporizador("TON_00", 6)
        self.TON_1= Temporizador("TON_01", 2)
        self.TON_2= Temporizador("TON_02", 4)
        self.M0=True
        self.luz_roja = False
        self.luz_amarillo = False
        self.luz_verde = False
        
        self.worker:Worker= None

        self.tarea = threading.Thread(target=self.semaforo_funcionando) 
        
       
    def iniciar(self):
        if self.tarea:
            self.tarea.start()

    def semaforo_funcionando(self):
        while True:

            self.TON_0.entrada = self.M0 and not self.TON_2.salida
            self.TON_0.actualizar()
            self.TON_1.entrada = self.M0 and self.TON_0.salida
            self.TON_1.actualizar()
            self.TON_2.entrada = self.M0 and self.TON_1.salida
            self.TON_2.actualizar()

            self.luz_roja = self.M0 and not self.TON_0.salida
            self.luz_amarillo = self.M0 and self.TON_0.salida and not self.TON_1.salida
            self.luz_verde = self.M0 and self.TON_1.salida

            print(f'R:{self.luz_roja} a:{self.luz_amarillo} v:{self.luz_verde}')
              #mapeado de interface
            if self.worker:
                self.worker.prender_luz_roja(self.luz_roja)

            time.sleep(0.01)

    def establecer_worker(self,worker):
        self.worker = worker

def main():
    print("dentro de main")
    semaforo=Semaforo()
    semaforo.iniciar()
if __name__=="__main__":
    main()