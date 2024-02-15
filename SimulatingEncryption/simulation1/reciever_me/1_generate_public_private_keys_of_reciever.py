from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from os import urandom

# Generate receiver's keys
receiver_private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
receiver_public_key = receiver_private_key.public_key()



# Serialize Receiver's public key to PEM format
receiver_public_pem = receiver_public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Write Receiver's public key to a file
with open('./receiver_public_key.pem', 'wb') as f:
    f.write(receiver_public_pem)
    


# Serialize Receiver's private key to PEM format
receiver_private_pem = receiver_private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    # encryption_algorithm=serialization.BestAvailableEncryption(b'mypassword')
    encryption_algorithm=serialization.NoEncryption()
    # Use serialization.NoEncryption() if you don't want to encrypt the private key
)

# Write Receiver's private key to a file
with open('receiver_private_key.pem', 'wb') as f:
    f.write(receiver_private_pem)