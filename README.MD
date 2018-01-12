DJANGO SERVER FOR BRAINOTES APP
===============================

API-REST for Brainotes app with users and notes models

SERVICES
--------

+ /usuarios/ (GET,POST)
+ /usuarios/{idUsuario} (GET,PUT,DELETE)
+ /notas/ (GET,POST)
+ /notas/{idNota} (GET,PUT,DELETE)


JSON EXAMPLE
------------

User:

{
    "id": 1,
    "nombre": "Alex"
}

Nota:

{
    "id": 1,
    "usuario": 3,
    "fecha_Hora": "2018-01-28T18:35:00Z",
    "titulo": "Cita con el Doctor Gonzalez",
    "cuerpo": "La cita es en el hospital 12 de Octubre en la planta 3 de cardiologia. Asistir con las pruebas realizadas a la consulta",
    "recordatorio": 1,
    "color": "Verde"
}
