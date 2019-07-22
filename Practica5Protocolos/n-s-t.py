from Crypto.Cipher import PKCS1_OAEP, DES, AES
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256, HMAC
from Crypto.Signature import pss
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes
import base64
import json
from socket_class import SOCKET_SIMPLE_TCP

# Parametros
key_a_t = b'0123456789ABCDEF'
key_b_t = b'FEDCBA9876543210'
BLOCK_SIZE_AES = 16

# Crea el socket servidor y escucha
print("Creando socket y escuchando...")
socket = SOCKET_SIMPLE_TCP('127.0.0.1', 5555)
socket.escuchar()

# A->T: Alice, Bob, Ra
datos = socket.recibir()
json_a_t = datos.decode("utf-8" ,"ignore")
print("A->T: " + json_a_t)
msg_a_t = json.loads(json_a_t)

# T: Guarda Alice, Bob, Ra
t_alice, t_bob, t_random = msg_a_t
t_random = bytearray.fromhex(t_random)

############################################################################
# COMPLETAR: CREAR K_AB, CREAR E_BT(K_AB, Alice), ENVIAR EL MENSAJE A ALICE 
############################################################################

# Creamos K_AB
K_AB = get_random_bytes(BLOCK_SIZE_AES)

# T: msg_t_a = Ra, Bob, K_AB, E_BT(K_AB, Alice)

datos = []
datos.append(K_AB.hex().encode("utf-8"))
datos.append("Alice".encode("utf-8"))
json_datos = json.dumps(datos)

cipher = AES.new(key_b_t,AES.MODE_ECB)
E_BT = cipher.encrypt(pad(json_datos.encode("utf-8"),BLOCK_SIZE_AES))

msg_t_a = []
msg_t_a.append(t_random.hex())
msg_t_a.append("Bob")
msg_t_a.append(K_AB.hex())

msg_t_a.append(E_BT.hex())

json_t_a = json.dumps(msg_t_a)




# T->A: E_AT(msg_t_a)
print("A->T: " + json_t_a)
socket.enviar(json_t_a.encode("utf-8"))

# Terminamos nuestra tarea, cerramos el socket
print("A->T terminado")
socket.cerrar()