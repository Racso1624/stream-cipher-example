# Oscar Fernando López Barrios
# Carné 20679
# Ejercicio de Stream Cipher
# Cifrado

from functions import *

def decryption(encrypted_text, key):
    binary_encrypted_text = text_to_bits(encrypted_text)
    binary_key = text_to_bits(key)

    decrypted_binary = ""

    for a, b in zip(binary_encrypted_text, binary_key):
        decrypted_binary += xor(a, b)

    decrypted_result = bits_to_text(decrypted_binary)

    return decrypted_result
