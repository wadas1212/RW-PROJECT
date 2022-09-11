#!/bin/bash


#copy the file to the folder where this file is located this will be done first.


function online {
a=$(ls | grep *.*.*.*)
  return $?
}

until online
do
  sleep 1
done

#####################################################
#	HERE_DOC for the decryption
# this is a python code that helps in decryption
python3 - <<HERE
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
from cryptography.fernet import Fernet
import os
import pathlib
import sys

with open('EMAIL_ME.txt', 'rb') as f:
    enc_fernet_key = f.read()
    #print(enc_fernet_key)

# Private RSA key
private_key = RSA.import_key(open('private.pem').read())

# Private decrypter
private_crypter = PKCS1_OAEP.new(private_key)

dec_fernet_key = private_crypter.decrypt(enc_fernet_key)
with open('decrypted_fernet_key.txt', 'wb') as f:
    f.write(dec_fernet_key)
HERE
#####################################################


#rm $a
#cp d$a ~/Desktop/Decrypted/
#rm d$a


 
