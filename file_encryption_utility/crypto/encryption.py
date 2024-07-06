import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

def get_output_path():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'sandbox', 'output'))

def generate_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def encrypt_file(file_path: str, password: str):
    salt = os.urandom(16)
    key = generate_key(password, salt)
    fernet = Fernet(key)

    with open(file_path, 'rb') as file:
        data = file.read()

    encrypted_data = fernet.encrypt(data)

    output_dir = get_output_path()
    output_path = os.path.join(output_dir, f"{os.path.basename(file_path)}.encrypted")
    with open(output_path, 'wb') as file:
        file.write(salt + encrypted_data)

def decrypt_file(file_path: str, password: str):
    with open(file_path, 'rb') as file:
        salt = file.read(16)
        encrypted_data = file.read()

    key = generate_key(password, salt)
    fernet = Fernet(key)

    decrypted_data = fernet.decrypt(encrypted_data)

    output_dir = get_output_path()
    output_path = os.path.join(output_dir, f"decrypted_{os.path.basename(file_path)[:-10]}")
    with open(output_path, 'wb') as file:
        file.write(decrypted_data)