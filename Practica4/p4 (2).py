from Crypto.Hash import SHA512
from Crypto.Hash import HMAC
from Crypto.Hash import SHA3_256
#Ejercicio A
print('EJERCICIO A')
fichero = open("nombre.txt", "rb")
linea = fichero.readline()
nombreHash = SHA512.new()
while linea != b"":
    nombreHash.update(linea)
    linea = fichero.readline()

print(nombreHash.hexdigest())
fichero.close()

print("----------------------------------------------------------------------------")

#Ejercicio B
print("EJERCICIO B")
ficheroB = open('nombre.txt','rb')
h = HMAC.new(b'S3cr3tK3y', digestmod=SHA512)

linea = ficheroB.readline()
while linea != b"":
    h.update(linea)
    linea = ficheroB.readline()

print(h.hexdigest())

try:
    h.hexverify(h.hexdigest())
except ValueError:
    print("FICHERO NO VALIDO")
finally:
    print("FICHERO VALIDO")

print("----------------------------------------------------------------------------")

ficheroB.close()

#EJERCICIO C
print("EJERCICIO C")
ficheroC = open("nombre.docx", "rb")

linea = ficheroC.read(4096)
hashC = SHA3_256.new()
while linea != b"":
    hashC.update(linea)
    linea = ficheroC.read(4096)

print(hashC.hexdigest())

ficheroC.close()