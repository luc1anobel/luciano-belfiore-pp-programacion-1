from os import system 
system("cls")
'''1. Obtener existencias: para ello deberá cargar en el main la existencia de cada juguete
en todos los depósitos. En una lista de cantidad, no uno por uno. Por lo que habrá una
matriz con 3 columnas o filas, provincia, tipo de juguete y cantidad.PBA,
CABA, Chubut, Tucumán y Mendoza   autos, muñecas, trenes, peluches, spinners y cartas.'''

def obtener_existencias (existencia,indice):
    provincia=""
    continuar = "si"
    while continuar == "si":
        provincia = input("ingrese la provincia (pba,caba, chubut, tucuman y mendoza)\n eliga la opcion: ")
        while provincia != "pba" and provincia != "caba" and provincia != "chubut" and provincia != "tucuman" and provincia != "mendoza":
            provincia = input("error, ingrese una provincia valida (pba,caba, chubut, tucuman y mendoza)\n eliga la opcion: ")
        tipo_de_juguetes = input("ingrese el tipo de juguete(autos, muñecas, trenes, peluches, spinners, cartas)\neliga la opcion:  ")
        while tipo_de_juguetes != "autos" and tipo_de_juguetes != "muñecas" and tipo_de_juguetes != "trenes" and tipo_de_juguetes != "peluches" and tipo_de_juguetes != "spinners" and tipo_de_juguetes != "cartas":
            tipo_de_juguetes = input("error, ingrese un juguete valido valida (autos, muñecas, trenes, peluches, spinners, cartas)\n eliga la opcion: ")
        cantidad = int(input ("ingrese la cantidad: "))

        if indice == len(existencia):
            existencia += [["","",0]]

        
        existencia[indice][0] += provincia
        existencia[indice][1] += tipo_de_juguetes
        existencia[indice][2] += cantidad


        indice  +=1

        continuar = input("quiere agregar mas(si-no): ")
    return existencia , indice 
