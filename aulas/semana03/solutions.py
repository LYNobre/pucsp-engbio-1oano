Escreva um programa chamado citacao.py que imprime uma citação

de sua escolha exatamente 1000 vezes. Você só necessita utilizar a função main().]

# Exercício 4.5
# citacao.py

def main():
    print("Este programa repete uma citação de sua escolha 1000 vezes")
    cit = input("Diga algo memorável: ")
    for c in range(1000):
        print(cit)



def main():
    print("Este programa imprime uma tabela de valores de n a 2^n para n = [1-10]")
    for n in range(10):
        print(n, 2 ** n)


# tabela.py
from math import log
def main():
    for n in range(10,200,10):
        print("n = %s; log(n) = %s; nlog(n) = %s; n^2 = %s; 2n = %s " % (n, log(n), n * log(n), n ** 2, 2 * n) )


4.7 Escreva um programa chamado tabela.py que imprime uma
tabela de valores de n, logn, nlogn, n2, e 2n para n=10,20,....,200.
O log é uma função do módulo math. Você só necessita utilizar a função main().
A função nlogn cresce mais que n ou n2?
Como você descreveria o crescimento de 2n? E de logn?


Escreva um programa tabela_circulo.pyque
imprime uma tabela para as áreas dos
círculos de raio r=1,2,...,10. Use uma função de área
