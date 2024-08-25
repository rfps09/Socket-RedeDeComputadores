SELECT cr.id, r.nro_room, tr.type_of_room
FROM client_rooms cr
JOIN clients c ON (cr.client_id = c.id)
JOIN rooms r ON (cr.room_id = r.nro_room)
JOIN type_of_rooms tr ON (r.type_of_room_id = tr.id)
WHERE c.cpf = 'user_cpf'