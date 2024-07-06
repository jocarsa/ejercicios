'''
Ejercicio Python
Jose Vicente Carratalá
'''

def calcula_codigo_barras(num1,num2):
    # creamos un codigo de separacion
    separacion = "101"
    # comprobamos si los numeros son enteros
    if type(num1) != int or type(num2) != int:
        return None
    if len(str(num1)) != 3 or len(str(num2)) != 3:
        return None
    return 1
if __name__ == "__main__":
    print(calcula_codigo_barras(725,221))
