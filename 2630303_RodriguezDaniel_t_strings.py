# Nombre: Daniel Rodriguez Moreno

# Matricula: 2630303

# Grupo: 3

# PRINCIPIOS Y BUENAS PRÁCTICAS
"""
- Los strings son inmutables: cualquier cambio genera una 
nueva cadena.
- Es buena práctica normalizar entrada con strip() y lower() 
antes de compararla.
- Evitar "números mágicos" en índices; documentar qué extrae 
cada slice.
- Usar métodos de string en lugar de reescribir lógica básica.
- Diseñar validaciones claras: primero que no esté vacío, luego 
el formato.
- Escribir código legible: nombres de variables claros y 
mensajes de error entendibles.
"""
# Resumen ejecutivo

"""
un string en Python es un tipo de dato que representa una 
secuencia de caracteres. Los strings son inmutables, lo que 
significa que una vez creados, no se pueden modificar 
directamente; cualquier operación que parezca modificar un 
string en realidad crea uno nuevo.
Es importante validar y normalizar texto de entrada para 
asegurar que los datos sean consistentes y seguros, especialmente
en aplicaciones que manejan información sensible como correos.

"""

# Problems
print('problems'.upper())
print('--------------------------------')
 # Problem 1: Full name formatter
"""
    Description: Este problema consiste en tomar un nombre 
    completo ingresado por el usuario y formatearlo de manera 
    adecuada, asegurando que cada parte del nombre comience con 
    una letra mayúscula y que no haya espacios innecesarios.

"""
# TEST CASES:
name = input("Escribe tu nombre: ")
full_name = name.title()
words = full_name.split()
if len(words) == 0:
    print('Error')
else:
    full_name = " ".join(words)
    formatted_name = full_name.title()
    initials = ""
    for word in words:
        initials = initials + word[0].upper() + "."
print("formatted_name:", formatted_name)
print("initials:", initials)

# OUTPUT
"""
# Normal
--------------------------------
Escribe tu nombre: daniel rodriguez moreno
formatted_name: Daniel Rodriguez Moreno
initials: D.R.M.
--------------------------------
# Borde
--------------------------------
Escribe tu nombre: DaNiel RODRIguez MoReNo
formatted_name: 
initials: D.R.M.
--------------------------------
# Error
--------------------------------
Escribe tu nombre: 1234
formatted_name: 1234
initials: 1.
--------------------------------
"""

print('--------------------------------')

 # problem 2: Email validator

"""
    Description: Este problema consiste en validar una 
    dirección de correo electrónico ingresada por el usuario, 
    asegurando que cumpla con un formato básico de correo 
    electrónico.

"""
# TEST CASES:
email_text = input("Escribe tu email: ")
email_text = email_text.strip()
at_sign = email_text.find("@")
domain = email_text[at_sign + 1:]
print(email_text)
if email_text.count("@") == 1 and "." in domain and " " not in email_text: 
    print('valid_email: True')
    print('Dominio:', domain)
else:
   print("valid_email: False")

   # OUTPUT
"""
# Normal
--------------------------------
Escribe tu email: 2630303@upv.edu.mx
2630303@upv.edu.mx
valid_email: True
Dominio: upv.edu.mx
--------------------------------
# Borde
--------------------------------
Escribe tu email: d@r.m
d@r.m
valid_email: True
Dominio: r.m
--------------------------------
#Error
--------------------------------
Escribe tu email: daniel@xd
daniel@xd
valid_email: False
--------------------------------
"""
print('--------------------------------')

 #problem 3: Palindrome checker 

"""
    Description: Este problema consiste en verificar si una
    cadena de texto ingresada por el usuario es un palíndromo,
    es decir, si se lee igual de izquierda a derecha que de
    derecha a izquierda, ignorando espacios y mayúsculas/minúsculas.
    
"""
# TEST CASES:
is_palindrome = input("Escribe un palindromo: ")
is_palindrome = is_palindrome.replace(" ", "")
if is_palindrome == is_palindrome[::-1]:
    print('Palindromo: True')
    
else: 
    is_palindrome != is_palindrome[::-1]
    print('Palindromo: False')

    # OUTPUT
"""
# Normal
--------------------------------
Escribe un palindromo: amo la paloma
Palindromo: True
--------------------------------
# Borde
--------------------------------
Escribe un palindromo: a
Palindromo: True
--------------------------------
# Error
--------------------------------
Escribe un palindromo: dinosaurio
Palindromo: False
--------------------------------
"""
print('--------------------------------')

 #problem 4: Sentence word stats 
