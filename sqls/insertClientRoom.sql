UPDATE rooms
SET availability = FALSE
WHERE nro_room = id_room;
INSERT INTO client_rooms(room_id,client_id)
VALUES (id_room,user_id)