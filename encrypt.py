import os

from cryptography.fernet import Fernet
import base64

# Get file paths
dir_path = os.path.dirname(os.path.realpath(__file__))
mess_path = os.path.join(dir_path,"Messages")
inps = sorted(os.listdir(mess_path))


# Get key
key_path = os.path.join(dir_path,"Key","key.fernet")
f = open(key_path, "rb")
key = f.read()


# Function to encrypt a file
def encrypt_message(dir_path, message_file, key):

    # Read message
    message_path = os.path.join(dir_path,"Messages",message_file)
    f = open(message_path, 'rb')
    message = f.read()
    f.close()


    # Encrypt message
    cipher = Fernet(key)

    #message_byte = message.encode('utf-8')
    token = cipher.encrypt(message)
    
    
    # Save encrypted message
    out_path = os.path.join(dir_path,"Encrypted-messages",message_file[:-4]+".encrypted")
    f = open(out_path, 'wb')
    f.write(token)
    f.close()

# Loop to encrypt all messages in "Messages"
for f in inps:
    encrypt_message(dir_path,f, key)