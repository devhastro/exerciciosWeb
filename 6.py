import random

# Exercício 6.1
def ex_6_1():
    sqrt_list = [round((x ** 0.5), 2) for x in range(0, 21) if x % 2 == 0]
    print("Raízes quadradas dos números pares de 0 a 20:", sqrt_list)

# Exercício 6.6
def ex_6_6():
    square_roots_dict = {num: round(num ** 0.5, 2) for num in range(1, 11)}
    print("Dicionário com as raízes quadradas de 1 a 10:", square_roots_dict)

# Exercício 6.15
def ex_6_15():
    num_list = [12, 5, 8, 21, 17, 9, 25, 6, 13, 30]
    reference_num = 10
    above_ref_list = [num for num in num_list if num > reference_num]
    print("Itens da lista original maiores que", reference_num, ":", above_ref_list)

# Exercício 6.23
def ex_6_23():
    qa_dict = {
        "Qual é a capital do Brasil?": "Brasília",
        "Quem escreveu 'Dom Quixote'?": "Miguel de Cervantes",
        "Quantos elementos químicos a tabela periódica tem?": "118"
    }
    question = random.choice(list(qa_dict.keys()))
    answer = input(question + "\nSua resposta: ")
    if answer.lower() == qa_dict[question].lower():
        print("Resposta correta!")
    else:
        print("Resposta incorreta.")

# Exercício 6.24
def ex_6_24():
    choices = ["pedra", "papel", "tesoura"]
    user_choice = input("Escolha pedra, papel ou tesoura: ").lower()
    comp_choice = random.choice(choices)
    print("Computador escolheu:", comp_choice)
    if user_choice == comp_choice:
        print("Empate!")
    elif (user_choice == "pedra" and comp_choice == "tesoura") or \
         (user_choice == "papel" and comp_choice == "pedra") or \
         (user_choice == "tesoura" and comp_choice == "papel"):
        print("Você venceu!")
    else:
        print("Computador venceu!")

# Menu de seleção
while True:
    print("\nEscolha um exercício para executar:")
    print("1. Exercício 6.1 - " )
    print("2. Exercício 6.6 - ")
    print("3. Exercício 6.15 - ")
    print("4. Exercício 6.23 - ")
    print("5. Exercício 6.24 - ")
    print("0. Sair")
    choice = input("Digite o número do exercício ou 0 para sair: ")
    if choice == "1":
        ex_6_1()
    elif choice == "2":
        ex_6_6()
    elif choice == "3":
        ex_6_15()
    elif choice == "4":
        ex_6_23()
    elif choice == "5":
        ex_6_24()
    elif choice == "0":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Escolha novamente.")
