#Nombre Alumno:
#Jose Vicente Carratala

def creaDiccionario(archivo="enzimas.txt"):
    lista = []
    archivo = open(archivo,'r')
    lineas = archivo.readlines()
    for linea in lineas:
        nombre = linea.split(";")[0]
        corte = linea.split(";")[1]
        cadenareconocimiento = linea.split(";")[2]
        diccionario = {
            "clave":nombre,
            "valor":[cadenareconocimiento,corte],
            }
    return diccionario

if __name__=="__main__":
    print(creaDiccionario())
