
#Construir um programa que apresente a soma dos cem primeiros números naturais (1 + 2 + 3 +...+ 98 + 99 + 100).




print("Soma dos cem primeiros números inteiros")

soma = 0

for contador in range(100):
    contador = contador + 1
    soma = soma + contador

print(soma, contador)