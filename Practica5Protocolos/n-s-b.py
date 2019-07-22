from Crypto.Cipher import PKCS1_OAEP, DES, AES
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256, HMAC
from Crypto.Signature import pss
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes
import base64
import json
from socket_class import SOCKET_SIMPLE_TCP


key_a_t = b'0123456789ABCDEF'
key_b_t = b'FEDCBA9876543210'
BLOCK_SIZE_AES = 16

print("Creando socket y escuchando...")
socket = SOCKET_SIMPLE_TCP('127.0.0.1', 5556)
socket.escuchar()

#Recibe datos
datos = socket.recibir()
datos_hex = datos.hex()
print("A -> B: " + datos_hex)

#Se descifra la clave K_AB
decipher_aes_a_b = AES.new(key_b_t, AES.MODE_ECB)
json_a_b = unpad(decipher_aes_a_b.decrypt(datos), BLOCK_SIZE_AES)
print("A->B (Clear): " + json_a_b.hex())
K_AB = json_a_b

#Se genera el valor Rb
b_random = get_random_bytes(8)
print("Rb: " + b_random.hex())

#Cifra el valor Rb y se envia a Alice usando K_AB
cipher_aes_b_a = AES.new(K_AB, AES.MODE_ECB)
cipher_text_b_a = cipher_aes_b_a.encrypt(pad(b_random, BLOCK_SIZE_AES))
socket.enviar(cipher_text_b_a)

#Recibe E_AB(Rb-1)
b_random1 = socket.recibir()
decipher_aes_a_b1 = AES.new(K_AB, AES.MODE_ECB)
decipher_aes_random_b1 = unpad(decipher_aes_a_b1.decrypt(b_random1), BLOCK_SIZE_AES) 
b_random1 =  decipher_aes_random_b1.decode("utf-8", "ignore")
print("A->B:: Rb-1: " + b_random1)


#Intercambio de datos
nombre = "Guillermo Velasco Amo"
cipher_aes_nombre = AES.new(K_AB, AES.MODE_ECB)
cipher_aes_nombre_text = cipher_aes_nombre.encrypt(pad(nombre.encode("utf-8"), BLOCK_SIZE_AES))
socket.enviar(cipher_aes_nombre_text)

#Cerrar 
socket.cerrar()
