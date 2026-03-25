from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open("key.key", "wb") as f:
    f.write(key)

cipher = Fernet(key)

# file read
with open("sample.txt", "rb") as file:
    data = file.read()

# encrypt
encrypted_data = cipher.encrypt(data)

# save encrypted file
with open("sample.enc", "wb") as file:
    file.write(encrypted_data)

print("File Encrypted Successfully!")

#-------------Decryption----------------------
from cryptography.fernet import Fernet

# key load
with open("key.key", "rb") as f:
    key = f.read()

cipher = Fernet(key)

# encrypted file read
with open("sample.enc", "rb") as file:
    encrypted_data = file.read()

# decrypt
decrypted_data = cipher.decrypt(encrypted_data)

# save original file
with open("decrypted.txt", "wb") as file:
    file.write(decrypted_data)

print("File Decrypted Successfully!")