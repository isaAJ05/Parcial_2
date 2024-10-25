print("DEPENDENCIAS DEL SISTEMA")

nombres_comandos = ['DEPEND', 'INSTALL', 'REMOVE', 'LIST', 'END']
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
        
        match comando:
            case 'DEPEND':
                print(depend(elementos))
            case 'INSTALL':
                elemento = elementos[0]
                instalar_con_dependencias(elemento)
            case 'REMOVE':
                elemento = elementos[0]
                if eliminable_tf(elemento): # si está instalada
                    if elemento in instaladas:
                        instaladas.remove(elemento)
                        print(f"eliminando {elemento}")
                        if elemento in dependencias:
                            for dep in dependencias[elemento]:
                                eliminar_dependencia(elemento, dep)
                    else:
                        print(f"{elemento} no está instalado")
                else:
                    print(f"{elemento} no se puede eliminar") # si no está instalada no se puede eliminar
            case 'LIST':
                print(instaladas)
                return 
            case 'END':
                exit()
    else:
        print("(!) Inválido.")  


def depend(elementos): # crea un diccionario con las dependencias
    dependencias[elementos.pop(0)] = elementos
    return dependencias

def instalada_tf(elemento):
    return elemento in instaladas

def instalar_con_dependencias(elemento):
    if not instalada_tf(elemento):
        if elemento in dependencias:
            for dep in dependencias[elemento]:
                instalar_con_dependencias(dep)
        instaladas.append(elemento)
        print(f"instalando {elemento}")
    else:
        print(f"{elemento} ya está instalado")

'''
def eliminable_tf(elemento):
    if already_installed(elemento):
        if elemento in dependencias: # si el elemento tiene dependencias
            for depen in dependencias[elemento]: # recorre las dependencias del elemento
                if depen in instaladas: # si alguna dependencia está instalada
                    return False # no se puede eliminar el elemento
            return True # si no hay dependencias instaladas (ya se eliminaron), se puede eliminar el elemento
        else:
            return True # si el elemento no tiene dependencias, se puede eliminar
    else:
        return False # si no está instalado, no se puede eliminar
'''
def eliminable_tf(elemento):
    if instalada_tf(elemento):
        if elemento in dependencias:  # si el elemento tiene dependencias
            for depen in dependencias[elemento]:  # recorre las dependencias del elemento
                if depen in instaladas:  # si alguna dependencia está instalada
                    return True  # no se puede eliminar el elemento
            return False  # si no hay dependencias instaladas (ya se eliminaron), se puede eliminar el elemento
        else:
            return True  # si el elemento no tiene dependencias, se puede eliminar
    else:
        return False  # si no está instalado, no se puede eliminar


def eliminar_dependencia(elemento, dependencia):
    if dependencia in instaladas:
        # Verificar si la dependencia es requerida por algún otro elemento
        for depen in dependencias.values():
            if dependencia in depen:
                print(f"La dependencia '{dependencia}' es requerida por otro elemento.")
                return False
        
        # Si no es requerida por ningún otro elemento, eliminarla
        if elemento in dependencias and dependencia in dependencias[elemento]:
            dependencias[elemento].remove(dependencia)
            print(f"La dependencia '{dependencia}' ha sido eliminada del elemento '{elemento}'.")
            return True
        else:
            print(f"La dependencia '{dependencia}' no está asociada con el elemento '{elemento}'.")
            return False
    else:
        print(f"La dependencia '{dependencia}' no está instalada.")
        return False

def separar_comandos(comandostr):
    comando_separado = comandostr.split()
    return comando_separado

while True:
    f=input('-> ')
    c=separar_comandos(f)
    identificar_comando(c.pop(0),c)
    