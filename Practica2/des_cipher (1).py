from Crypto.Random import get_random_bytes
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad,unpad
from Crypto.Util import Counter
import base64

class DES_CIPHER:
    
    BLOCK_SIZE_DES = 8 # DES: Bloque de 64 bits
    
    def __init__(self, key):
 #"""Inicializa las variables locales"""
        self.k = key

    def cifrarCBC(self, cadena, IV):
 #"""Cifra el parámetro cadena (de tipo String) con una IV específica, y devuelve el texto cifrado binario"""

        cadena = cadena.encode("utf-8")
        cipher = DES.new(self.k, DES.MODE_CBC, IV)
        ciphertext = cipher.encrypt(pad(cadena,self.BLOCK_SIZE_DES))
        

        return ciphertext
 
    def descifrarCBC(self, cifrado, IV):
 #"""Descrifra el parámetro cifrado (de tipo binario) con una IV específica, y  devuelve la cadena en claro de tipo String"""

        decipher_des = DES.new(self.k, DES.MODE_CBC, IV)
        new_data = unpad(decipher_des.decrypt(cifrado), self.BLOCK_SIZE_DES)
        new_data = new_data.decode("utf-8", "ignore")

        return new_data


    def cifrarECB(self, cadena):

        cadena = cadena.encode("utf-8")
        cipher = DES.new(self.k, DES.MODE_ECB)
        ciphertext = cipher.encrypt(pad(cadena, self.BLOCK_SIZE_DES))

        return ciphertext

    def descifrarECB(self, cifrado):

        decipher_des = DES.new(self.k, DES.MODE_ECB)
        new_data = unpad(decipher_des.decrypt(cifrado), self.BLOCK_SIZE_DES)
        new_data = new_data.decode("utf-8", "ignore")

        return new_data

    def cifrarCTR(self, cadena, ctr):

        cadena = cadena.encode("utf-8")
        cipher = DES.new(self.k, DES.MODE_CTR, counter=ctr)
        ciphertext = cipher.encrypt(cadena)

        return ciphertext

    def descifrarCTR(self, cifrado, ctr):

        decipher_des = DES.new(self.k, DES.MODE_CTR, counter=ctr)
        new_data = decipher_des.decrypt(cifrado)
        new_data = new_data.decode("utf-8", "ignore")

        return new_data




key = get_random_bytes(8) # Clave aleatoria de 64 bits
IV = get_random_bytes(8) # IV aleatorio de 64 bits
datos = "Hola Mundo con DES en modo CBC"
d = DES_CIPHER(key)
cifrado = d.cifrarCBC(datos, IV)
descifrado = d.descifrarCBC(cifrado, IV)
print(cifrado)
print(descifrado)

ndatos = "Hola Mundo con DES en modo ECB"
cifrado = d.cifrarECB(ndatos)
descifrado = d.descifrarECB(cifrado)
print(cifrado)
print(descifrado)

ndatos = "Hola Mundo con DES en modo CTR"
cont = Counter.new(64)
cifrado = d.cifrarCTR(ndatos, cont)
descifrado = d.descifrarCTR(cifrado, cont)
print(cifrado)
print(descifrado)