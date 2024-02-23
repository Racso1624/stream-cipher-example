from keystream_generator import *
from encryption import *
from decryption import *

word = "Hola mundo"
word_2 = "Saludos JP"
key = keystream_generator(len(word))
encrypted = encryption(word, key)
decrypted = decryption(encrypted, key)

encrypted_2 = encryption(word_2, key)
decrypted_2 = decryption(encrypted_2, key)

print("Texto encriptado: ", encrypted)
print("Texto desencriptado: ", decrypted)

print("Texto encriptado 2: ", encrypted_2)
print("Texto desencriptado 2: ", decrypted_2)