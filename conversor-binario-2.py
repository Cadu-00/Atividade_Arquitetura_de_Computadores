import math

lista_de_numeros = [32, 57, 101, 77]
numero = ""

#Apenas um loop para utilizar os numeros de dentro da lista.
for n in lista_de_numeros:

    #Funcao de uma biblioteca de terceiros que converte numeros decimais para binarios
    numero = bin(n)
    print(f"{n} = {numero[2:]}")