#2_Calcular por cada depósito la cantidad total de juguetes almacenados entre todos los tipos.
def calcular_por_deposito (existencia,menu):
    pba_acumulador = 0
    caba_acumulador = 0
    chubut_acumulador = 0 
    tucuman_acumulador = 0
    mendoza_acumulador = 0
    pba_acumulador_autos = 0
    pba_acumulador_muñecas = 0
    pba_acumulador_trenes = 0
    pba_acumulador_peluches = 0
    pba_acumulador_spinners = 0
    pba_acumulador_cartas = 0
    caba_acumulador_autos = 0
    caba_acumulador_muñecas = 0
    caba_acumulador_trenes = 0
    caba_acumulador_peluches = 0
    caba_acumulador_spinners = 0
    caba_acumulador_cartas = 0
    chubut_acumulador_autos = 0
    chubut_acumulador_muñecas = 0
    chubut_acumulador_trenes = 0
    chubut_acumulador_peluches = 0
    chubut_acumulador_spinners = 0
    chubut_acumulador_cartas = 0
    tucuman_acumulador_autos = 0
    tucuman_acumulador_muñecas = 0
    tucuman_acumulador_trenes = 0
    tucuman_acumulador_peluches = 0
    tucuman_acumulador_spinners = 0
    tucuman_acumulador_cartas = 0
    mendoza_acumulador_autos = 0
    mendoza_acumulador_muñecas = 0
    mendoza_acumulador_trenes = 0
    mendoza_acumulador_peluches = 0
    mendoza_acumulador_spinners = 0
    mendoza_acumulador_cartas = 0
    for i in existencia:

        match i[0]:
            case "pba":
                pba_acumulador += i[2]
                match i[1]:
                    case "autos":
                        pba_acumulador_autos += i[2]
                    case "muñecas":
                        pba_acumulador_muñecas += i[2]
                    case "trenes":
                        pba_acumulador_trenes += i[2]
                    case "peluches":
                        pba_acumulador_peluches += i[2]
                    case "spinners":
                        pba_acumulador_spinners += i[2]
                    case "cartas":
                        pba_acumulador_cartas += i[2]
            case "caba":
                caba_acumulador += i[2]
                match i[1]:
                    case "autos":
                        caba_acumulador_autos += i[2]
                    case "muñecas":
                        caba_acumulador_muñecas += i[2]
                    case "trenes":
                        caba_acumulador_trenes += i[2]
                    case "peluches":
                        caba_acumulador_peluches += i[2]
                    case "spinners":
                        caba_acumulador_spinners += i[2]
                    case "cartas":
                        caba_acumulador_cartas += i[2]
            case "chubut":
                chubut_acumulador += i[2]
                match i[1]:
                    case "autos":
                        chubut_acumulador_autos += i[2]
                    case "muñecas":
                        chubut_acumulador_muñecas += i[2]
                    case "trenes":
                        chubut_acumulador_trenes += i[2]
                    case "peluches":
                        chubut_acumulador_peluches += i[2]
                    case "spinners":
                        chubut_acumulador_spinners += i[2]
                    case "cartas":
                        chubut_acumulador_cartas += i[2]
            case "tucuman":
                tucuman_acumulador += i[2]
                match i[1]:
                    case "autos":
                        tucuman_acumulador_autos += i[2]
                    case "muñecas":
                        tucuman_acumulador_muñecas += i[2]
                    case "trenes":
                        tucuman_acumulador_trenes += i[2]
                    case "peluches":
                        tucuman_acumulador_peluches += i[2]
                    case "spinners":
                        tucuman_acumulador_spinners += i[2]
                    case "cartas":
                        tucuman_acumulador_cartas += i[2]
            case "mendoza":
                mendoza_acumulador += i[2]  
                match i[1]:
                    case "autos":
                        mendoza_acumulador_autos += i[2]
                    case "muñecas":
                        mendoza_acumulador_muñecas += i[2]
                    case "trenes":
                        mendoza_acumulador_trenes += i[2]
                    case "peluches":
                        mendoza_acumulador_peluches += i[2]
                    case "spinners":
                        mendoza_acumulador_spinners += i[2]
                    case "cartas":
                        mendoza_acumulador_cartas += i[2]
        
    match menu:
        case "2":    
            respuesta=\
            f'''
            el total del depisoto de pba es = {pba_acumulador}
            el total del depisoto de caba es = {caba_acumulador}
            el total del depisoto de chubut es = {chubut_acumulador}
            el total del depisoto de tucuman es = {tucuman_acumulador}
            el total del depisoto de mendoza es = {mendoza_acumulador}
            '''
        case "3":
            respuesta=\
            f'''
            pba:
            el deposito de autos de pba {reponer_juguetes(pba_acumulador_autos)}
            el deposito de muñecas de pba {reponer_juguetes(pba_acumulador_muñecas)}
            el deposito de trenes de pba {reponer_juguetes(pba_acumulador_trenes)}
            el deposito de peluches de pba {reponer_juguetes(pba_acumulador_peluches)}
            el deposito de spinners de pba {reponer_juguetes(pba_acumulador_spinners)}
            el deposito de cartas de pba {reponer_juguetes(pba_acumulador_cartas)}
            caba:
            el deposito de autos de caba {reponer_juguetes(caba_acumulador_autos)}
            el deposito de muñecas de caba {reponer_juguetes(caba_acumulador_muñecas)}
            el deposito de trenes de caba {reponer_juguetes(caba_acumulador_trenes)}
            el deposito de peluches de caba {reponer_juguetes(caba_acumulador_peluches)}
            el deposito de spinners de caba {reponer_juguetes(caba_acumulador_spinners)}
            el deposito de cartas de caba {reponer_juguetes(caba_acumulador_cartas)}
            chubut:
            el deposito de autos de chubut {reponer_juguetes(chubut_acumulador_autos)}
            el deposito de muñecas de chubut {reponer_juguetes(chubut_acumulador_muñecas)}
            el deposito de trenes de chubut {reponer_juguetes(chubut_acumulador_trenes)}
            el deposito de peluches de chubut {reponer_juguetes(chubut_acumulador_peluches)}
            el deposito de spinners de chubut {reponer_juguetes(chubut_acumulador_spinners)}
            el deposito de cartas de chubut {reponer_juguetes(chubut_acumulador_cartas)}
            tucuman:
            el deposito de autos de tucuman {reponer_juguetes(tucuman_acumulador_autos)}
            el deposito de muñecas de tucuman {reponer_juguetes(tucuman_acumulador_muñecas)}
            el deposito de trenes de tucuman {reponer_juguetes(tucuman_acumulador_trenes)}
            el deposito de peluches de tucuman {reponer_juguetes(tucuman_acumulador_peluches)}
            el deposito de spinners de tucuman {reponer_juguetes(tucuman_acumulador_spinners)}
            el deposito de cartas de tucuman {reponer_juguetes(tucuman_acumulador_cartas)}
            mendoza:
            el deposito de autos de mendoza {reponer_juguetes(mendoza_acumulador_autos)}
            el deposito de muñecas de mendoza {reponer_juguetes(mendoza_acumulador_muñecas)}
            el deposito de trenes de mendoza {reponer_juguetes(mendoza_acumulador_trenes)}
            el deposito de peluches de mendoza {reponer_juguetes(mendoza_acumulador_peluches)}
            el deposito de spinners de mendoza {reponer_juguetes(mendoza_acumulador_spinners)}
            el deposito de cartas de mendoza {reponer_juguetes(mendoza_acumulador_cartas)}
            '''
        case "4":
            respuesta=\
            f'''
            {comparar(pba_acumulador_autos,caba_acumulador_autos,chubut_acumulador_autos,tucuman_acumulador_autos,mendoza_acumulador_autos)}autos
            {comparar(pba_acumulador_muñecas,caba_acumulador_muñecas,chubut_acumulador_muñecas,tucuman_acumulador_muñecas,mendoza_acumulador_muñecas)}muñecas
            {comparar(pba_acumulador_trenes,caba_acumulador_trenes,chubut_acumulador_trenes,tucuman_acumulador_trenes,mendoza_acumulador_trenes)}trenes
            {comparar(pba_acumulador_peluches,caba_acumulador_peluches,chubut_acumulador_peluches,tucuman_acumulador_peluches,mendoza_acumulador_peluches)}peluches
            {comparar(pba_acumulador_spinners,caba_acumulador_spinners,chubut_acumulador_spinners,tucuman_acumulador_spinners,mendoza_acumulador_spinners)}spinners
            {comparar(pba_acumulador_cartas,caba_acumulador_cartas,chubut_acumulador_cartas,tucuman_acumulador_cartas,mendoza_acumulador_cartas)}cartas
            '''
        case "5":
            precios_autos,precios_muñecas,precios_trenes,precios_peluches,precios_spinners,precios_cartas = pedida_de_precios()

            recaudacion_pba = (pba_acumulador_autos*precios_autos)+(pba_acumulador_muñecas*precios_muñecas)+(pba_acumulador_trenes*precios_trenes)+(pba_acumulador_peluches*precios_peluches)+(pba_acumulador_spinners*precios_spinners)+(pba_acumulador_cartas*precios_cartas)
            recaudacion_caba = (caba_acumulador_autos*precios_autos)+(caba_acumulador_muñecas*precios_muñecas)+(caba_acumulador_trenes*precios_trenes)+(caba_acumulador_peluches*precios_peluches)+(caba_acumulador_spinners*precios_spinners)+(caba_acumulador_cartas*precios_cartas)
            recaudacion_chubut = (chubut_acumulador_autos*precios_autos)+(chubut_acumulador_muñecas*precios_muñecas)+(chubut_acumulador_trenes*precios_trenes)+(chubut_acumulador_peluches*precios_peluches)+(chubut_acumulador_spinners*precios_spinners)+(chubut_acumulador_cartas*precios_cartas)
            recaudacion_tucuman = (tucuman_acumulador_autos*precios_autos)+(tucuman_acumulador_muñecas*precios_muñecas)+(tucuman_acumulador_trenes*precios_trenes)+(tucuman_acumulador_peluches*precios_peluches)+(tucuman_acumulador_spinners*precios_spinners)+(tucuman_acumulador_cartas*precios_cartas)
            recaudacion_mendoza = (mendoza_acumulador_autos*precios_autos)+(mendoza_acumulador_muñecas*precios_muñecas)+(mendoza_acumulador_trenes*precios_trenes)+(mendoza_acumulador_peluches*precios_peluches)+(mendoza_acumulador_spinners*precios_spinners)+(mendoza_acumulador_cartas*precios_cartas)

            respuesta = f"{comparar(recaudacion_pba,recaudacion_caba,recaudacion_chubut,recaudacion_tucuman,recaudacion_mendoza)}recaudacion"
        case "6":
            respuesta=\
            f''' 
            {mas_de_50000(pba_acumulador)}
            {mas_de_50000(caba_acumulador)}
            {mas_de_50000(chubut_acumulador)}
            {mas_de_50000(tucuman_acumulador)}
            {mas_de_50000(mendoza_acumulador)}
            '''
        case "8":
            precios_autos,precios_muñecas,precios_trenes,precios_peluches,precios_spinners,precios_cartas = pedida_de_precios()
            recaudacion_pba = (pba_acumulador_autos*precios_autos)+(pba_acumulador_muñecas*precios_muñecas)+(pba_acumulador_trenes*precios_trenes)+(pba_acumulador_peluches*precios_peluches)+(pba_acumulador_spinners*precios_spinners)+(pba_acumulador_cartas*precios_cartas)
            recaudacion_caba = (caba_acumulador_autos*precios_autos)+(caba_acumulador_muñecas*precios_muñecas)+(caba_acumulador_trenes*precios_trenes)+(caba_acumulador_peluches*precios_peluches)+(caba_acumulador_spinners*precios_spinners)+(caba_acumulador_cartas*precios_cartas)
            recaudacion_chubut = (chubut_acumulador_autos*precios_autos)+(chubut_acumulador_muñecas*precios_muñecas)+(chubut_acumulador_trenes*precios_trenes)+(chubut_acumulador_peluches*precios_peluches)+(chubut_acumulador_spinners*precios_spinners)+(chubut_acumulador_cartas*precios_cartas)
            recaudacion_tucuman = (tucuman_acumulador_autos*precios_autos)+(tucuman_acumulador_muñecas*precios_muñecas)+(tucuman_acumulador_trenes*precios_trenes)+(tucuman_acumulador_peluches*precios_peluches)+(tucuman_acumulador_spinners*precios_spinners)+(tucuman_acumulador_cartas*precios_cartas)
            recaudacion_mendoza = (mendoza_acumulador_autos*precios_autos)+(mendoza_acumulador_muñecas*precios_muñecas)+(mendoza_acumulador_trenes*precios_trenes)+(mendoza_acumulador_peluches*precios_peluches)+(mendoza_acumulador_spinners*precios_spinners)+(mendoza_acumulador_cartas*precios_cartas)
            respuesta =\
            f'''
            {recaudacion_pba}
            {recaudacion_caba}
            {recaudacion_chubut}
            {recaudacion_tucuman}
            {recaudacion_mendoza}
            '''
    return respuesta

