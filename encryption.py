from functions import *

def encryption(text, key):
    binary_text = text_to_bits(text)
    binary_key = text_to_bits(key)

    binary_encryption = ""

    for a, b in zip(binary_text, binary_key):
        binary_encryption += xor(a, b)

    encrypted_result = bits_to_text(binary_encryption)

    return encrypted_result