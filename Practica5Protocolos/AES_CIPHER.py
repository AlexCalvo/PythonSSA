from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Util import Counter
import base64

class AES_CIPHER:
    
    BLOCK_SIZE_AES = 16 # AES: Bloque de 64 bits
    
    def __init__(self, key):
 #Inicializa las variables locales
        self.k = key

    def cifrarCBC(self, cadena, IV):
 #Cifra el parámetro cadena (de tipo String) con una IV específica, y devuelve el texto cifrado binario
        cadena = cadena.encode("utf-8")
        cipher = AES.new(self.k, AES.MODE_CBC, IV)
        ciphertext = cipher.encrypt(pad(cadena,self.BLOCK_SIZE_AES))
        return ciphertext
 
    def descifrarCBC(self, cifrado, IV):
 #Descrifra el parámetro cifrado (de tipo binario) con una IV específica, y  devuelve la cadena en claro de tipo String
        decipher_AES = AES.new(self.k, AES.MODE_CBC, IV)
        new_data = unpad(decipher_AES.decrypt(cifrado), self.BLOCK_SIZE_AES)
        new_data = new_data.decode("utf-8", "ignore")

        return new_data

    def cifrarECB(self, cadena):
        cadena = cadena.encode("utf-8")
        cipher = AES.new(self.k, AES.MODE_ECB)
        ciphertext = cipher.encrypt(pad(cadena, self.BLOCK_SIZE_AES))

        return ciphertext

    def descifrarECB(self, cifrado):
        decipher_AES = AES.new(self.k, AES.MODE_ECB)
        new_data = unpad(decipher_AES.decrypt(cifrado), self.BLOCK_SIZE_AES)
        new_data = new_data.decode("utf-8", "ignore")

        return new_data

    def cifrarCTR(self, cadena, ctr):
        cadena = cadena.encode("utf-8")
        cipher = AES.new(self.k, AES.MODE_CTR, counter=ctr)
        ciphertext = cipher.encrypt(cadena)

        return ciphertext

    def descifrarCTR(self, cifrado, ctr):
        decipher_AES = AES.new(self.k, AES.MODE_CTR, counter=ctr)
        new_data = decipher_AES.decrypt(cifrado)
        new_data = new_data.decode("utf-8", "ignore")

        return new_data




key = get_random_bytes(16) # Clave aleatoria de 64 bits
IV = get_random_bytes(16) # IV aleatorio de 64 bits
datos = "Hola Mundo con AES en modo CBC"
d = AES_CIPHER(key)
cifrado = d.cifrarCBC(datos, IV)
AEScifrado = d.AEScifrarCBC(cifrado, IV)
print(cifrado)
print(AEScifrado)

ndatos = "Hola Mundo con AES en modo ECB"
cifrado = d.cifrarECB(ndatos)
AEScifrado = d.AEScifrarECB(cifrado)
print(cifrado)
print(AEScifrado)

ndatos = "Hola Mundo con AES en modo CTR"
cont = Counter.new(128)
cifrado = d.cifrarCTR(ndatos, cont)
AEScifrado = d.AEScifrarCTR(cifrado, cont)
print(cifrado)
print(AEScifrado)