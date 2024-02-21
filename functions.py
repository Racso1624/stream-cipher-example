def xor(a, b):
    a_bool = bool(int(a))
    b_bool = bool(int(b))
    result = int((a_bool or b_bool) and not (a_bool and b_bool))
    return str(result)

def text_to_bits(text):

    result_bits = ""
    for letter in text:
        bits = bin(ord(letter))[2:].zfill(8)
        result_bits += bits
    return result_bits

def bits_to_text(bits):

    result_text = ""
    for i in range(0, len(bits), 8):
        bit_group = bits[i:i+8]
        value = int(bit_group, 2)
        result_text += chr(value)
    return result_text