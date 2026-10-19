# Manejo de números y booleanos en Python

# Nombre: Daniel Rodriguez Moreno

# Matricula: 2630303

# Grupo: 3

# Resumen
"""
En python los numeros intigers(enteros) que son numeros enteros 
que podemos sumar(+), restar(-), multiplicar(*), dividir(/) y
entre otras muchas operaciones,
Tambien existen los Floats que en python son los numeros que 
tienen punto decimal.
En python tambien existen los booleanos: 
True = verdadero
False = falso
Al momento de escribir codigo es importante validar rangos para 
evitar errores confusos y que no entren valores fuera de lo 
permitido. 
El dividir entre cero es un erro matematico en python por lo tanto 
se causa una excepción, por eso se debe comprobar el divisor antes
de dividir
"""
# PRINCIPIOS Y BUENAS PRACTICAS
"""
- Usar tipos apropiados: int para contadores, 
float para cantidades con decimales.
- Evitar duplicar expresiones complejas: 
guardar resultados intermedios en variables.
- Validar datos antes de operar 
(por ejemplo, que horas y salarios no sean negativos).
- Usar nombres de variables descriptivos y mensajes 
claros para el usuario.
- Documentar claramente cómo se interpretan los booleanos 
(qué significa true y qué significa false en cada contexto).  
"""

# PROBLEMS
"""
En este problema utilizamos operaciones matematicas para 
transformar los grados celcius a farenheit y kelvin al igual
que validamos si es una temperatura alta con un true y una baja 
con una false el try y el except los utilisamos para validar 
que se ingrese algo que pueda ser transformado a un numero.
"""
print('problems'.upper())

# Problem 1: Temperature converter and range flag
print('------------------------------------------')
try:
    temp_c = float(input("Ingresa la temperatura en Celsius: "))

    temp_f = (temp_c * 9 / 5) + 32
    temp_k = temp_c + 273.15

    if temp_k < 0:
        print("Error: temperatura imposible en Kelvin.")
    else:
        is_high_temperature = temp_c >= 30.0

        print("Fahrenheit:", temp_f)
        print("Kelvin:", temp_k)
        print("High temperature:", is_high_temperature)

except ValueError:
    print("Error: debes ingresar un número válido.")

"""
------------------------------------------
# Normal
------------------------------------------
Ingresa la temperatura en Celsius: 40
Fahrenheit: 104.0
Kelvin: 313.15
High temperature: True
------------------------------------------
# Borde
------------------------------------------
Ingresa la temperatura en Celsius: 30
Fahrenheit: 86.0
Kelvin: 303.15
High temperature: True
------------------------------------------
# Error
------------------------------------------
Ingresa la temperatura en Celsius: huevo
Error: debes ingresar un número válido.
------------------------------------------
"""
print('------------------------------------------')

#  Problem 2: Work hours and overtime payment
"""
Primero utilizamos try and except para validar que se escriban
numeros(floats and integers) , luego designamos la entrada donde 
se pedira los valores, para posterior con con un if condicionar 
que se escriban solo valores positivos, el eslse lo utilizo para 
que soolo se trabajo en horario normal y posterior asignar el pago
cuando se trabajan tiempos extra.
"""
try:
    hours_worked = float(input("Ingresa las horas trabajadas: "))
    hourly_rate = float(input("Ingresa el pago por hora: "))

    if hours_worked < 0 or hourly_rate < 0:
        print("Error: los valores no pueden ser negativos.")
    else:
        if hours_worked <= 40:
            total_pay = hours_worked * hourly_rate
            has_overtime = False
        else:
            regular_pay = 40 * hourly_rate
            overtime_hours = hours_worked - 40
            overtime_pay = overtime_hours * hourly_rate * 1.5
            total_pay = regular_pay + overtime_pay
            has_overtime = True

        print("Total weekly pay:", total_pay)
        print("Has overtime:", has_overtime)

except ValueError:
    print("Error: debes ingresar valores numéricos.")

