import string
import secrets
import os

# Nombre del archivo donde se guardarán las contraseñas
ARCHIVO_CONTRASENAS = "passwords.txt"

def generar_contrasena():
    """
    Pregunta al usuario por la longitud y si desea símbolos,
    y genera una contraseña criptográficamente segura.
    """
    try:
        longitud = int(input("Introduce la longitud deseada para la contraseña: "))
        if longitud < 8:
            print("⚠️ Advertencia: Se recomienda una longitud de al menos 8 caracteres.")
    except ValueError:
        print("❌ Error: Debes introducir un número válido.")
        return None

    incluir_simbolos = input("¿Deseas incluir símbolos (ej: @, #, $)? (s/n): ").lower()

    # Definimos el alfabeto de caracteres a usar
    caracteres = string.ascii_letters + string.digits  # Letras (mayús/minús) y números

    if incluir_simbolos == 's':
        caracteres += string.punctuation  # Añadimos los símbolos

    # Usamos secrets para generar una contraseña segura
    contrasena = ''.join(secrets.choice(caracteres) for i in range(longitud))
    return contrasena

def guardar_contrasena(sitio, contrasena):
    """
    Guarda el sitio y la contraseña en el archivo de texto.
    El modo 'a' (append) añade la línea al final sin borrar lo anterior.
    """
    with open(ARCHIVO_CONTRASENAS, 'a', encoding='utf-8') as f:
        f.write(f"{sitio}:{contrasena}\n")
    print(f"✅ Contraseña para '{sitio}' guardada correctamente.")

def ver_contrasenas():
    """
    Lee y muestra las contraseñas guardadas en el archivo.
    """
    if not os.path.exists(ARCHIVO_CONTRASENAS):
        print("📂 Aún no has guardado ninguna contraseña.")
        return

    print("\n--- Tus Contraseñas Guardadas ---")
    with open(ARCHIVO_CONTRASENAS, 'r', encoding='utf-8') as f:
        lineas = f.readlines()
        if not lineas:
            print("📂 El archivo está vacío.")
        else:
            for linea in lineas:
                # Usamos strip() para quitar saltos de línea y espacios
                sitio, contrasena = linea.strip().split(':', 1)
                print(f"Sitio: {sitio} | Contraseña: {contrasena}")
    print("---------------------------------\n")


def main():
    """
    Función principal que muestra el menú y gestiona las opciones del usuario.
    """
    while True:
        print("\n--==[ Menú Principal ]==--")
        print("1. Crear y guardar una nueva contraseña")
        print("2. Ver contraseñas guardadas")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            nueva_contrasena = generar_contrasena()
            if nueva_contrasena:
                print(f"\nTu nueva contraseña generada es: {nueva_contrasena}")
                sitio = input("¿Para qué sitio o servicio es esta contraseña?: ")
                guardar_contrasena(sitio, nueva_contrasena)
        elif opcion == '2':
            ver_contrasenas()
        elif opcion == '3':
            print("👋 ¡Hasta la próxima!")
            break
        else:
            print("❌ Opción no válida. Inténtalo de nuevo.")

# Esto asegura que el script se ejecute solo cuando lo corres directamente
if __name__ == "__main__":
    main()