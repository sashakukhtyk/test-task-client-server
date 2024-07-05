from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

def encrypt_data(data):
    return cipher_suite.encrypt(data.encode('utf-8'))


def decrypt_data(encrypted_data):
    return cipher_suite.decrypt(encrypted_data).decode('utf-8')