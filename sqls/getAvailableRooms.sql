SELECT r.nro_room, tr.type_of_room
FROM rooms r
JOIN type_of_rooms tr ON (r.type_of_room_id = tr.id)
WHERE r.availability = TRUE