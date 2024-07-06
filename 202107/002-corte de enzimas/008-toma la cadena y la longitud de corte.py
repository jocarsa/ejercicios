#Nombre Alumno:
#Jose Vicente Carratala

def creaDiccionario(archivo="enzimas.txt"):
    diccionario = {}
    archivo = open(archivo,'r')
    lineas = archivo.readlines()
    for linea in lineas:
        nombre = linea.split(";")[0]
        corte = linea.split(";")[1]
        cadenareconocimiento = linea.split(";")[2].replace("\n","")
        diccionario[nombre] = [cadenareconocimiento,corte]
    return diccionario

def catalizaSecuencia1Corte(nombre_enzima,secuencia,fichero="enzimas.txt"):
    diccionario = creaDiccionario(fichero)
    cadena = diccionario[nombre_enzima][0]
    corte = diccionario[nombre_enzima][1]
    print(cadena,corte)
    

if __name__=="__main__":
    secADN="AAAAAAAAAAGAATTCAAAAAAAAAA"
    print(catalizaSecuencia1Corte("EcoRI",secADN))
