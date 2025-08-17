import redis
import json
import os
from dotenv import load_dotenv

=
# 🔧 CONFIGURACIÓN

load_dotenv()  # Cargar variables del archivo .env

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", None)

try:
    r = redis.Redis(
        host=REDIS_HOST,
        port=REDIS_PORT,
        password=REDIS_PASSWORD,
        decode_responses=True
    )
    r.ping()  # Probar conexión
    print(" Conectado a KeyDB correctamente")
except Exception as e:
    print(" Error de conexión a KeyDB:", e)
    exit(1)


#  FUNCIONES CRUD

def agregar_libro():
    titulo = input("Título: ")
    autor = input("Autor: ")
    genero = input("Género: ")
    estado = input("Estado (leído/no leído): ")

    # ID único autoincremental
    libro_id = r.incr("libro:id")  
    clave = f"libro:{libro_id}"

    libro = {
        "id": libro_id,
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "estado": estado
    }

    r.set(clave, json.dumps(libro))
    print(f" Libro agregado con ID {libro_id}")

def actualizar_libro():
    libro_id = input("Ingrese el ID del libro a actualizar: ")
    clave = f"libro:{libro_id}"

    if not r.exists(clave):
        print(" No existe un libro con ese ID.")
        return

    libro = json.loads(r.get(clave))

    print("Deje en blanco si no desea cambiar un campo.")
    nuevo_titulo = input(f"Título ({libro['titulo']}): ") or libro['titulo']
    nuevo_autor = input(f"Autor ({libro['autor']}): ") or libro['autor']
    nuevo_genero = input(f"Género ({libro['genero']}): ") or libro['genero']
    nuevo_estado = input(f"Estado ({libro['estado']}): ") or libro['estado']

    libro.update({
        "titulo": nuevo_titulo,
        "autor": nuevo_autor,
        "genero": nuevo_genero,
        "estado": nuevo_estado
    })

    r.set(clave, json.dumps(libro))
    print(" Libro actualizado.")

def eliminar_libro():
    libro_id = input("Ingrese el ID del libro a eliminar: ")
    clave = f"libro:{libro_id}"

    if r.delete(clave):
        print(" Libro eliminado.")
    else:
        print(" No se encontró el libro.")

def ver_libros():
    keys = r.scan_iter("libro:*")
    encontrados = False
    for key in keys:
        libro = json.loads(r.get(key))
        print(f"[{libro['id']}] {libro['titulo']} - {libro['autor']} ({libro['genero']}) [{libro['estado']}]")
        encontrados = True
    if not encontrados:
        print(" No hay libros registrados.")

def buscar_libros():
    criterio = input("Buscar por (titulo/autor/genero): ").lower()
    valor = input("Ingrese el valor a buscar: ")

    keys = r.scan_iter("libro:*")
    encontrados = False
    for key in keys:
        libro = json.loads(r.get(key))
        if valor.lower() in libro.get(criterio, "").lower():
            print(f"[{libro['id']}] {libro['titulo']} - {libro['autor']} ({libro['genero']}) [{libro['estado']}]")
            encontrados = True

    if not encontrados:
        print(" No se encontraron resultados.")


# 🎛️ MENÚ PRINCIPAL

def menu():
    while True:
        print("\n=====  MENÚ BIBLIOTECA =====")
        print("1. Agregar libro")
        print("2. Actualizar libro")
        print("3. Eliminar libro")
        print("4. Ver listado de libros")
        print("5. Buscar libros")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            actualizar_libro()
        elif opcion == "3":
            eliminar_libro()
        elif opcion == "4":
            ver_libros()
        elif opcion == "5":
            buscar_libros()
        elif opcion == "6":
            print(" Saliendo del sistema...")
            break
        else:
            print(" Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
