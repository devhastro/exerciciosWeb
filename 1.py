import math

def exercicio_1_3():
    print("=== Exercício 1.3: Média Aritmética de Três Números ===")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o terceiro número: "))
    media = (num1 + num2 + num3) / 3
    print("A média aritmética dos três números é:", media)

def exercicio_1_5():
    print("=== Exercício 1.5: Soma do Dobro de Três Números ===")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o terceiro número: "))
    soma_dobro = 2*num1 + 2*num2 + 2*num3
    print("A soma do dobro dos três números é:", soma_dobro)

def exercicio_1_7():
    print("=== Exercício 1.7: Inteiros Anterior e Posterior ===")
    num = int(input("Digite um número inteiro: "))
    anterior = num - 1
    posterior = num + 1
    print("O número inteiro anterior a", num, "é", anterior)
    print("O número inteiro posterior a", num, "é", posterior)

def exercicio_1_11():
    print("=== Exercício 1.11: Área e Comprimento de um Círculo ===")
    raio = float(input("Digite o raio do círculo: "))
    area = math.pi * raio**2
    comprimento = 2 * math.pi * raio
    print("A área do círculo é:", area)
    print("O comprimento do círculo é:", comprimento)

def exercicio_1_20():
    print("=== Exercício 1.20: Velocidade Média de um Objeto ===")
    distancia = float(input("Digite a distância percorrida (em metros): "))
    tempo = float(input("Digite o tempo gasto (em segundos): "))
    velocidade_media = distancia / tempo
    print("A velocidade média do objeto é:", velocidade_media, "m/s")

def main():
    while True:
        print("\n=== Menu de Exercícios ===")
        print("1. Exercício 1.3")
        print("2. Exercício 1.5")
        print("3. Exercício 1.7")
        print("4. Exercício 1.11")
        print("5. Exercício 1.20")
        print("0. Sair")
        escolha = input("Escolha o número do exercício que deseja executar (ou 0 para sair): ")
        
        if escolha == '1':
            exercicio_1_3()
        elif escolha == '2':
            exercicio_1_5()
        elif escolha == '3':
            exercicio_1_7()
        elif escolha == '4':
            exercicio_1_11()
        elif escolha == '5':
            exercicio_1_20()
        elif escolha == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
