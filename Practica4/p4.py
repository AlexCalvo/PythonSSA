from Crypto.Hash import SHA512
from Crypto.Hash import SHA3_256
from Crypto.Hash import HMAC

#Ejercicio1
print('EJERCICIO A')
f = open("p4ssa.txt","rb")
linea = f.readline()
hash_object = SHA512.new()
while linea != b"":
    hash_object.update(linea)
    linea = f.readline()
    
print(hash_object.hexdigest())
f.close()

#Ejercicio2
print('EJERCICIO B')
f2 = open('p4ssa.txt','rb')
h = HMAC.new(b'S3cr3tK3y',digestmod=SHA512)
linea = f2.readline()
while linea != b"":
    h.update(linea)
    linea = f2.readline()

print(h.hexdigest())
f2.close()

try:
    h.hexverify(h.hexdigest())
except ValueError:
    print("El fichero no es valido")
finally:
    print("El fichero es valido")

#Ejercicio3
print('EJERCICIO C')
f3 = open('p4ssa.docx','rb')
linea = f3.read(4096)
h2 = SHA3_256.new()
while linea != b"":
    h2.update(linea)
    linea = f3.read(4096)
print(h2.hexdigest())
f3.close()

