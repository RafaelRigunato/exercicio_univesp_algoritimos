#Realizar a leitura dos valores de quatro notas escolares bimestrais de um aluno representadas pelas variáveis N1, N2, N3 e N4. 
#Calcular a média aritmética (variável MD) desse aluno e apresentar a mensagem “Aluno Aprovado com média” se a média obtida for maior ou igual a 5;
 #caso contrário, apresentar a mensagem “Aluno Reprovado com média”. Informar também, após a apresentação das mensagens, o valor da média obtida pelo aluno.




def calculate_average (n1, n2, n3, n4):
    nota = (n1 + n2 + n3 + n4) / 4
    return nota



print("Média dos alunos")

n1 = int(input("Nota 1 "))
n2 = int(input("Nota 2 "))
n3 = int(input("Nota 3 "))
n4 = int(input("Nota 4 "))

media = calculate_average(n1, n2, n3, n4)

if media >= 5:
    print("Aluno aprovado com média ", media)
else : print("Aluno Reprovado com média", media)



