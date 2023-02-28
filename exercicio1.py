#Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit. 
#A fórmula de conversão é F ← C * 9 / 5 + 32, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
 
def convert (c):
    fahren = (c * 9/5) + 32
    print("Seu valor em Fahren é:", fahren)
    return 0 

print("Conversor de Graus ")

celcius = int(input("Digite o Grau em Celcius "))
convert(celcius)

