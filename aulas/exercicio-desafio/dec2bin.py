#!/usr/bin/env python 

def dec2bin(num):
  quoc, resto = novo_qr(num)
  i = 0
  bin = resto
  while (quoc > 0):
     i += 1
     quoc, resto = novo_qr(quoc)
     bin = bin + resto * (10 ** i)     
  return bin

def novo_qr(n):
  return (int(n / 2), n % 2)

def main():
  num = input("entre com um número inteiro: ")

  # Converte o número para inteiro
  num = int(num)
  print( dec2bin(num) )

main()
