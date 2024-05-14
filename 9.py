class SaldoInsuficienteError(Exception):
    pass

class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteError("Saldo insuficiente para realizar o saque.")
        self.saldo -= valor

def exercicio_9_1():
    try:
        num1 = int(input("Digite o primeiro número inteiro: "))
        num2 = int(input("Digite o segundo número inteiro: "))
        resultado = num1 / num2
        print(f"O resultado da divisão é: {resultado}")
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")

def exercicio_9_2():
    def calcular_media(numeros):
        try:
            return sum(numeros) / len(numeros)
        except ZeroDivisionError:
            print("Erro: Lista vazia.")
        except TypeError:
            print("Erro: A lista contém valores não numéricos.")

    lista = [1, 2, 3, 4, 5]
    print("A média dos números na lista é:", calcular_media(lista))

def exercicio_9_3():
    def calculadora():
        try:
            num1 = float(input("Digite o primeiro número: "))
            operacao = input("Digite a operação (+, -, *, /): ")
            num2 = float(input("Digite o segundo número: "))
            if operacao == '+':
                print("Resultado:", num1 + num2)
            elif operacao == '-':
                print("Resultado:", num1 - num2)
            elif operacao == '*':
                print("Resultado:", num1 * num2)
            elif operacao == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Erro: Divisão por zero não é permitida.")
                print("Resultado:", num1 / num2)
            else:
                print("Erro: Operação inválida.")
        except ValueError:
            print("Erro: Valor inválido.")
        except ZeroDivisionError as e:
            print(e)

def exercicio_9_4():
    conta = ContaBancaria(1000)
    try:
        conta.sacar(1500)
    except SaldoInsuficienteError as e:
        print(e)

def exercicio_9_5():
    def ler_arquivo(nome_arquivo):
        try:
            with open(nome_arquivo, 'r') as arquivo:
                conteudo = arquivo.read()
                print(conteudo)
        except FileNotFoundError:
            print("Erro: Arquivo não encontrado.")
        except PermissionError:
            print("Erro: Sem permissão para ler o arquivo.")

# Menu de seleção dos exercícios
while True:
    print("\nEscolha um exercício para executar:")
    print("1. Exercício 9.1 - Divisão de números inteiros")
    print("2. Exercício 9.2 - Média aritmética de uma lista")
    print("3. Exercício 9.3 - Calculadora básica")
    print("4. Exercício 9.4 - Manipulação de conta bancária")
    print("5. Exercício 9.5 - Leitura de arquivo de texto")
    print("0. Sair")

    opcao = input("Digite o número do exercício (0-5): ")

    if opcao == '1':
        exercicio_9_1()
    elif opcao == '2':
        exercicio_9_2()
    elif opcao == '3':
        exercicio_9_3()
    elif opcao == '4':
        exercicio_9_4()
    elif opcao == '5':
        exercicio_9_5()
    elif opcao == '0':
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
