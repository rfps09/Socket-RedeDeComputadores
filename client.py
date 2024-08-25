import socket

HOST = 'localhost'
PORT = 50000
UNICODE = 'utf-8'
BYTES = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

def main_menu():
    print('Digite a opção desejada')
    print('Menu:')
    print('1 - Reservar quarto')
    print('2 - Cancelar reserva')
    print('3 - Sair')

def get_cpf(msg):
    user_cpf = input(msg)
    if user_cpf.isdigit() and len(user_cpf) == 11:
        return user_cpf
    else:
        return -1

def get_nro_room(msg):
    user_input = input(msg)
    if user_input.isdigit():
        return user_input
    else:
        return -1
    
def get_reserved_rooms_per_cpf(user_cpf):
    msg = 'get_rooms_per_cpf' + ';' + user_cpf
    s.sendall(msg.encode(UNICODE))
    data = s.recv(BYTES).decode(UNICODE)
    print(f'-- Quartos reservados para o cpf({user_cpf}) --')
    print(data)    
    
def available_rooms():
    msg = 'get_available_rooms'
    s.sendall(msg.encode(UNICODE))
    data = s.recv(BYTES).decode(UNICODE)
    print('-- Quartos disponíveis para reserva --')
    print(data)

while True:
    main_menu()
    user_input = input()
    if user_input.isdigit() and int(user_input) > 0 and int(user_input) < 4:
        user_input = int(user_input)
        
        if user_input == 1:
            available_rooms()
            nro_room = get_nro_room('Digite o número do quarto que deseja reservar:')
            if nro_room != -1:
                user_cpf = get_cpf('Insira seu CPF (apenas número, sem . ou -) para concluir a reservar:')
                if user_cpf != -1:
                    msg = 'set_reserved_room' + ';' + nro_room + ';' + user_cpf
                    s.sendall(msg.encode(UNICODE))
                    data = s.recv(BYTES).decode(UNICODE)
                    print(data)
                else:
                    print('O formato do cpf não é válido!!!')
            else:
                print('A entrada não é um número!!!')
        
        if user_input == 2:
            user_cpf = get_cpf('Insira seu CPF (apenas número, sem . ou -):')
            if user_cpf != -1:
                get_reserved_rooms_per_cpf(user_cpf)
                print('Digite o N° da reserva que deseja cancelar:')
                id_reserve = input()
                if id_reserve.isdigit():
                    msg = 'delete_reserve' + ';' + id_reserve
                    s.sendall(msg.encode(UNICODE))
                    data = s.recv(BYTES).decode(UNICODE)
                    print(data)
                else:
                    print('A entrada não é um número!!!')
        
        if user_input == 3:
            msg = 'exit'
            s.sendall(msg.encode(UNICODE))
            data = s.recv(BYTES).decode(UNICODE)
            print(data)
            break
    else:
        print('Escolha Inválida!!!')