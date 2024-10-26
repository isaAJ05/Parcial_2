print("DEPENDENCIAS DEL SISTEMA")

nombres_comandos = ['DEPEND', 'INSTALL', 'REMOVE', 'LIST', 'END']
dict_dependencias = {}
list_instaladas = []

def identificar_comando(comando, elementos): # identifica el comando y llama a la función correspondiente
    if comando in nombres_comandos and comando.isupper(): # si el comando está en la lista y es mayúscula
        match comando:
            case 'DEPEND':
                depend(elementos)
            case 'INSTALL':
                elemento = elementos[0]
                if elemento in list_instaladas: 
                    print(f"    {elemento} ya está instalado.") # no reinstalar si ya estaba
                else:
                    install(elemento) # si no estaba instalado, instalar
            case 'REMOVE':
                elemento = elementos[0]
                if eliminable(elemento): # si se puede eliminar, hacerlo
                    list_instaladas.remove(elemento)
                    print(f"    Eliminando {elemento}...")
                    if elemento in dict_dependencias: # eliminar dependencias si es posible hacerlo
                        dependencias_a_eliminar = dict_dependencias[elemento][:]
                        for dependencia in dependencias_a_eliminar:
                            eliminar_dependencia(dependencia)
            case 'LIST':
                print(list_instaladas) # mostrar lista de elementos instalados
            case 'END':
                exit() # salir del programa
    else:
        print("(!) Nombre de comando no válido.")  


def depend(elementos): # crea un diccionario con las dependencias
    dict_dependencias[elementos.pop(0)] = elementos
    return dict_dependencias

def install(elemento): # instala un elemento y sus dependencias
    if elemento not in list_instaladas:
        if elemento in dict_dependencias:
            for dependencia in dict_dependencias[elemento]:
                install(dependencia)
        list_instaladas.append(elemento)
        print(f"    Instalando {elemento}...")

def eliminable(elemento): # verifica si un elemento se puede eliminar
    if elemento in list_instaladas:
        for dep in dict_dependencias.values():
            if elemento in dep: # si hay elementos que dependen de él
                for dependiente, dependencias in dict_dependencias.items():
                    if elemento in dependencias and dependiente in list_instaladas: # si hay elementos que dependen de él y están instalados
                        print(f"    {elemento} aún se necesita.")
                        return False  # no se puede eliminar     
        return True  # si no hay elementos que dependan de él, se puede eliminar
    else:
        print(f"    {elemento} no está instalado.")
        return False  # si no está instalado, no se puede eliminar
   
def eliminar_dependencia(dependencia): # elimina implícitamente las dependencias si es posible
    i=0
    for dependiente, dependencias in dict_dependencias.items():
        if dependencia in dependencias and dependiente in list_instaladas:
            i+=1 # no se puede eliminar la dependencia si hay otros elementos que tambien dependan de ella
    if i==0:
        list_instaladas.remove(dependencia)
        print(f"    Eliminando {dependencia}...")
           
while True: # main
    comando_ln=input('-> ')
    if len(comando_ln)>80: # validación de 80 carácteres máximo por comando
        print("(!) Comando muy largo.")
    else:
        c=comando_ln.split() # separar por espacios
        elemento_valido=True
        for elemento in c:
            if len(elemento)>10: # validación de 10 carácteres máximo por elemento
                print("(!) Elemento muy largo.")
                elemento_valido=False
                break
        if elemento_valido:
            identificar_comando(c.pop(0),c)
                
    
    