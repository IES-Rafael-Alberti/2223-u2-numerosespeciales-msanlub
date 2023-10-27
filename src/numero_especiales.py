# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


'''Ingrese el número inicial: 10
Ingrese el número final: 20
¿Desea calcular la suma de pares o impares? (pares/impares): pares

La suma de los números pares que no son múltiplos de 3 en el rango de 10 a 20 es: 72'''

def eligeParidad(paridad):
    if paridad == "pares":
        True
    else:
        False

def multiploTres(numeroInicial,numeroFinal):
    if numeroInicial %3 == 0 and numeroFinal %3 ==0:
        return True

def sumaPar(numeroInicial,numeroFinal):
    par = 0
    if numeroInicial % 2 == 0 and numeroFinal % 2 == 0:
        par = numeroInicial + numeroFinal
    return par

def sumaImpar(numeroInicial,numeroFinal):
    impar = 0
    if numeroInicial % 2 != 0 and numeroFinal % 2 != 0:
        impar = numeroInicial + numeroFinal
    return impar

if __name__=="__main__":
    #entrada
    numeroInicial = int(input("Ingrese el número inicial: "))
    numeroFinal = int(input("Ingrese el número final: "))
    
    paridad = str(input("Desea calcular la suma de pares o impares?(pares/impares): "))
    
    #proceso
    numeroParidad = eligeParidad(paridad)
    multiplo = multiploTres(numeroInicial,numeroFinal)
    par = sumaPar(numeroInicial,numeroFinal)
    impar = sumaImpar(numeroInicial,numeroFinal)
    if numeroParidad == True:
        if multiplo == False:
            #salida
            print(par)
        else:
            print("No es múltiplo de tres.")
    elif numeroParidad == False:
        if multiplo == False:
            print(impar)
        else:
            print("No es múltiplo de tres.")