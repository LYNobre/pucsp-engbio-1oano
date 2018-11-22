#!/usr/bin/env python

n = int(input("numero?"))

quoc = n
resto = quoc % 2
binario = str(resto)

while (quoc > 0):
    quoc = int(quoc / 2)
    resto = quoc % 2
    binario = str(resto) + binario
    
print(binario)
