# Problema-Modulo-5--Prog4

🎯 Objetivo
Modificar la aplicación de biblioteca personal para reemplazar el uso de MongoDB por KeyDB, un sistema de almacenamiento en memoria compatible con Redis. Los datos deberán ser almacenados y gestionados usando operaciones rápidas y eficientes mediante redis-py.

📝 Contexto
En esta actividad, los estudiantes aprenderán a utilizar sistemas de almacenamiento en memoria para desarrollar aplicaciones con alto rendimiento en lectura y escritura. Para ello, deben adaptar su aplicación de línea de comandos para que funcione con KeyDB, utilizando estructuras de datos serializadas como JSON.

📌 Requisitos funcionales
La aplicación debe mantener todas las funcionalidades implementadas anteriormente:

Agregar nuevo libro
➤ Añadir libros especificando título, autor, género y estado de lectura.

Actualizar información de un libro
➤ Permitir modificar cualquier dato del libro.

Eliminar libro existente
➤ Eliminar un libro del sistema.

Ver listado de libros
➤ Mostrar todos los libros registrados.

Buscar libros
➤ Permitir búsquedas por título, autor o género.

Salir
➤ Finalizar el programa de forma segura.

🔄 Cambios y objetivos clave
Sustituir MongoDB por KeyDB como sistema de almacenamiento principal.

Representar cada libro como un objeto serializado (por ejemplo, en formato JSON).

Utilizar la biblioteca redis-py (o keydb si se usa un wrapper dedicado) para conectarse y operar con KeyDB.

Implementar todas las operaciones CRUD adaptadas a las estructuras clave-valor de KeyDB.

Configurar KeyDB en el entorno de desarrollo y documentar todo el proceso.

💡 Consideraciones técnicas
Cada libro debe almacenarse como un objeto serializado (por ejemplo, usando json.dumps()).

Usar una clave única para cada libro (libro:<id> o libro:<título> si no hay duplicados).

Las operaciones CRUD deben utilizar comandos como SET, GET, DEL, SCAN, etc.

Las variables de conexión a KeyDB deben estar en un archivo .env (host, puerto, contraseña si aplica).

Incluir un archivo requirements.txt con las dependencias (redis, python-dotenv, etc.).

Manejar excepciones comunes (por ejemplo, conexión fallida, clave no encontrada).
