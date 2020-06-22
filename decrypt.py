import os

from cryptography.fernet import Fernet
import base64


# Get file paths
dir_path = os.path.dirname(os.path.realpath(__file__))
enc_mess_path = os.path.join(dir_path,"Encrypted-messages")
inps = sorted(os.listdir(enc_mess_path))


# Get key
key_path = os.path.join(dir_path,"Key","key.fernet")
f = open(key_path, "rb")
key = f.read()


# Function to encrypt a file
def decrypt_message(dir_path, message_file, key):

    # Read message
    enc_message_path = os.path.join(dir_path,"Encrypted-messages",message_file)
    f = open(enc_message_path, 'rb')
    encrypted = f.read()
    f.close()

    
    # Decrypt message
    cipher = Fernet(key)
    decoded = cipher.decrypt(encrypted)

    # Save decrypted message
    out_path = os.path.join(dir_path,"Decrypted-messages",message_file[:-10]+".txt")
    f = open(out_path, 'wb')
    f.write(decoded)
    f.close()

# Loop to encrypt all messages in "Encrypted-messages"
for f in inps:
    decrypt_message(dir_path,f, key)