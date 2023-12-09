# Guardar el texto en un archivo llamado "texto_preg1.txt"
with open("texto_preg1.txt", "w") as archivo:
    archivo.write(texto_preg1)

# Paso 2: Leer el archivo y contar las ocurrencias de la palabra "la"
with open("texto_preg1.txt", "r") as archivo:
    contenido = archivo.read()
    contador_la = contenido.lower().count("la")

print(f'La palabra "la" aparece {contador_la} veces en el archivo.')

# Paso 3: Agregar texto ingresado por el usuario al final del archivo
texto_usuario = input("Ingrese un texto para agregar al final del archivo: ")

with open("texto_preg1.txt", "a") as archivo:
    archivo.write("\n" + texto_usuario)

print("Texto agregado exitosamente al final del archivo.")