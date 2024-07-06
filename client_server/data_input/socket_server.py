import socket
import psycopg2
from cryptography.fernet import Fernet


HOST = "localhost"  # The server's hostname or IP address
PORT = 65432  # The port used by the server


# Load the key from the file
with open("secret.key", "rb") as key_file:
    key = key_file.read()

cipher_suite = Fernet(key)


conn = psycopg2.connect(
    dbname="test_client", user="postgres", password="1234", host="localhost"
)
cursor = conn.cursor()


def decrypt_data(encrypted_data):
    return cipher_suite.decrypt(encrypted_data).decode("utf-8")


def insert_into_db(data):
    cursor.execute("INSERT INTO data_input_item (data) VALUES (%s)", (data,))
    conn.commit()


# HOST = socket.gethostbyname(socket.gethostname())
def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server listening on {HOST}:{PORT}")

        try:
            while True:
                client_conn, addr = s.accept()
                print("Connected by", addr)
                data = client_conn.recv(1024)
                if not data:
                    print("No data received.")
                    break
                try:
                    decrypted_data = decrypt_data(data)
                    print(f"Decrypted data: {decrypted_data}")
                    insert_into_db(decrypted_data)
                except Exception as e:
                    print(f"Error handling data: {e}")
        except KeyboardInterrupt:
            print("Server stopped manually.")
        finally:
            cursor.close()
            conn.close()
            print("Database connection closed.")


start_server()
