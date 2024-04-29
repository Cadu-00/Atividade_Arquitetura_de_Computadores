# Conversor de numeros Decimais para numeros Binarios

#E so rodar para ver que funciona.

import math

# Primeiro, criamos 3 variaveis. A primeira para guardar o numero que sera convertido;
# a segunda para guardar as partes do numero; e a terceira para juntar todas as partes
# em um numero binario.

num = 156
binario = []
binario_formatado = ""

# Iniciaremos um loop que ira parar quando o numero for igual a 1.

while num != 1:

    # Aqui pegamos o resto da divisao que faz parte da conversao para binario.
    binario_parte = num % 2

    # Depois o adicionamos em uma lista.
    binario.append(binario_parte)

    # Em seguida divide o numero por dois devido a divisao sucessiva por 2 para
    # alcancar o binario
    num = int(num / 2)

# E necessario passar a divisao por 1 para dentro tambem, o que sera feito fora do
# loop ja que ele para quando este se tornar 1.
binario.append(1)

# Ja que apos a divisao sucessiva e necessario inverter o numero, o faremos com a
# lista .
binario.reverse()

# Porem tudo ainda esta dentro da lista entao e so cortar cada parte do numero e 
# junta-las dentro de um numero.
for n in binario:

    # Para poder facilitar e usar certas funcionalidades, convertemos o numero para
    # uma string.
    binario_formatado = binario_formatado + str(n)

binario_formatado = int(binario_formatado)

print(binario_formatado)

#Isso aqui e so para separar os resultados dentro do console.
print("\n------------------------------------------------------------------\n")

# Aqui todo aquele codigo e transformado em uma funcao para reaproveitar o codigo
# e utiliza-lo para converter outros numeros

#Definicao da funcao.
def converterDecimalBinario(numero):

    #Comentario sobre o que a funcao faz.
    """Torna um numero Decimal em um numero Binario"""

    #O mesmo codigo de antes, porem, em funcao.
    binario_partes = []
    binario_numero = ""

    while numero != 1:

        binario_parte = numero % 2 
        binario_partes.append(binario_parte)

        numero = int(numero / 2)

    binario_partes.append(1)

    binario_partes.reverse()

    for n in binario_partes:

        binario_numero = binario_numero + str(n)

    return int(binario_numero)

print(converterDecimalBinario(156))

print("\n------------------------------------------------------------------\n")

# E agora, faremos a conversao de cada numero pedidos durante a aula.
lista_de_numeros = [32, 57, 101, 77]

#Apenas um loop para utilizar os numeros de dentro da lista.
for n in lista_de_numeros:

    print(f"{n} = {converterDecimalBinario(n)}")