'''
Problema 2 – Frequencias Factoriales 
En un intento de reforzar su flojo negocio de lectura de palmas, Madame Adivinación ha 
decidido ofrecerle varias delicias numerológicas a su clientela. Ella ha sido capaz de 
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
Madame Adivinación estará para siempre (o más) en deuda con usted; Ella podría ¡Incluso 
darles un viaje si hacen bien tu trabajo!

Entrada de muestra 
3 
8 
100 
0 
Resultado esperado 
3! -- 
   (0)    0    (1)    0    (2)    0    (3)    0    (4)    0 
   (5)    0    (6)    1    (7)    0    (8)    0    (9)    0 
8! -- 
   (0)    2    (1)    0    (2)    1    (3)    1    (4)    1 
   (5)    0    (6)    0    (7)    0    (8)    0    (9)    0 
100! -- 
   (0)   30    (1)   15    (2)   19    (3)   10    (4)   10 
   (5)   14    (6)   19    (7)    7    (8)   14    (9)   20 
'''
print("Frecuencias Factoriales")
print("Adivina tu futuro con los dígitos de los factoriales.")
n=1
while(n!=0):
    n = int(input("\nIngrese un número entero para calcular su factorial (0 si desea salir): "))
    if n > 0 and n <= 366: #validacion de rango
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i #calculo del factorial
        print(f"{n}! -- ")
        for i in range(10): #recorrido de los digitos
            print(f"  ({i}) {str(factorial).count(str(i))} ", end="") #conteo de ocurrencias de cada dígito en el factorial
            if i % 2 == 0: #salto de línea
                print() 
    else if
    else:
        print("Número inválido. Intente de nuevo.")