"""
------------------------------------------
# Normal
------------------------------------------
Ingresa las horas trabajadas: 50
Ingresa el pago por hora: 100
Total weekly pay: 5500.0
Has overtime: True
------------------------------------------
# Borde
------------------------------------------
Ingresa las horas trabajadas: 41
Ingresa el pago por hora: 100
Total weekly pay: 4150.0
Has overtime: True
------------------------------------------
# Error
------------------------------------------
Ingresa las horas trabajadas: 20
Ingresa el pago por hora: 100
Total weekly pay: 2000.0
Has overtime: False
------------------------------------------
"""
print('------------------------------------------')

#  Problem 3: Discount eligibility with booleans

"""
En este problema asignamos un descuento cuando la compra 
supera el precio de 1000.0 para un estudiante o señor 
utilizando valores enteros, flotantes y booleanos.
Tambien se ralizan operaciones matematicas como el multiplicar
* 0.10 y restarselo al valor para aplicar el descuento.
Se obtiene resultados siempre y cuando sean numeros 
"""
try:
    is_student = input("¿Es estudiante? (si/no): ").lower() == "si"
    is_senior = input("¿Es adulto mayor? (si/no): ").lower() == "si"
    purchase_total = float(input("Ingresa el total de la compra: "))

    if purchase_total < 0:
        print("Error: el total no puede ser negativo.")
    else:
        has_discount = (
            is_student or
            is_senior or
            purchase_total >= 1000.0)

        if has_discount:
            discount = purchase_total * 0.10
        else:
            discount = 0.0

        total_to_pay = purchase_total - discount

        print("Has discount:", has_discount)
        print("Discount amount:", discount)
        print("Total to pay:", total_to_pay)

except ValueError:
    print("Error: ingresa una cantidad válida.")

"""
------------------------------------------
# Normal
------------------------------------------
¿Es estudiante? (si/no): si
¿Es adulto mayor? (si/no): no
Ingresa el total de la compra: 3367
Has discount: True
Discount amount: 336.70000000000005
Total to pay: 3030.3
------------------------------------------
# Borde
------------------------------------------
¿Es estudiante? (si/no):
¿Es adulto mayor? (si/no): si
Ingresa el total de la compra: 0.1
Has discount: True
Discount amount: 0.010000000000000002
Total to pay: 0.09
------------------------------------------
# Error
------------------------------------------
¿Es estudiante? (si/no):
¿Es adulto mayor? (si/no): no
Ingresa el total de la compra: 45
Has discount: False
Discount amount: 0.0
Total to pay: 45.0
------------------------------------------
"""
print('------------------------------------------')

# Problem 4: Basic statistics of three integers

"""
Primero en la entrada coloco la indicacion para que ingresen
los tres numeros, previo se hace la suma 1 + 2 + 3, enseguida 
obtiene el promedio el, el valor max/min mediante operaciones
matematicas y ahi mismo se calcula si los numeros son pares con 
% lo que hace es encontrar el residua al se dividos y si es
cero significa que es par y si es mayor a cero es impar. 
En la sañida me arrora la suma, el promedio, valor maximo 
y minimo y por ultimp me indica si todos son pares con un true 
o si no lo son todos con un false.
"""
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))

suma = num1 + num2 + num3
promedio = float(suma / 3)
valor_maximo = max(num1, num2, num3)
valor_minimo = min(num1, num2, num3)
all_even = (num1 % 2 == 0 and
            num2 % 2 == 0 and
            num3 % 2 == 0)

print("Suma:", suma)
print("Promedio:", promedio)
print("Valor máximo:", valor_maximo)
print("Valor mínimo:", valor_minimo)
print("¿Todos son pares?:", all_even)

"""
------------------------------------------

# Normal
------------------------------------------
Ingresa el primer número: 20
Ingresa el segundo número: 24
Ingresa el tercer número: 80
Suma: 124
Promedio: 41.333333333333336
Valor máximo: 80
Valor mínimo: 20
¿Todos son pares?: True
------------------------------------------
# Borde
------------------------------------------
Ingresa el primer número: 67
Ingresa el segundo número: 77
Ingresa el tercer número: 29
Suma: 173
Promedio: 57.666666666666664
Valor máximo: 77
Valor mínimo: 29
¿Todos son pares?: False
------------------------------------------
# Error
Ingresa el primer número: 0.5
ValueError: invalid literal for int() with base 10: '0.5'
"""
print('------------------------------------------')

