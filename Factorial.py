'''
Ella ha sido capaz de
convencerlos de que la frecuencia de aparición de los dígitos en la representación decimal de
los factoriales dan testimonio de su futuro, a diferencia de la lectura de la palma de la mano.
Sin embargo, ella no puede simplemente evocar estas frecuencias, por lo que los emplea a
ustedes para determinar estos valores.

Recordemos que la definición de n! (es decir, n factorial) es sólo 1×2×3×...×n. Como ella
espera usar el día de la semana, el día del mes, o el día del año como el valor de n. Usted
debe ser capaz de determinar el número de ocurrencias de cada dígito decimal en números
tan grandes como 366 factorial (366!), que tiene 781 dígitos.

Los datos de entrada para el programa son simplemente una lista de enteros para los cuales
Se desean los recuentos de dígitos. Todos estos valores de entrada serán menores que o igual
que 366 y mayor que 0, excepto para el último entero, que será cero. No se moleste en
procesar este valor cero; justo detenga su programa en ese momento. El formato de salida no
es demasiado crítico, pero debe hacer que su programa produzca resultados que se parecen a
los que se muestran a continuación.

Entrada de muestra
3
8
100
0
Resultado esperado
3! --
 (0) 0 (1) 0 (2) 0 (3) 0 (4) 0
 (5) 0 (6) 1 (7) 0 (8) 0 (9) 0
8! --
 (0) 2 (1) 0 (2) 1 (3) 1 (4) 1
 (5) 0 (6) 0 (7) 0 (8) 0 (9) 0
100! --
 (0) 30 (1) 15 (2) 19 (3) 10 (4) 10
 (5) 14 (6) 19 (7) 7 (8) 14 (9) 20
'''

# Habria que cambiar esto a algo que entendamos mas, por ejemplo como sacar el factoria las efectivamente
#pero en teoria es lo mismo que el numero romanos
import math
from collections import Counter

def factorial_digit_frequency(n):
    # Calcular el factorial del número n
    factorial_result = math.factorial(n)
    
    # Convertir el factorial a una cadena de texto
    factorial_str = str(factorial_result)
    
    # Contar la frecuencia de cada dígito usando Counter
    digit_frequency = Counter(factorial_str)
    
    # Crear un diccionario con las frecuencias de los dígitos del 0 al 9
    frequency_dict = {str(i): digit_frequency.get(str(i), 0) for i in range(10)}
    
    return frequency_dict

lista,n=[],1
while(n!=0):
    n=int(input("Digite n: "))
    if(n>0 and n<=366):
        lista.append(n)
    
for elem in lista:
    result = factorial_digit_frequency(elem)
    print(f'\n{elem}! --')
    text=''
    for dig in range(5):
        text+=f'({dig}): {result[str(dig)]}    '
    print(text)
    text=''
    for dig in range(5, 10):
        text+=f'({dig}): {result[str(dig)]}    '
    print(text)
        


