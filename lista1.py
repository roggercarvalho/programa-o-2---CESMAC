#Ex - 1  Faça um Programa que peça um número inteiro e determine se ele é par ou ímpar. Dica: utilize o operador módulo (resto da divisão[%]).
'''print("---- PROGRAMa----")
num = int(input("digite um numero: "))

if(num % 2 == 0):
    print(f"O numero {num} e par")
else: 
    print(f"O numero {num} e impar")'''


#Ex- 2 Faça um Programa que peça dois números e imprima o maior deles.
'''print("---- PROGRAMa----")

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))

if (num1 > num2):
    print(f"Num1 {num1} e maio")
elif(num1 < num2):
    print(f"Num2 {num2} e maior")
else:
    print(f"{num1} e {num2} sao iguais!")'''


#Ex- 3 Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
''''print("----- PROGRAMa-----")
vogais = ["a", "e", "i", "o", "u"]

letra = input("Digite uma letras: ").lower()

if letra in vogais:
        print(f"A letra {letra} e uma vogal")
else:
        print("A letra é uma coonsoante.)'''

#Ex- 4 Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#a. A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#b. A mensagem "Reprovado", se a média for menor do que sete;
#c. A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''print("----- PROGRAMa-----")

media = 0
n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))

media = (n1 + n2) / 2

if(media >= 7 and media <=9 ):
    print(f"APROVADO - MEDIA {media}")
elif(media< 7):
    print(f"REPROVADO")
elif(media == 10):
    print("PARABENS FDP. TU PASSOU COM NOTA MAXIMA!")'''

#Ex- 5  Faça um Programa que leia três números e mostre o maior deles.'print("----- PROGRAMa-----")
'''print("----- PROGRAMa-----")
lista_numeros = []
contador = 0

for contador in range(3):
    num = int(input("Digite um numero: "))
    lista_numeros.append(num)

maior = max(lista_numeros)

print(f"O maior numero e: {maior}")'''

#Ex-6  Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

'''print("----- PROGRAMa-----")
print("M= matutino\nV= vespertino\nN= noturno\n")
turno = input("Em qual turno você estuda: ").lower

match turno: 
    case "m":
        print("Bom dia!")
    case "v":
        print("Boa tarde!")
    case "n":
        print("Boa noite!")
    case _:
        print("perdeu play boy!")
'''
    
#Ex- 7 Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# a. "Telefonou para a vítima?"
# b. "Esteve no local do crime?"
# c. "Mora perto da vítima?"
# d. "Devia para a vítima?"
# e. "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a A pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

'''contador = 0
print("----- PROGRAMa-----")
perguntas = [
    "Telefonou para a vítima? 'S' ou 'N' ",
    "Esteve no local do crime? 'S' ou 'N' ",
    "Mora perto da vítima? 'S' ou 'N'",
    "Devia para a vítima? 'S' ou 'N'",
    "Já trabalhou com a vítima? 'S' ou 'N'"
]
for pergunta in perguntas:
    resposta = input(pergunta).lower()
    if resposta == "s":
        contador += 1

if contador == 2:
    print("Suspeito?")

if contador ==3 or contador ==4:
    print("Cumplice")

if contador == 5:
    print("Assasino")

else: 
    print("Inocente")'''
    









