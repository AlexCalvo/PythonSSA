from Crypto.Random import get_random_bytes
from Crypto.Cipher import DES, AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Util import Counter
import base64

class AES_CIPHER:

 

 def __init__(self, key):
     self.key=key #Inicializa las variables locales
 
 
 def cifrar(self, cadena, IV, block):
    #Cifra el parámetro cadena (de tipo String) con una IV específica, y devuelve el texto cifrado binario"""
    cipher = AES.new(self.key, AES.MODE_ECB, IV)
    self.data=cadena.encode("utf-8")
    cypher = cipher.encrypt(pad(self.data,block))
    print(cypher)
    encoded_ciphertext = base64.b64encode(cypher)
    print(encoded_ciphertext)
    return cypher
 
 def descifrar(self, cifrado, IV, block):

     decipher_des = AES.new(self.key, AES.MODE_ECB, IV)
     new_data = unpad(decipher_des.decrypt(cifrado),block).decode("utf-8","ignore")
     print(new_data)
     return new_data


 
 # Descrifra el parámetro cifrado (de tipo binario) con una IV específica, y devuelve la cadena en claro de tipo String"""

key = get_random_bytes(16) # Clave aleatoria de 128 bits
IV = get_random_bytes(16) # IV aleatorio de 128 bits
BLOCK_SIZE_AES = 16 # Bloque de 128 bits
datos = "Hola Mundo con AES en modo CBC"
print(datos)
d = AES_CIPHER(key)
print("Cifrar con AES ->")
cifrado = d.cifrar(datos, IV,BLOCK_SIZE_AES)
print("Descifrar con AES ->")
descifrado = d.descifrar(cifrado, IV,BLOCK_SIZE_AES)