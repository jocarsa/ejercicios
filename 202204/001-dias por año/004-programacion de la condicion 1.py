'''
Ejercicio Python
Jose Vicente Carratalá
'''

def calcula_dias(anyo):
    if anyo%4 == 0 and anyo%100 != 0:
        return 366
    else:
        return 365

if __name__ == "__main__":
    pass
