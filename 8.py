# Exercício 8.3: Classe ContaBancaria
class ContaBancaria:
    def __init__(self):
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor
        print("Depósito de R$%.2f realizado." % valor)

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print("Saque de R$%.2f realizado." % valor)
        else:
            print("Saldo insuficiente.")

    def exibir_saldo(self):
        print("Saldo atual: R$%.2f" % self.saldo)

# Exercício 8.7: Classes Pessoa e Funcionario
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_dados(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)

class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def mostrar_dados(self):
        super().mostrar_dados()
        print("Salário:", self.salario)

# Exercício 8.10: Classes Pessoa e Cliente
class Cliente(Pessoa):
    def __init__(self, nome, idade, endereco):
        super().__init__(nome, idade)
        self.endereco = endereco

    def mostrar_dados(self):
        super().mostrar_dados()
        print("Endereço:", self.endereco)

# Exercício 8.13: Classes ContaBancaria e ContaPoupanca
class ContaPoupanca(ContaBancaria):
    def __init__(self, taxa_juros):
        super().__init__()
        self.taxa_juros = taxa_juros / 100

    def rendimento(self, meses):
        rendimento = self.saldo * (self.taxa_juros / 12) * meses
        self.saldo += rendimento
        print("Rendimento após %d meses: R$%.2f" % (meses, rendimento))

# Exercício 8.19: Classes Livro e LivroDeBiblioteca
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def mostrar_dados(self):
        print("Título:", self.titulo)
        print("Autor:", self.autor)

class LivroDeBiblioteca(Livro):
    def __init__(self, titulo, autor, codigo):
        super().__init__(titulo, autor)
        self.codigo = codigo

    def mostrar_dados(self):
        super().mostrar_dados()
        print("Código:", self.codigo)

# Menu de seleção
def menu():
    print("\nEscolha o exercício que deseja executar:")
    print("1. Exercício 8.3 - Conta Bancária")
    print("2. Exercício 8.7 - Pessoa e Funcionário")
    print("3. Exercício 8.10 - Pessoa e Cliente")
    print("4. Exercício 8.13 - Conta Bancária e Conta Poupança")
    print("5. Exercício 8.19 - Livro e Livro de Biblioteca")
    print("0. Sair")

def main():
    opcao = None
    while opcao != "0":
        menu()
        opcao = input("Digite o número do exercício ou 0 para sair: ")
        if opcao == "1":
            print("\nExecutando Exercício 8.3 - Conta Bancária")
            conta = ContaBancaria()
            conta.depositar(1000)
            conta.sacar(500)
            conta.exibir_saldo()
        elif opcao == "2":
            print("\nExecutando Exercício 8.7 - Pessoa e Funcionário")
            pessoa1 = Pessoa("João", 30)
            funcionario1 = Funcionario("Maria", 25, 2500)
            pessoa1.mostrar_dados()
            funcionario1.mostrar_dados()
        elif opcao == "3":
            print("\nExecutando Exercício 8.10 - Pessoa e Cliente")
            pessoa2 = Pessoa("Ana", 35)
            cliente1 = Cliente("Carlos", 40, "Rua XYZ, 123")
            pessoa2.mostrar_dados()
            cliente1.mostrar_dados()
        elif opcao == "4":
            print("\nExecutando Exercício 8.13 - Conta Bancária e Conta Poupança")
            conta_poupanca = ContaPoupanca(0.5)
            conta_poupanca.depositar(1000)
            conta_poupanca.rendimento(12)
            conta_poupanca.exibir_saldo()
        elif opcao == "5":
            print("\nExecutando Exercício 8.19 - Livro e Livro de Biblioteca")
            livro1 = Livro("Dom Quixote", "Miguel de Cervantes")
            livro_biblioteca = LivroDeBiblioteca("Harry Potter", "J.K. Rowling", "ABC123")
            livro1.mostrar_dados()
            livro_biblioteca.mostrar_dados()
        elif opcao == "0":
            print("Saindo...")
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()
