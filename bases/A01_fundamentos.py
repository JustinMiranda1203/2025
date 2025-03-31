from A02_utils import nuevo_tema , nuevo_subtema
print("HOLA MUNDO")

#este es un comentario

"""
hoy es jueves 
 y ya quiero salir 
ya me aburri
"""
nuevo_tema('variable')
#variables 
numero=4 # entero
temperatura=26.12 #flotante
nombre='Daniela <3'
fuma = True

print(numero)
print(temperatura)
print(nombre)

print("numero:", numero)
print("temperatura:", temperatura)
print("nombre:", nombre)

print("fuma?", fuma)

print('fuma\n'*2)

print('DANIELA<3\n'*2)

nuevo_tema('listas')
frutas=['manzanas','peras','guayabas','papayas','naranjas','kiwis']
print("frutas:", frutas)

varios = ['DANIELA <3', 25, True,22,23,frutas]
print('VARIOS:',varios)

nuevo_tema("funciones")

nuevo_tema('ciclos')
nuevo_subtema('for_1')

for numero in range(10):
    print(numero)

nuevo_subtema('for_2')
for numero in range(-3,10):
    print(numero)

nuevo_subtema('for_3')
for numero in range(-3,10,2):
    print(numero)

nuevo_subtema('for_4')
for indice, fruta in enumerate(frutas):
    print(indice+1,fruta)

nuevo_tema('listas_2')

frutas.append('piñas')
frutas.append('limones')
frutas.append('sandias')
print(frutas)

frutas.remove('manzanas')
print(frutas)

print('obteniendo el elemento 4:', frutas[4])

frutas.reverse()
print("frutas:",frutas)

frutas.sort()
print("frutas:",frutas)

nuevo_subtema("if-else")

numero_2=8;

if numero_2>6:
    print("numero 2 es mayor a 6")
else:
    print("numero 2 no es mayor a 6")

if frutas:
    print("algo sucedio")

if temperatura:
    print("en temperatura hay algo")

edad=0
if edad:
    print("edad es diferente de cero")
else:
    print("edad es igual a cero")

if []:
    print("lalista contiene algo")
else:
    print("la lista es vacia")

nuevo_subtema("ejemplo factorial")

fac=15
resultado=1
for num in range(fac):
  aux= fac - num
  resultado= resultado * aux
print(resultado)

nuevo_tema("diccionarios")

carro = {}
print("carro:",carro)

carro = {
    "marca" : "volskwagwen",
    "año": 2024,
    "color": "gris",
    "cilindraje":4,
    "llanta de respuesto": True
}
print("carro:",carro)
print("obteniendo hn elemento :", carro.get("marca"))
print("obteniendo hn elemento :", carro.get("puerta"))

print("obteniendo hn elemento :", carro["marca"])
#print("obteniendo hn elemento :", carro["puertas"])

print("carro.items()):",carro.items())
print("carro.values()):",carro.values())
print("carro.key()):",carro.keys())

for key, value in carro.items():
    print(F"{key} - {value}") 

carro.update({"color": "rojo"})
print("carro:" , carro)

carro.clear()
print("carro:",carro)

