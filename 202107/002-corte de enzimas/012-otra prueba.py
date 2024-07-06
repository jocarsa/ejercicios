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
    encontrar = secuencia.find(cadena)
    primeraparte = secuencia[0:int(encontrar)+int(corte)]
    segundaparte = secuencia[int(encontrar)+int(corte):-1]
    return [primeraparte,segundaparte]
    

if __name__=="__main__":
    secADN="AAAAAAAAAAGAATTCAAAAAAAAAA"
    print(catalizaSecuencia1Corte("EcoRI",secADN))

    secADN="AAAAAAAAAAGCCCGGGCAAAAAAAAAA"
    print(catalizaSecuencia1Corte("SrfI",secADN))
