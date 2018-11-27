# Exercício 3.7

def media(n1, n2):
    # Lembre-se de converter um dos termos para float
    return (n1 + n2) / 2

def main():
    print("Este programa calcula a média entre dois números")
    num1 = input("Entre com o primeiro número: ")
    num2 = input("Entre com o segundo número: ")

    # Lembrar de converter os números
    num1 = float(num1)
    num2 = float(num2)

    # Chamada de função média
    m = media(num1, num2)
    print("A média entre esses números é: ", m)

# Chamada da função principal
main()

# Exercício 3.13
# temp.py
def fahrenheit2celsius(tempF):
    return (tempF - 32) * 5.0/9 # <--Um dos termos da divisão deve ser float

def main():
    print("Este programa converte temperaturas em Fahrenheit para Celsius")
    tempF = input("Entre com um valor em Farenheit: ")
    tempF = float(tempF)
    print("O valor da temperatura em Celsius eh: %s " % fahrenheit2celsius(tempF) )

main()


# Exercício 3.14
def fahrenheit2celsius(tempF):
    return (tempF - 32) * 5.0/9 # <--Um dos termos da divisão deve ser float

def fahrenheit2kelvin(tempF):
    return fahrenheit2celsius(tempF) + 273.15

def main():
    print("Este programa converte temperaturas em Fahrenheit para Celsius e Kelvin")
    tempF = input("Entre com um valor em Farenheit: ")
    tempF = float(tempF)
    print("O valor da temperatura em Celsius eh: %s " % fahrenheit2celsius(tempF) )
    print("O valor da temperatura em Kelvin eh: %s " % fahrenheit2kelvin(tempF) )

main()

# Exercício 3.15
# heart.py

# Calcula a quantidade de batimentos a partir da idade
def batimentos(idade):
    return 208 - 0.7 * idade

# Função principal
def main():
    print("Este programa calcula o batimento cardíaco em minutos a partir da idade")
    idade = input("Entre com sua idade: ")

    # este programa considera a idade como fração
    idade = float(idade)
    bat = batimentos(idade)
    print("A quantidade de batimentos por minuto para uma pessoa de %s é %s" % (idade, bat))

main()

# Exercício 3.16
# heron.py

from math import sqrt

def heron(a,b,c):
    p = (a + b + c) / 2
    return sqrt( p * (p - a) * (p - b) * (p - c)  )

def main():
    print("Este programa calcula a área de um triângulo utilizando o teorema de Herão")
    a = input("Entre com o 1o lado do triângulo")
    b = input("Entre com o 2o lado do triângulo")
    c = input("Entre com o 3o lado do triângulo")

    # Converte os valores para float
    a, b, c = float(a), float(b), float(c)
    area = heron(a,b,c)
    print("A área do triângulo é %s" % (area) )

main()

# Exercício 3.17
# interest.py

def saldo(principal, juros, tempo):
    return principal * (1 + juros) ** tempo

def main():
    print("Este programa calcula o novo saldo a partir do juros e tempo")
    p = input("Entre com o valor do principal: ")
    j = input("Entre com a taxa de juros: ")
    t = input("Entre com o número de anos: ")

    p, j, t = float(p), float(j), float(t)

    novo_saldo = saldo(p, j, t)
    print("O novo saldo em %s anos será de %s " % (t, novo_saldo) )

main()
