def cifradoCesarAlfabetoInglesMAYandMINUS(cadena):
    """Devuelve un cifrado Cesar generalizado (+i)"""


    # Definir la nueva cadena resultado
    des = int(input("Introduce un numero para realizar cifrado: "))
    resultado = ''
    # Realizar el "cifrado", sabiendo que A = 65, Z = 90, a = 97, z = 122
    i = 0
    
    while i < len(cadena):
        # Recoge el caracter a cifrar
        ordenClaro = ord(cadena[i])
        ordenCifrado = 0
        # Cambia el caracter a cifrar
        if (ordenClaro >= 65 and ordenClaro <= 90):
            ordenCifrado = (((ordenClaro - 65) +des) % 26) + 65
        elif (ordenClaro >= 97 and ordenClaro <= 122):
            ordenCifrado = (((ordenClaro - 97) +des) % 26) + 97
        # Añade el caracter cifrado al resultado
        resultado = resultado + chr(ordenCifrado)
        i = i + 1
    # devuelve el resultado
    return resultado

claroCESAR = 'VENI VIDI VINCI ZETA'
print(claroCESAR)
cifradoCESAR = cifradoCesarAlfabetoInglesMAYandMINUS(claroCESAR) 
print(cifradoCESAR)

claroCESAR = 'veni vidi vinci zeta'
print(claroCESAR)
cifradoCESAR = cifradoCesarAlfabetoInglesMAYandMINUS(claroCESAR) 
print(cifradoCESAR)


def desCifradoCesarAlfabetoInglesMAYandMINUS(cadena):
    """Devuelve un cifrado Cesar tradicional (+3)"""
    # Definir la nueva cadena resultado
    resultado = ''
    des = int(input("Introduce un numero para realizar el descrifrado:"))
    # Realizar el "cifrado", sabiendo que A = 65, Z = 90, a = 97, z = 122
    i = 0
    while i < len(cadena):
        # Recoge el caracter a cifrar
        ordenClaro = ord(cadena[i])
        ordenCifrado = 0
        # Cambia el caracter a cifrar
        if (ordenClaro >= 65 and ordenClaro <= 90):
            ordenCifrado = (((ordenClaro - 65) -3) % 26) + 65
        elif (ordenClaro >= 97 and ordenClaro <= 122):
            ordenCifrado = (((ordenClaro - 97) -3) % 26) + 97
        # Añade el caracter cifrado al resultado
        resultado = resultado + chr(ordenCifrado)
        i = i + 1
    # devuelve el resultado
    return resultado

claroCESAR = 'VENI VIDI VINCI ZETA'
print(claroCESAR)
cifradoCESAR = desCifradoCesarAlfabetoInglesMAYandMINUS(claroCESAR) 
print(cifradoCESAR)

claroCESAR = 'veni vidi vinci zeta'
print(claroCESAR)
cifradoCESAR = desCifradoCesarAlfabetoInglesMAYandMINUS(claroCESAR) 
print(cifradoCESAR)