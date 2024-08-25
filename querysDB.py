import sqlite3

def get_available_rooms():
    conn = sqlite3.connect('prj_redes.db')
    cur = conn.cursor()

    f = open('sqls/getAvailableRooms.sql', 'r', encoding='utf-8')
    sql = f.read()
    f.close()

    cur.execute(sql)
    result = cur.fetchall()
    cur.close()

    msg = ''
    for nro_room, type_room in result:
        msg += str(nro_room) + ' - ' + type_room + '\n'
    
    conn.close()
    
    return msg

def set_reserved_room(room_id,user_cpf):
    conn = sqlite3.connect('prj_redes.db')
    cur = conn.cursor()

    f = open('sqls/checkClient.sql', 'r', encoding='utf-8')
    sql = f.read()
    sql = sql.replace('user_cpf', user_cpf)
    f.close()

    cur.execute(sql)
    result = cur.fetchone()

    if result:
        client_id = result[0]
    else:
        f = open('sqls/insertClient.sql', 'r', encoding='utf-8')
        sql = f.read()
        sql = sql.replace('user_cpf', user_cpf)
        f.close()

        cur.execute(sql)
        conn.commit()
        client_id = cur.lastrowid

    f = open('sqls/insertClientRoom.sql', 'r', encoding='utf-8')
    sql = f.read()
    sql = sql.replace('user_id', str(client_id))
    sql = sql.replace('id_room', room_id)
    f.close()

    querys = sql.split(';')

    for query in querys:
        cur.execute(query)
        conn.commit()

    row_id = cur.lastrowid

    cur.close()
    conn.close()
    
    return 'Reserva de N°: ' + str(row_id) + ' Realizda com sucesso!'

def get_rooms_per_cpf(user_cpf):
    conn = sqlite3.connect('prj_redes.db')
    cur = conn.cursor()

    f = open('sqls/getRoomsPerCPF.sql', 'r', encoding='utf-8')
    sql = f.read()
    sql = sql.replace('user_cpf', user_cpf)
    f.close()

    cur.execute(sql)
    result = cur.fetchall()
    cur.close()

    msg = ''
    for nro_reserve, nro_room, type_room in result:
        msg += 'Reserva N° ' + str(nro_reserve) + ': ' + str(nro_room) + ' - ' + type_room + '\n'
    
    conn.close()
    
    return msg

def set_delete_reserve(id_reserve):
    conn = sqlite3.connect('prj_redes.db')
    cur = conn.cursor()

    f = open('sqls/checkRoom.sql', 'r', encoding='utf-8')
    sql = f.read()
    sql = sql.replace('id_reserve', id_reserve)
    f.close()

    cur.execute(sql)
    result = cur.fetchone()
    id_room = str(result[0])

    f = open('sqls/deleteReserve.sql', 'r', encoding='utf-8')
    sql = f.read()
    sql = sql.replace('id_reserve', id_reserve)
    sql = sql.replace('id_room', id_room)
    f.close()

    querys = sql.split(';')

    for query in querys:
        cur.execute(query)
        conn.commit()

    cur.close()
    conn.close()
    
    return 'Reserva de N°: ' + str(id_reserve) + ' CANCELADA!!!'