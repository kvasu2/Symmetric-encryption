import os

from cryptography.fernet import Fernet
import base64

key = Fernet.generate_key()

dir_path = os.path.dirname(os.path.realpath(__file__))

# Save key
key_file = os.path.join(dir_path,"Key","key.fernet")
with open(key_file, 'wb') as f:
    f.write(key)
