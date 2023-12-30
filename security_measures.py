```python
# security_measures.py

import os
import hashlib
from getpass import getpass
from loguru import logger
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_private_key

# Generate a new RSA key pair
def generate_key_pair():
    try:
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        public_key = private_key.public_key()
        return private_key, public_key
    except Exception as e:
        logger.error(f"Error in key pair generation: {e}")
        return None, None

# Save the RSA key pair to files
def save_key_pair(private_key, public_key):
    try:
        # Save the private key
        with open("private_key.pem", "wb") as f:
            f.write(private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            ))
        # Save the public key
        with open("public_key.pem", "wb") as f:
            f.write(public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ))
    except Exception as e:
        logger.error(f"Error in saving key pair: {e}")

# Load the RSA key pair from files
def load_key_pair():
    try:
        # Load the private key
        with open("private_key.pem", "rb") as f:
            private_key = load_pem_private_key(
                f.read(),
                password=None
            )
        # Load the public key
        with open("public_key.pem", "rb") as f:
            public_key = serialization.load_pem_public_key(
                f.read()
            )
        return private_key, public_key
    except Exception as e:
        logger.error(f"Error in loading key pair: {e}")
        return None, None

# Encrypt a message with the public key
def encrypt_message(message, public_key):
    try:
        encrypted_message = public_key.encrypt(
            message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return encrypted_message
    except Exception as e:
        logger.error(f"Error in message encryption: {e}")
        return None

# Decrypt a message with the private key
def decrypt_message(encrypted_message, private_key):
    try:
        decrypted_message = private_key.decrypt(
            encrypted_message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return decrypted_message
    except Exception as e:
        logger.error(f"Error in message decryption: {e}")
        return None
```
