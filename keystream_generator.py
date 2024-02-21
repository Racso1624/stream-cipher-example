import string
import secrets

def keystream_generator(key_length):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for i in range(key_length))