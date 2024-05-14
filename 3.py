def exibir_menu():
    print("Escolha um exercício para executar:")
    print("1. Exercício 3.1: Mostrar todos os números de 1 a 100")
    print("2. Exercício 3.2: Mostrar todos os números pares de 1 a 100")
    print("3. Exercício 3.3: Mostrar todos os números ímpares de 1 a 100")
    print("4. Exercício 3.4: Somar e mostrar todos os números de 1 a 100")
    print("5. Exercício 3.5: Somar e mostrar todos os números pares de 1 a 100")
    print("0. Sair")

def mostrar_numeros():
    for i in range(1, 101):
        print(i)

def mostrar_pares():
    for i in range(2, 101, 2):
        print(i)

def mostrar_impares():
    for i in range(1, 101, 2):
        print(i)

def somar_numeros():
    soma = sum(range(1, 101))
    print("A soma de todos os números de 1 a 100 é:", soma)

def somar_pares():
    soma = sum(range(2, 101, 2))
    print("A soma de todos os números pares de 1 a 100 é:", soma)

def main():
    while True:
        exibir_menu()
        escolha = input("Digite o número do exercício que deseja executar (ou 0 para sair): ")

        if escolha == "1":
            mostrar_numeros()
        elif escolha == "2":
            mostrar_pares()
        elif escolha == "3":
            mostrar_impares()
        elif escolha == "4":
            somar_numeros()
        elif escolha == "5":
            somar_pares()
        elif escolha == "0":
            print("Saindo...")
            break
        else:
            print("Escolha inválida. Por favor, digite um número de 0 a 5.")

if __name__ == "__main__":
    main()
