from cryptography.fernet import Fernet

# Generate the key
key = Fernet.generate_key()

# Save the key to a file
with open('secret.key', 'wb') as key_file:
    key_file.write(key)


