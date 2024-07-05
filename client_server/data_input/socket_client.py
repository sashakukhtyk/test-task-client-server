import socket
from cryptography.fernet import Fernet
from .key_generator import encrypt_data


def send_data(data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 65432))
        encrypted_data = encrypt_data(data)
        s.sendall(encrypted_data)
        print('Data sent successfully')