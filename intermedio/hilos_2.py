
import time

import threading


class programa(threading.Thread):
    def __init__(self , nombre , tiempo):
        super().__init__()
        self.nombre=nombre
        self.tiempo=tiempo
        print(f'iniciar tarea con el nombre {self.nombre}')
        #print('iniciando programa')


    def run(self):
        print(f'se iniciara la operacion del programa{self.nombre}')
        time.sleep(self.tiempo)
        print(f'terminando la tarea{self.nombre}')
       
   
    def mostrar(self):
        print('mostrar algo')


def main():
    print('dentro del main')
    tarea1 = programa('estructura',5)
    tarea1.start()
    tarea2 = programa('electronica',8)
    
    #despulpadora.corre()
    #despulpadora.mostrar()

if __name__=='__main__':
    main()