"""
    Description:
    Dada una oración, se debe normalizar el texto,
    organizarze, eliminar espacios al inicio y al
    final y separar por espacios.
    Tambien debe arrojar el numero de palabras,
    la primera y la ultima palabra y al igual que la 
    palabra mas larga por longitud.

"""
# TEST CASES:
sentences = input('Escribe una oracion: ')
sentences = sentences.strip()
sentences = sentences.split()
if len(sentences) == 0:
    print('error')
else:
    print('word_count:', len(sentences))
    print('First_word:', sentences[0])
    print('Last_word:', sentences[-1])
    print('Shortest_word:', min(sentences, key=len))
    print('longest_word:', max(sentences,key=len))

# OUTPUT
"""
# Normal
--------------------------------
Escribe una oracion: todos los domingos voy a misa
word_count: 6
First_word: todos
Last_word: misa
Shortest_word: a
longest_word: domingos
--------------------------------
# Error
--------------------------------
Escribe una oracion:
error
--------------------------------
"""    
print('--------------------------------')

 #problem 5: Password strength classifier
"""
En este problema pongo una condicion ala hora de generar una
una contraseña weak muy simple, donde se tiene que colocar una 
cantidad exactade 8 caracteres para que la contraseña sea 
valida, caso contario me señala que mi contraseña es invalida. 
"""
Pasword = input('Escribe tu contraseña: ')
if len(Pasword) == 8:
    print('Valid password')
else:
    print('Invalid password')
print('--------------------------------')

    # OUTPUT
"""
# normal
--------------------------------
Escribe tu contraseña: mpasword
Valid password
--------------------------------
# Borde
--------------------------------
Escribe tu contraseña: mtxwnqpz
Valid password
--------------------------------
# Error
--------------------------------
Escribe tu contraseña: 12sdfggjijo
Invalid password
--------------------------------
"""

 #problem 6: Product label formatter
"""
Description: 
En este problema genero un etiqueta con el npmbre y precio
del producto, donde al inicio coloco un producto y le doy 
valor valido de mas de 30 cacteres y me genera una etiqueta 
de lo contrario me marca un error.
"""
product_name = input("Nombre del producto: ").strip()
price_value = input("Precio del producto: ")

if product_name == "":
    print("Error: el nombre no puede estar vacío")
else:
    try:
        price = float(price_value)

        if price <= 0:
            print("Error: el precio debe ser positivo")
        else:
            label = f"Product: {product_name} | Price: ${price_value}"
            label = label[:30].ljust(30)
            print(f'"{label}"')

    except ValueError:
        print("Error: introduce un precio válido")

# OUTPUT
"""
# Normal
--------------------------------
Nombre del producto: pan
Precio del producto: 11
"Product: pan | Price: $11     "
--------------------------------
# Borde
--------------------------------
Nombre del producto: cocacola
Precio del producto: 50
"Product: cocacola | Price: $50"
--------------------------------
# Error
--------------------------------
Nombre del producto: aceite nutrioli
Precio del producto: 55
"Product: aceite nutrioli | Pri"
--------------------------------
"""
print('--------------------------------')

# Conclusiones
"""
El buen manejo de los strings ala hora de comparar o validar
datos que nos proporcionan es muy importante ya que nos permite
organizar y seleccionar mas a fondo toda esa informacion, desde 
capturar si una respuesta fue valida, hasta saber la cantidad de 
caracteres en una oracion.
En mi opinion es una herramienta que nos agiliza el trabajo y 
gracias a su inmutibilidad nos permite guardar sus cambios 
de manera correcta y que no sea tan facil, metodos como lower() 
que nos convierte las letras a minusculas, el strip() que nos 
ayuda a separar las palabras correctamente y otros mas que nos 
ayudan a agilizar el trabajo y mejorarlo.
"""
# Referencias 
"""
1) Python documentation - https://docs.python.org/es/3/library/string.html#module-string — str
2) Python documentation - https://www.geeksforgeeks.org/python/why-are-python-strings-immutable/ - str
3) Python documentation - https://www.bing.com/videos/riverview/relatedvideo?q=python+strings+methods&&mid=C06BFD6216C3EF9C3B3DC06BFD6216C3EF9C3B3D&churl=https%3a%2f%2fwww.youtube.com%2fchannel%2fUCZ73n3-oODMvkoBbXYQFM4g&FORM=VRDGAR -str
4) Python documentation - https://www.bing.com/videos/riverview/relatedvideo?q=python+strings+methods&&mid=458897D206EBE3CCFDC3458897D206EBE3CCFDC3&churl=https%3a%2f%2fwww.youtube.com%2fchannel%2fUCtEVu-quNsZrhXU6Ekm-PXA&FORM=VRDGAR -str 
5) Python documentation - und_string.py -str

"""