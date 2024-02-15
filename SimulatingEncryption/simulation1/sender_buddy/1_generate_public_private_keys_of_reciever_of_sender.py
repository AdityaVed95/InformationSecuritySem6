# from cryptography.hazmat.primitives import hashes
# from cryptography.hazmat.primitives.asymmetric import padding, rsa
# from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
# from cryptography.hazmat.backends import default_backend
# from os import urandom

# # Generate Buddy's keys (sender)
# buddy_private_key = rsa.generate_private_key(
#     public_exponent=65537,
#     key_size=2048,
#     backend=default_backend()
# )
# buddy_public_key = buddy_private_key.public_key()

# print(type(buddy_public_key))

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from os import urandom

# Generate Buddy's keys (sender)
buddy_private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
buddy_public_key = buddy_private_key.public_key()

# Serialize Buddy's public key to PEM format
buddy_public_pem = buddy_public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Write Buddy's public key to a file
with open('./buddy_public_key.pem', 'wb') as f:
    f.write(buddy_public_pem)

# Serialize Buddy's private key to PEM format
buddy_private_pem = buddy_private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()  # No encryption for demonstration
    # Use serialization.BestAvailableEncryption(b'mypassword') for encrypted storage
)

# Write Buddy's private key to a file
with open('buddy_private_key.pem', 'wb') as f:
    f.write(buddy_private_pem)
