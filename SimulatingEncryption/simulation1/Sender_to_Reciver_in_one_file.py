from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from os import urandom

# Generate Buddy's keys (sender)
buddy_private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
buddy_public_key = buddy_private_key.public_key()

# Generate receiver's keys
receiver_private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
receiver_public_key = receiver_private_key.public_key()

# Buddy's operations
# 1. Hash and sign the message
message = b"Hello, secure world!"
hasher = hashes.Hash(hashes.SHA256(), backend=default_backend())
hasher.update(message)
message_hash = hasher.finalize()
signature = buddy_private_key.sign(
    message_hash,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# 2. Generate a new AES key and encrypt the message
aes_key = urandom(32)  # 256-bit key
nonce = urandom(16)  # GCM nonce
aes_cipher = Cipher(algorithms.AES(aes_key), modes.GCM(nonce), backend=default_backend())
encryptor = aes_cipher.encryptor()
encrypted_message = encryptor.update(message) + encryptor.finalize()
auth_tag = encryptor.tag  # Get the authentication tag after finalizing the encryption

# 3. Encrypt the AES key with receiver's public key
encrypted_aes_key = receiver_public_key.encrypt(
    aes_key + nonce + auth_tag,  # Include nonce and auth_tag with the AES key for decryption
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Simulating the receiver's operations
# 1. Verify the signature
try:
    buddy_public_key.verify(
        signature,
        message_hash,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Signature verified: message is from Buddy.")
except Exception as e:
    print("Signature verification failed:", e)

# 2. Decrypt the AES key, nonce, and auth_tag
decrypted_data = receiver_private_key.decrypt(
    encrypted_aes_key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
aes_key_decrypted, nonce_decrypted, auth_tag_decrypted = decrypted_data[:32], decrypted_data[32:48], decrypted_data[48:]

# 3. Decrypt the message
aes_cipher = Cipher(algorithms.AES(aes_key_decrypted), modes.GCM(nonce_decrypted, auth_tag_decrypted), backend=default_backend())
decryptor = aes_cipher.decryptor()
decrypted_message = decryptor.update(encrypted_message) + decryptor.finalize()

# 4. Verify the integrity of the message
hasher = hashes.Hash(hashes.SHA256(), backend=default_backend())
hasher.update(decrypted_message)
new_message_hash = hasher.finalize()

if new_message_hash == message_hash:
    print("Integrity verified: the message is unchanged.")
else:
    print("Integrity check failed: the message has been altered.")

print("Decrypted message:", decrypted_message.decode())
