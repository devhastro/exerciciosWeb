import random

def verificar_par_impar():
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")

def verificar_positivo_negativo_zero():
    numero = float(input("Digite um número: "))
    if numero > 0:
        print("O número é positivo.")
    elif numero < 0:
        print("O número é negativo.")
    else:
        print("O número é zero.")

def verificar_vogal_consoante():
    letra = input("Digite uma letra: ").lower()
    if letra in 'aeiou':
        print("É uma vogal.")
    else:
        print("É uma consoante.")

def verificar_ano_bissexto():
    ano = int(input("Digite um ano: "))
    if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        print("O ano é bissexto.")
    else:
        print("O ano não é bissexto.")

def verificar_maioridade():
    idade = int(input("Digite sua idade: "))
    if idade >= 18:
        print("Você é maior de idade.")
    else:
        print("Você é menor de idade.")

def menu():
    print("1. Exercício 2.1 - Verificar se um número é par ou ímpar")
    print("2. Exercício 2.2 - Verificar se um número é positivo, negativo ou zero")
    print("3. Exercício 2.3 - Verificar se uma letra é vogal ou consoante")
    print("4. Exercício 2.4 - Verificar se um ano é bissexto")
    print("5. Exercício 2.5 - Verificar se uma pessoa é maior de idade")
    opcao = int(input("Escolha uma opção (1-5): "))
    if opcao == 1:
        verificar_par_impar()
    elif opcao == 2:
        verificar_positivo_negativo_zero()
    elif opcao == 3:
        verificar_vogal_consoante()
    elif opcao == 4:
        verificar_ano_bissexto()
    elif opcao == 5:
        verificar_maioridade()
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    menu()
