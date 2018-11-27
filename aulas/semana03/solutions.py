Escreva um programa chamado citacao.py que imprime uma citação

de sua escolha exatamente 1000 vezes. Você só necessita utilizar a função main().]

# Exercício 4.5
# citacao.py

def main():
    print("Este programa repete uma citação de sua escolha 1000 vezes")
    cit = input("Diga algo memorável: ")
    for c in range(1000):
        print(cit)

# Exercício 4.6
# potencia.py

def main():
    print("Este programa imprime uma tabela de valores de n a 2^n para n = [1-10]")
    for n in range(10):
        print(n, 2 ** n) # <-- Uau. Parece o problema da quantidade de simbolos que podem ser representados a partir da quantidade de bits
