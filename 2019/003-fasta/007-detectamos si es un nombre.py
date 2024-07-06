#Nombre Alumno:
#Jose Vicente Carratala

def calculaPorcentajesGC(nomfich):
    archivo = open(nomfich,'r')
    lineas = archivo.readlines()
    for linea in lineas:
        if linea[0] == ">":
            pass
        else:
            

if __name__=="__main__":
    print(calculaPorcentajesGC("sampleFasta.fa"))