#3. Obtener los nombres de los juguetes que es necesario reponer en cada depósito. Crear una función que devuelva todos los juguetes con menos de 500 unidades.
def reponer_juguetes (acumulador_exacto):
    
    if acumulador_exacto < 500:
        respuesta = "necesita mas juguetes"
    else:
        respuesta = "no le hace falta reponer"
        
    return respuesta
#4. Máxima cantidad de juguetes almacenados de cada tipo. Devolver en qué provincia se encuentran.
def comparar (pba,caba,chubut,tucuman,mendoza):

    if pba == caba and pba == chubut and pba == tucuman and pba == mendoza:
        respuesta = "las 5 provincias tienen la misma cantidad de:"
    else:
        if pba == caba and pba == chubut and pba == tucuman and pba > mendoza:
            respuesta = "todas las provincias excepto mendoza tienen la misma cantidad de:"
        elif pba == caba and pba == chubut and pba > tucuman and pba > mendoza:
            respuesta = "pba,caba,chubut tienen la misma cantidad de:"
        elif pba == caba and pba > chubut and pba > tucuman and pba > mendoza:
            respuesta = "pba y caba tienen la misma cantidad de:"
        elif pba > caba and pba > chubut and pba > tucuman and pba > mendoza: 
            respuesta = "pba tienen la mayor cantidad de:"
        elif caba == chubut and caba == tucuman and caba == mendoza:
            respuesta = "todas las provincias excepto pba tienen la misma cantidad de:"
        elif caba == chubut and caba == tucuman and caba > mendoza:
            respuesta = "caba,chubut,tucuman tienen la misma cantidad de:"
        elif caba == chubut and caba > tucuman and caba > mendoza:
            respuesta = "caba y chubut tienen la misma cantidad de:"
        elif caba > chubut and caba > tucuman and caba > mendoza:
            respuesta = "caba tienen la mayor cantidad de:"
        elif chubut == tucuman and chubut > mendoza:
            respuesta = "chubut y tucuman tienen la misma cantidad de:"
        elif chubut > tucuman and chubut > mendoza:
            respuesta = "chubut tienen la mayor cantidad de:"
        elif tucuman == mendoza:
            respuesta = "tucuman y mendoza tienen la misma cantidad de:"
        elif tucuman > mendoza:
            respuesta = "tucuman tienen la mayor cantidad de:"
        else:
            respuesta = "mendoza tienen la mayor cantidad de:"
    return respuesta

'''5_Depósito con mayor recaudación, teniendo en cuenta que disponemos de un vector
con los valores por unidad de cada juguete. Esto se debe hacer con una función que
reciba la lista de precios por parámetro para poder actualizarlos frente a la inflación.'''


def pedida_de_precios ():

    precios_autos = int(input("ingrese el precio de los autos: "))
    precios_muñecas = int(input("ingrese el precio de los muñecas: "))
    precios_trenes = int(input("ingrese el precio de los trenes: "))
    precios_peluches = int(input("ingrese el precio de los peluches: "))
    precios_spinners = int(input("ingrese el precio de los spinners: "))
    precios_cartas = int(input("ingrese el precio de los cartas: "))

    return precios_autos,precios_muñecas,precios_trenes,precios_peluches,precios_spinners,precios_cartas

def mas_de_50000 (total):

    if total >= 50000:
        if total == 50000:
            respuesta = "tiene exactamente 50,000"
        else:
            respuesta = f"tiene mas de 50,000 unidades exactamentes {total}"
    else:
        respuesta = f"tiene menos de 50,000 unidades exactamente {total}"
    return respuesta