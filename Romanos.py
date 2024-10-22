'''
Muchas personas están familiarizadas con los números romanos para relativamente números
pequeños. Los símbolos "i", "v", "x", "l" y "c" representan los valores decimales 1, 5, 10, 50
y 100 respectivamente. Para representar a otros valores, estos símbolos, y múltiplos cuando
sea necesario, se concatenan, con los símbolos de menor valor escritos más a la derecha. Por
ejemplo, el número 3 se representa como "III" y el valor 73 es representado como "LXXIII".
Las excepciones a esta regla se producen para los números con valores unitarios de 4 o 9, y
para decenas valores de 40 o 90. Para estos casos, las representaciones de números romanos
son "iv" (4), "ix" (9), "XL" (40) y "XC" (90). Así que las representaciones de números
romanos para 24, 39, 44, 49 y 94 son "xxiv", "xxxix", "xliv", "xlix" y "xciv",
respectivamente. El prefacio de muchos libros tiene páginas numeradas con números
romanos, comenzando con "i" para la primera página del prefacio, y continuando en
secuencia. Supongamos libros con páginas que tienen 100 o menos páginas de prefacio.
¿Cuántos caracteres "i", "v", "x", "l" y "c" son necesarios para numerar las páginas del
prefacio? Por ejemplo, en un prefacio de cinco páginas usaremos los números romanos "i",
"ii", "iii", "iv", y "v", lo que significa que necesitamos 7 caracteres "i" y 2 caracteres "v".

'''

# Función para convertir números a romanos
def int_to_roman(num):
    val = [
        100, 90, 50, 40, 10, 9, 5, 4, 1
        ]
    syb = [
        "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"
        ]
    roman_num = ''
    i = 0
    while  num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num

# Función para contar los caracteres
def count_roman_characters(max_page):
    counts = {"i": 0, "v": 0, "x": 0, "l": 0, "c": 0}
    
    for page in range(1, max_page + 1):
        roman_page = int_to_roman(page).lower()
        
        # Contar las ocurrencias de cada carácter
        for char in counts:
            counts[char] += roman_page.count(char)
    
    return counts

n, result=1,{}
while(n!=0):
    n=int(input("Digite n: "))
    if(n>0):
        result[n]=count_roman_characters(n)

        
