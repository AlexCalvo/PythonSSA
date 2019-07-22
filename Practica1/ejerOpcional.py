def cifradoMonoalfabetico(texto,clave):

    # Definir la nueva cadena resultado
    texto = input("Introduce un texto en claro para realizar cifrado: ")
    clave = input("Introduce clave para realizar cifrado: ")
    resultado = ''
    i = 0
    
    while i < len(texto):
        # Recoge el caracter a cifrar
        ordenClaro = ord(texto[i])
        ordenClave = ord(clave[i])
        ordenCifrado = 0
        # Cambia el caracter a cifrar
        ordenCifrado = (ordenClaro % 26) + (ordenClave % (len(clave)))
        # Añade el caracter cifrado al resultado
        resultado = resultado + chr(ordenCifrado)
        i = i + 1
    # devuelve el resultado
    return resultado