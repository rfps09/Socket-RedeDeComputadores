DELETE FROM client_rooms
WHERE id = id_reserve;
UPDATE rooms
SET availability = TRUE
WHERE nro_room = id_room;