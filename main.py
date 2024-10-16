from os import system 
system("cls")
from funciones import *
'''
Una empresa se dedica al almacenamiento y posterior distribución de juguetes en el interior
del país. Para ello cuentan con 5 depósitos distribuidos en diferentes provincias (PBA,
CABA, Chubut, Tucumán y Mendoza).
Los depósitos pueden almacenar 6 tipos diferentes de juguetes: autos, muñecas, trenes,
peluches, spinners y cartas.
La oficina central, recibe mensualmente una planilla de existencias donde se indican las
existencias de cada juguete para cada depósito.
Realizar un menú de opciones:
1. Obtener existencias: para ello deberá cargar en el main la existencia de cada juguete
en todos los depósitos. En una lista de cantidad, no uno por uno. Por lo que habrá una
matriz con 3 columnas o filas, provincia, tipo de juguete y cantidad.
2. Calcular por cada depósito la cantidad total de juguetes almacenados entre todos los
tipos.
3. Obtener los nombres de los juguetes que es necesario reponer en cada depósito.
Crear una función que devuelva todos los juguetes con menos de 500 unidades.
4. Máxima cantidad de juguetes almacenados de cada tipo. Devolver en qué provincia se
encuentran.
5. Depósito con mayor recaudación, teniendo en cuenta que disponemos de un vector
con los valores por unidad de cada juguete. Esto se debe hacer con una función que
reciba la lista de precios por parámetro para poder actualizarlos frente a la inflación.
6. Cantidad de depósitos que hayan almacenado más de 50.000 unidades entre los 6
juguetes. Mostrar provincias.
7. Porcentaje de juguetes de cada tipo sobre el total de juguetes almacenados. Realizar
una función que muestre el porcentaje de cada uno.
8. Generar un informe con la recaudación de cada depósito, ordenada de mayor a menor
usando insertion sort o quick sort. Justificar la elección del algoritmo. Para ello la
función deberá recibir una matriz de ventas, y una lista de precios.
9. Generar una función que permita corregir un error de carga mediante carga aleatoria o
distribuida de matrices.'''

menu1=\
'''
1. Obtener existencias
2. Calcular por cada depósito la cantidad total de juguetes almacenados entre todos lostipos.
3. Obtener los nombres de los juguetes que es necesario reponer en cada depósito.
4. Máxima cantidad de juguetes almacenados de cada tipo
5. Depósito con mayor recaudación
6. Cantidad de depósitos que hayan almacenado más de 50.000 unidades entre los 6 juguetes
7. Porcentaje de juguetes de cada tipo sobre el total de juguetes almacenados
8. Generar un informe con la recaudación de cada depósito
9. Generar una función que permita corregir un error de carga mediante carga aleatoria o distribuida de matrices.
10. salir 
eliga una opcion: '''
carga=[["pba","autos" , 50000],["pba","muñecas" , 100],["caba","autos" , 50000]]
existencia = []
res = True
indice = 0
while res == True:
    menu = input(menu1)
    while menu != "1" and menu != "2" and menu != "3" and menu != "4" and menu != "5" and menu != "6" and menu != "7" and menu != "8" and menu != "9" and menu != "10":
        menu = input(f"error ingrese un numero valido:\n {menu1}")

    match menu:
        case "1":
            carga, indice = obtener_existencias(existencia, indice)
            print(carga)
        case "2":
            if carga == [] :
                print("\ningrese los objetos con la opcion 1")
            else:
                print(calcular_por_deposito(carga,menu))
        case "3":
            if carga == [] :
                print("\ningrese los objetos con la opcion 1")
            else:
                print(calcular_por_deposito(carga,menu))
        case "4":
            if carga == [] :
                print("\ningrese los objetos con la opcion 1")
            else:
                print(calcular_por_deposito(carga,menu))
        case "5":
            if carga == [] :
                print("\ningrese los objetos con la opcion 1")
            else:
                print(calcular_por_deposito(carga,menu))
        case "6":
            if carga == [] :
                print("\ningrese los objetos con la opcion 1")
            else:
                print(calcular_por_deposito(carga,menu))
        case "7":
            pass
        case "8":
            if carga == [] :
                print("\ningrese los objetos con la opcion 1")
            else:
                print(calcular_por_deposito(carga,menu))
        case "9":
            pass
        case "10":
            res = False

