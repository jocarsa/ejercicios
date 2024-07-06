'''
Ejercicio Python
Jose Vicente Carratalá
'''

def distancia(cad1,cad2,voc="ACGT"):
    cad1 = cad1.upper()
    cad2 = cad2.upper()
    for i in range(0,len(cad1)):
        if cad1[i] not in voc or cad1[i] not in voc:
            return -1


if __name__ == "__main__":
    print(distancia("SBS","SSS","sb"))

