print("DEPENDENCIAS DEL SISTEMA")

nombres_comandos = ['DEPEND', 'INSTALL', 'REMOVE', 'LIST']
dependencias = {}
instaladas = []

'''
[VALIDACIONES POR HACER]
comando: 80 char max
elementos: 10 char max
distinguir may y min

INSTALAR
instalar elemento Y sus dependencias
si ya está, no volver a instalar (incluso si fue instalado por otra dependencia)

ELIMINAR
eliminar elemento y sus dependencias si no hay mas elementos que dependan de ellas
solo se puede eliminar una dependencia si no hay mas elementos que dependan de ella (ya no se necesita)
'''
def identificar_comando(comando, elementos):
    if comando in nombres_comandos:
        match(comando):
            case 'DEPEND':
                print(depend(elementos)) # crea diccionario para determinar las dependencias
            case 'INSTALL':
                if instalada_tf(elementos):
                    instaladas.append(elementos) # agrega el elemento a la lista de instalados
                    print("instalar")
                else:
                    print("ya está") # si ya está instalado previamente no se agrega a la lista
            case 'REMOVE':
                if not instalada_tf(elementos): # si está instalada
                    instaladas.pop(elementos)
                    print("eliminar")
                else:
                    print("no está instalado") # si no está instalada no se puede eliminar
            case 'LIST':
                print(instaladas) # imprime la lista de elementos instalados
    else:
        print("(!) Inválido.")  


def depend(elementos): # crea un diccionario con las dependencias
    dependencias[elementos.pop(0)] = elementos
    return dependencias

def already_installed(elemento): # verifica si ya está instalado el elemento o no
    if elemento in instaladas:
        return True # ya está instalado el elemento
    else:
        return False # aún no está instalado el elemento
    
def instalada_tf(elemento): 
    if not already_installed(elemento): # si no está instalado
        for i,depen in dependencias.items(): # recorre el diccionario de dependencias
            if i == elemento:
                if depen in instaladas: 
                        return True # si el elemento tiene dependencia y está instalado
                else:
                    return False # si el elemento tiene dependencia pero no está instalado
        return True # si no tiene dependencias y aún no está instalado
    else:
        return False # si no tiene dependencias pero ya está instalado
    
def separar_comandos(comandostr):
    comando_separado = comandostr.split()
    return comando_separado



while True:
    f=input('-> ')
    c=separar_comandos(f)
    identificar_comando(c.pop(0),c)
    if c[0] == 'END':
        break