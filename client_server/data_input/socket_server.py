import socket
import psycopg2
from cryptography.fernet import Fernet

HOST = 'localhost'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

# Encryption key (this should be the same in client and server, and kept secret)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

conn = psycopg2.connect(dbname='test_client', user='postgres', password='1234', host='localhost')
cursor = conn.cursor()

def decrypt_data(encrypted_data):
    return cipher_suite.decrypt(encrypted_data).decode('utf-8')

def insert_into_db(data):
    cursor.execute("INSERT INTO myapp_item (data) VALUES (%s)", (data,))
    conn.commit()

# HOST = socket.gethostbyname(socket.gethostname())
def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        
        while True:
            conn, addr = s.accept()
            print('Connected by', addr)
            data = conn.recv(1024)
            if not data:
                break
            decrypted_data = decrypt_data(data)
            insert_into_db(decrypted_data)

start_server()