'''
Ejercicio Python
Jose Vicente Carratalá
'''

def calcula_dias(anyo):
    if type(anyo) == int and anyo >= 0:
        if (anyo%4 == 0 and anyo%100 != 0) or (anyo%4 == 0 and anyo%100 == 0 and anyo%400 == 0):
            return 366
        else:
            return 365
    else:
        return -1
if __name__ == "__main__":
    print(calcula_dias(2002))
    print(calcula_dias(2004))
    print(calcula_dias(2000))
    print(calcula_dias(-100))
