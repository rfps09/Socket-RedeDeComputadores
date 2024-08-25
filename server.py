import socket
from querysDB import get_available_rooms, set_reserved_room, get_rooms_per_cpf, set_delete_reserve

HOST = 'localhost'
PORT = 50000
UNICODE = 'utf-8'
BYTES = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
print('Esperando Conexão...')

conn, addr = s.accept()
print('Conectado ao:', addr)
while True:
    data = conn.recv(BYTES).decode(UNICODE)
    data = data.split(';')
    if data[0] == 'exit':
        msg = 'Fechando Conexão...'
        conn.sendall(msg.encode(UNICODE))
        conn.close()
        break

    if data[0] == 'get_available_rooms':
        msg = get_available_rooms()
        conn.sendall(msg.encode(UNICODE))
    
    if data[0] == 'set_reserved_room':
        msg = set_reserved_room(data[1],data[2])
        conn.sendall(msg.encode(UNICODE))
    
    if data[0] == 'get_rooms_per_cpf':
        msg = get_rooms_per_cpf(data[1])
        conn.sendall(msg.encode(UNICODE))

    if data[0] == 'delete_reserve':
        msg = set_delete_reserve(data[1])
        conn.sendall(msg.encode(UNICODE))