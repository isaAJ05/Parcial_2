print("Dependencias del sistema")

nombres_comandos = ['DEPEND', 'INSTALL', 'REMOVE', 'LIST'] # max 10 char

def identificar_comando(comando, elementos):
    if comando in nombres_comandos:
        match(comando):
            case 'DEPEND':
                print(depend(elementos))
            case 'INSTALL':
                if instalada_tf(elementos):
                    instaladas.append(elementos)
                    print("istalar")
                else:
                    print("ya esta")
            case 'REMOVE':
                if instalada_tf(elementos):
                    instaladas.pop(elementos)
                    print("eliminar")
                else:
                    print("ya esta")
            case 'LIST':
                pass
    else:
        print("(!) Inválido.")
    
dependencias = {}
instaladas = []

def depend(elementos):
    dependencias[elementos.pop(0)] = elementos
    return dependencias

def already_installed(elemento):
    if elemento in instaladas:
        return True
    else:
        return False
    
def instalada_tf(elemento):
    if not already_installed(elemento):
        for i,depen in dependencias.items():
            if i == elemento:
                if depen in instaladas:
                        return True
                else:
                    return False
        return True
    else:
        return False
    
def separar_palabras(cadena):
    lista_palabras = cadena.split()
    return lista_palabras



while True:


    list=['a', 'b', 'c']

    f=input('-> ')
    c=separar_palabras(f)
    identificar_comando(c.pop(0),c)