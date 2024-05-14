# Exercício 5.1
def soma(a, b):
    return a + b

# Exercício 5.2
def par_impar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

# Exercício 5.3
def imprimir_valores(inteiro, real, texto):
    print("Número inteiro:", inteiro)
    print("Número real:", real)
    print("Texto:", texto)

# Exercício 5.4
def mensagem(nome, idade):
    print("Nome:", nome)
    print("Idade:", idade)

# Exercício 5.6
def adicionar(lista):
    lista.append(6)


while True:
    print("\nMenu:")
    print("1. Exercício 5.1")
    print("2. Exercício 5.2")
    print("3. Exercício 5.3")
    print("4. Exercício 5.4")
    print("5. Exercício 5.6")
    print("0. Sair")

    escolha = input("Escolha o número do exercício ou 0 para sair: ")

    if escolha == '1':
        print("Resultado do Exercício 5.1:", soma(3, 5))
    elif escolha == '2':
        print("Resultado do Exercício 5.2:", par_impar(7))
    elif escolha == '3':
        imprimir_valores(10, 3.14, "Python")
    elif escolha == '4':
        mensagem(nome="Maria", idade=25)
    elif escolha == '5':
        idades = [20, 30, 40, 50, 60]
        adicionar(idades)
        print("Lista de idades após adicionar elemento:", idades)
    elif escolha == '0':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Escolha novamente.")
