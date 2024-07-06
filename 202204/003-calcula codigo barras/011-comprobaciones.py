'''
Ejercicio Python
Jose Vicente Carratalá
'''
import math

def decimal_a_binario(decimal):
    binario = ""
    dividendo = decimal
    while dividendo > 0:
        binario = str(dividendo%2)+binario
        dividendo = math.floor(dividendo/2)
    return binario

def calcula_codigo_barras(num1,num2):
    # creamos un codigo de separacion
    separacion = "101"
    # comprobamos si los numeros son enteros
    if type(num1) != int or type(num2) != int:
        return None
    if len(str(num1)) != 3 or len(str(num2)) != 3:
        return None
    return f"{separacion} {decimal_a_binario(num1)} {separacion} {decimal_a_binario(num2)} {separacion}"
if __name__ == "__main__":
    print(calcula_codigo_barras(725,221))
    print(calcula_codigo_barras(725,-3))
    print(calcula_codigo_barras(725,673))
    print(calcula_codigo_barras(128,128))
