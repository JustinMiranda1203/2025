
import time

import threading


class programa:
    def __init__(self , nombre , tiempo):
        self.nombre=nombre
        self.tiempo=tiempo
        print(f'iniciar tarea con el nombre {self.nombre}')
        print('iniciando programa')
        tarea1=threading.Thread(target=self.corre)
        tarea1.start()

    def corre(self):
        print(f'se iniciara la operacion del programa{self.nombre}')
        time.sleep(self.tiempo)
        print(f'terminando la tarea{self.nombre}')
       
   
    def mostrar(self):
        print('mostrar algo')


def main():
    print('dentro del main')
    tarea2 = programa('estructura',5)
    tarea1 = programa('electronica',8)
    #despulpadora.corre()
    #despulpadora.mostrar()

if __name__=='__main__':
    main()