#Problem 5: Loan eligibility (income and debt ratio)

"""
Se verifica sei la persona se le puede validar el prestamo 
dependiendo las deudas y el puntaje de credito
lo cual este programa debe arrojar el ratio de endeudamiento y 
true si es valido el prestamo.
"""

monthly_income = float(input("Enter monthly income: "))
monthly_debt = float(input("Enter monthly debt: "))
credit_score = int(input("Enter credit score: "))

if monthly_income > 0:
    debt_ratio = monthly_debt / monthly_income

    eligible = (
        monthly_income >= 8000.0 and
        debt_ratio <= 0.4 and
        credit_score >= 650
    )

    print("Debt ratio:", debt_ratio)
    print("Loan eligible:", eligible)
else:
    print("Monthly income must be greater than zero.")

"""
------------------------------------------
# Normal
------------------------------------------
Enter monthly income: 8967
Enter monthly debt: 2500
Enter credit score: 800
Debt ratio: 0.2788000446080071
Loan eligible: True
------------------------------------------
# Borde
------------------------------------------
Enter monthly income: 8000
Enter monthly debt: 3200
Enter credit score: 650
Debt ratio: 0.4
Loan eligible: True
------------------------------------------
Error
------------------------------------------
Enter monthly income: 7967
Enter monthly debt: 4600
Enter credit score: 400
Debt ratio: 0.5773816995104807
Loan eligible: False
------------------------------------------
"""
print('------------------------------------------')

# Problem 6: Body Mass Index (BMI) and category flag

"""
Dada la estatura y el peso el programa arroja en la salida el
indice de masa corporal e indica si la persona tiene un bajo
peso, un peso normal o un sobrepeso.
"""
weight_kg = float(input("Enter weight in kg: "))
height_m = float(input("Enter height in meters: "))

bmi = weight_kg / (height_m * height_m)

is_underweight = bmi < 18.5
is_normal = 18.5 <= bmi < 25.0
is_overweight = bmi >= 25.0

print("BMI:", bmi)
print("Is underweight:", is_underweight)
print("Is normal:", is_normal)
print("Is overweight:", is_overweight)

"""
------------------------------------------
# Normal
Enter weight in kg: 70
Enter height in meters: 1.65
BMI: 25.71166207529844
Is underweight: False
Is normal: False
Is overweight: True
------------------------------------------
# Borde
------------------------------------------
Enter weight in kg: 40
Enter height in meters: 1.70
BMI: 13.84083044982699
Is underweight: True
Is normal: False
Is overweight: False
------------------------------------------
Error
------------------------------------------
Enter weight in kg: 105
Enter height in meters: 1.75
BMI: 34.285714285714285
Is underweight: False
Is normal: False
Is overweight: True
------------------------------------------
"""
print('------------------------------------------')

# CONCLUCIONES
"""
El uso de numeros ya sea enteros o flotantes al crear un programa
en python te ayuda a desiganarle el valor a distintas constantes,
como tambien el aplicar operaciones matematicas que nos dan valores
mas exactos.
El usar numeros o valores booleanos nos ayuda en un programa para
designar si el vaolor ingresado es correcto.
"""

# REFERENCIAS
"""
1) Python Documentation - Built-in Types (int, float, bool)

https://docs.python.org/3/library/stdtypes.html

2) Python Documentation - Arithmetic and Comparison Operators

https://docs.python.org/3/reference/expressions.html

3) Python Documentation - Built-in Functions (input, int, float, max, min)

https://docs.python.org/3/library/functions.html

4) Python Documentation - Conditional Statements (if, elif, else)

https://docs.python.org/3/tutorial/controlflow.html

5) Python Documentation - Errors and Exceptions (ZeroDivisionError)

https://docs.python.org/3/tutorial/errors.html
"""