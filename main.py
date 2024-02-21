from keystream_generator import *
from encryption import *

word = "Hola mundo"
key = keystream_generator(len(word))
encrypted = encryption(word, key)

print(encrypted)