from keystream_generator import *
from encryption import *
from decryption import *

word = "Hola mundo"
key = keystream_generator(len(word))
encrypted = encryption(word, key)
decrypted = decryption(encrypted, key)

print("Texto encriptado: ", encrypted)
print("Texto desencriptado: ", decrypted)