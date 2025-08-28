#Ex B- 1 Faça um programa, utilizando while, que mostre na tela os números de 0 a 100.
'''print("---- PROGRAMa----")
contador = 0 

while contador <= 100:
    print(contador)
    contador+=1'''

#Ex b- 2 Faça um programa, utilizando while, que mostre na tela de 0 até N, em que N é o limite inserido pelo usuário.
'''print("---- PROGRAMa----")
contador = 0
num = int(input("Digite um numero: "))

while contador <= num:
    print(contador)
    contador +=1'''

#Ex B-Faça um programa, utilizando while, que permita o usuário fazer contas de adição enquanto quiser.
'''print("---- PROGRAMa----")
contador = 0

while 1:
    num1 = int(input("Digite um numero: "))
    num2 = int(input("Digite um numero: "))
    print(f"Resultado da soma: {num1 + num2}")

    seguir = input("Digite 'S' para continuar ou 'F' para finalizar: ").lower()
    if seguir == "f":
        break'''

#Ex D- A série de Fibonacci é formada pela sequência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.
'''print("---- PROGRAMa----")

lista = [0, 1] #tem haver com as posições "penúltma e última" dentro da lista.... 
for i in range (2,16): #tem haver com a quantidade de vezes que vai se repetir... 
    soma = lista[i-1] + lista[i-2] # soma o penúltima e o ultimo da lista, que inicalmente, será [0] [1] 0 + 1 = 1...
    lista.append(soma) #pega a soma pelo .append(soma) e coloca na lista o resultado. ate que acabe as 15 repetiçõs. 

    print(lista)
    '''

#Ex D-Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
'''print("---- PROGRAMa----")

numeros = [1,2,3,4,5,7,8,9,10]

maior = max(numeros) 
menor = min(numeros) 
 
soma = maior + menor 
print(f"O maior numeroe e: {maior}\nO menor numero e: {menor}\nA soma dos numeros e: {soma}")'''

#Ex D- Altere o programa anterior para que ele aceite apenas números entre 0 e 1000
'''print("---- PROGRAMa----")
lista_numeros = []
numero = 0

while numero <= 1000:
    numero = int(input("Digite um nunmero para add à lista: "))

    if numero <= 1000:
        lista_numeros.append(numero)

    else:
        print("Numero invalido")'''

#Ex D- Faça um programa que leia e valide as seguintes informações:
'''print("---- PROGRAMa----")
 #1. Nome: maior que 3 caracteres;
 #2. Idade: entre 0 e 150;
 #3. Salário: maior que zero;
 #4. Sexo: 'f' ou 'm';
 #5. Estado Civil: 's', 'c', 'v', 'd';
 #5. Use a função len(string) para saber o tamanho de um texto (número de caracteres)


while True:
    nome = input("Digite seu nome: ")
    if len(nome) > 3:
        break
    else:
        print("Nome deve ter mais que 3 caracteres.")

while True:

    idade = int(input("Digite sua idade: "))
    if idade > 0 and idade <= 150:
        break
    else:
        print("Idade deve ser entre 1 e 150.")
        print("Por favor, digite um número válido para idade.")

while True:
        salario = float(input("Digite seu salario: R$ "))
        if salario > 0:
            break
        else:
            print("Salário deve ser maior que zero.")
            print("Por favor, digite um valor válido para salário.")

while True:
    sexo = input("Digite seu sexo - 'M' ou 'F': ").lower()
    if sexo in ['m', 'f']:
        break
    else:
        print("Sexo deve ser 'M' ou 'F'.")

while True:
    estado_civil = input("Estado Civil: 's', 'c', 'v', 'd': ").lower()
    if estado_civil in ['s', 'c', 'v', 'd']:
        break
    else:
        print("Estado civil deve ser 's', 'c', 'v' ou 'd'.")


print(f"---DADOS DA PESQUISA--- \nNome:{nome}\nIdade:{idade}\nSalario:{salario}\nSexo:{sexo}\nEstado Civil:{estado_civil}")'''


#Ex D- Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é  aquele que é divisível somente por ele mesmo e por 1.
print("---- PROGRAMa----")
while True:
    num = int(input("Digite um número inteiro: "))

    if num <= 1:
        print("Numero invalido! Digite outro numero.")
        continue  

    quant = 0  
    contador = 0

    for contador in range(1, num + 1):
        if num % contador == 0:
            quant += 1

    if quant == 2:
        print(f"{num} e primo!")
    else:
        print(f"{num} nao e primo")

    continuar = input("Deseja continuar? 'S' para sim ou 'N' para nao: ").upper()
    if continuar != "S":
        break  

   

