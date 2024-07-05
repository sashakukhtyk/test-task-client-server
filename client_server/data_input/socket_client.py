import socket
from cryptography.fernet import Fernet


# Load the key from the file
with open('secret.key', 'rb') as key_file:
    key = key_file.read()

cipher_suite = Fernet(key)


def encrypt_data(data):
    return cipher_suite.encrypt(data.encode('utf-8'))


def send_data(data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 65432))
        encrypted_data = encrypt_data(data)
        s.sendall(encrypted_data)
        print('Data sent successfully')