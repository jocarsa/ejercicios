#Nombre Alumno:
#Jose Vicente Carratala

def calculaPorcentajesGC(nomfich):
    archivo = open(nomfich,'r')
    lineas = archivo.readlines()
    lista = []
    for linea in lineas:
        if linea[0] == ">":
            pass
        else:
            linea = linea.replace("\n","")
            print(linea)
            total = len(linea)
            contador = 0
            for letra in linea:
                if letra == "G" or letra == "C":
                    contador += 1
            lista.append(contador, total,(contador/total)*100)

if __name__=="__main__":
    print(calculaPorcentajesGC("sampleFasta.fa"))
