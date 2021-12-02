import socket
import hashlib

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host, port))
s.listen(1)
print(host)
print('Waiting for connections...')
conn, addr = s.accept()
print(addr, 'Connected to the server')

filename = input(str('Enter the file name: '))
file = open(filename, 'rb')
file_data = file.read(1024)
conn.send(file_data)
print('Success!')

hasher = hashlib.md5()
with open(filename, 'rb') as open_file:
    content = open_file.read()
    hasher.update(content)
    print (hasher.hexdigest())