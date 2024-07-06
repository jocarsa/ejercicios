#Nombre Alumno:
#Jose Vicente Carratala

def creaDiccionario(archivo="enzimas.txt"):
    archivo = open(archivo,'r')
    lineas = archivo.readlines()
    
    diccionario = {
        "clave":None,
        "valor":None,
        }
    return diccionario

if __name__=="__main__":
    print(creaDiccionario())
