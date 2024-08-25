CREATE TABLE type_of_rooms(
    id           INTEGER         NOT NULL PRIMARY KEY AUTOINCREMENT,
    type_of_room VARCHAR(50) NOT NULL
);
CREATE TABLE rooms(
    nro_room        INTEGER NOT NULL PRIMARY KEY,
    type_of_room_id INTEGER NOT NULL,
    availability    BOOLEAN NOT NULL,
    CONSTRAINT fk_type_of_room
    FOREIGN KEY (type_of_room_id)
    REFERENCES type_of_rooms(id)  
);
CREATE TABLE clients(
    id  INTEGER  NOT NULL PRIMARY KEY,
    cpf CHAR(11) NOT NULL UNIQUE
);
CREATE TABLE client_rooms(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    room_id INTEGER NOT NULL UNIQUE,
    CONSTRAINT fk_client FOREIGN KEY (client_id) REFERENCES clients(id),
    CONSTRAINT fk_room FOREIGN KEY (room_id) REFERENCES rooms(nro_room)
);