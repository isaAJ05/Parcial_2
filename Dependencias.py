print("DEPENDENCIAS DEL SISTEMA")

nombres_comandos = ['DEPEND', 'INSTALL', 'REMOVE', 'LIST', 'END']
dependencias = {}
instaladas = []

'''
ya funciona :D
[VALIDACIONES POR HACER]
comando: 80 char max
elementos: 10 char max
distinguir may y min

- y falta comentar tambien :p
'''
def identificar_comando(comando, elementos):
    if comando in nombres_comandos:
        match comando:
            case 'DEPEND':
                print(depend(elementos))
            case 'INSTALL':
                elemento = elementos[0]
                if elemento in instaladas:
                    print(f"{elemento} ya está instalado")
                else:
                    install(elemento)
            case 'REMOVE':
                elemento = elementos[0]
                if eliminable_tf(elemento): 
                    instaladas.remove(elemento)
                    print(f"Eliminando {elemento}")
                    if elemento in dependencias: 
                        dependencias_a_eliminar = dependencias[elemento][:]
                        for dep in dependencias_a_eliminar:
                            eliminar_dependencia(dep)
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

def install(elemento):
    if elemento not in instaladas:
        if elemento in dependencias:
            for dep in dependencias[elemento]:
                install(dep)
        instaladas.append(elemento)
        print(f"Instalando {elemento}")

def eliminable_tf(elemento):
    if elemento in instaladas:
        for deps in dependencias.values():
            if elemento in deps: # si hay elementos que dependen de él
                for dependiente, dependencias_dep in dependencias.items():
                    if elemento in dependencias_dep and dependiente in instaladas: # si hay elementos que dependen de él y están instalados
                        print(f"{elemento} aún se necesita")
                        return False  # no se puede eliminar     
        return True  # si el elemento no tiene dependencias, se puede eliminar
    else:
        print(f"{elemento} no está instalado")
        return False  # si no está instalado, no se puede eliminar
   
def eliminar_dependencia(dependencia):
    i=0
    for dependiente, dependencias_dep in dependencias.items():
        if dependencia in dependencias_dep and dependiente in instaladas:
            i+=1
    if i==0:
        instaladas.remove(dependencia)
        print(f"Eliminando {dependencia}")
           

while True:
    f=input('-> ')
    c=f.split()
    identificar_comando(c.pop(0),c)
    