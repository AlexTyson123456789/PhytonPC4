#-----------------------------------PROBLEMA_1-------------------------------------------------------

# Paso 1: Guardar el texto en un archivo
texto_del_problema1 = """En el ámbito del desarrollo de software, la colaboración es fundamental. La 
colaboración eficiente impulsa la eficacia y mejora la calidad del código. La calidad del 
código, a su vez, es esencial para la mantenibilidad del sistema. Mantener un sistema 
sin problemas es esencial para la satisfacción del cliente. La satisfacción del cliente, por 
supuesto, es un objetivo clave para cualquier equipo de desarrollo. Desarrollar 
estrategias para fomentar la colaboración continua y mejorar la calidad del código es 
una práctica que beneficia a todos los miembros del equipo y contribuye al éxito 
general del proyecto"""

# sirve apra guardar el texto en un archivo
with open('texto.txt', 'w') as texto:
    texto.write(texto_del_problema1)

# Lee el archivo y contar las ocurrencias de la palabra "la"
with open('texto.txt', 'r') as texto:
    contenido = texto.read()
    contar_la_palabra_la = contenido.lower().count("la")

print(f'La palabra "la" aparece {contar_la_palabra_la} veces en el archivo texto_del_problema1.')

# se ingresar un nuevo texto para agregarlo al final del trexto
texto_ingresado = input("Ingrese un texto para agregar al final del texto: ")

with open('texto.txt', 'a') as texto:
    texto.write('\n' + texto_ingresado)

print('Texto ingresado agregado al final del archivo texto.')
