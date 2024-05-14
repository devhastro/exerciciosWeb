import math

def calcular_potencia():
    base = float(input("Digite o primeiro número (base): "))
    expoente = float(input("Digite o segundo número (expoente): "))
    resultado = base ** expoente
    print(f"O resultado de {base} elevado a {expoente} é: {resultado}")

def calcular_raiz_quadrada():
    numero = float(input("Digite um número para calcular a raiz quadrada: "))
    raiz = math.sqrt(numero)
    print(f"A raiz quadrada de {numero:.2f} é: {raiz:.2f}")

def calcular_trigonometria():
    angulo_graus = float(input("Digite um ângulo em graus: "))
    angulo_radianos = math.radians(angulo_graus)
    seno = math.sin(angulo_radianos)
    cosseno = math.cos(angulo_radianos)
    tangente = math.tan(angulo_radianos)
    print(f"Seno: {seno:.2f}, Cosseno: {cosseno:.2f}, Tangente: {tangente:.2f}")

def calcular_logaritmo():
    numero = float(input("Digite um número para calcular o logaritmo natural: "))
    logaritmo = math.log(numero)
    print(f"O logaritmo natural de {numero} é: {logaritmo:.2f}")

def calcular_fatorial():
    numero = int(input("Digite um número para calcular o fatorial: "))
    fatorial = math.factorial(numero)
    print(f"O fatorial de {numero} é: {fatorial}")

def main():
    while True:
        print("\nMenu:")
        print("1. Exercício 4.1 - Calcular potência")
        print("2. Exercício 4.2 - Calcular raiz quadrada")
        print("3. Exercício 4.3 - Calcular seno, cosseno e tangente")
        print("4. Exercício 4.4 - Calcular logaritmo natural")
        print("5. Exercício 4.5 - Calcular fatorial")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            calcular_potencia()
        elif opcao == "2":
            calcular_raiz_quadrada()
        elif opcao == "3":
            calcular_trigonometria()
        elif opcao == "4":
            calcular_logaritmo()
        elif opcao == "5":
            calcular_fatorial()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
