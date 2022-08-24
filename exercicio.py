
import time

"""for numero in range(3):
    os.system('cls')
    while True:
        print("Informe 3 números diferentes para serem ordenados.\n")
        try:
            num = int(input(f"{numero+1}º número: "))
            if num in numeros:
                print(f"Número {num} já informado, insira um diferente.")
                time.sleep(2)
            else:
                numeros.append(num)
                break
        except ValueError:
            print("Informe um numero inteiro válido.")
            time.sleep(2)
        os.system('cls')"""

import os

os.system('cls')
print("Informe 3 números diferentes para serem ordenados.\n")


numeros = []
ordenacao = [0, 0, 0]

for numero in range(3):
    numeros.append(int(input(f"{numero+1}º número: ")))


def verificar(valor, var1, var2):
    if valor > var1 and valor > var2:
        ordenacao[2] = valor
    elif valor < var1 and valor < var2:
        ordenacao[0] = valor
    else:
        ordenacao[1] = valor


verificar(numeros[0], numeros[1], numeros[2])
verificar(numeros[1], numeros[0], numeros[2])
verificar(numeros[2], numeros[0], numeros[1])


os.system('cls')
print(f"Números ordenados: {ordenacao[0]} - {ordenacao[1]} - {ordenacao[2]}")
