import os

def exibir_menu():
    print("Escolha o exercício que deseja executar:")
    print("1. Exercício 7.1 - Exibir conteúdo de um arquivo")
    print("2. Exercício 7.3 - Inverter conteúdo de cada linha de um arquivo")
    print("3. Exercício 7.5 - Excluir um arquivo")
    print("4. Exercício 7.6 - Copiar arquivo com extensão modificada")
    print("5. Exercício 7.10 - Criar diretório, arquivos e compactar")

def exercicio_7_1():
    nome_arquivo = input("Digite o nome do arquivo: ")
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            print("Conteúdo do arquivo:")
            print(conteudo)
    except FileNotFoundError:
        print("Arquivo não encontrado.")

def exercicio_7_3():
    nome_arquivo = input("Digite o nome do arquivo de origem: ")
    nome_arquivo_saida = input("Digite o nome do arquivo de saída: ")
    try:
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            linhas_invertidas = [linha[::-1] for linha in linhas]

        with open(nome_arquivo_saida, 'w') as arquivo_saida:
            arquivo_saida.writelines(linhas_invertidas)
        
        print(f"Conteúdo invertido salvo em {nome_arquivo_saida}.")
    except FileNotFoundError:
        print("Arquivo não encontrado.")

def exercicio_7_5():
    nome_arquivo = input("Digite o nome do arquivo que deseja excluir: ")
    try:
        os.remove(nome_arquivo)
        print(f"Arquivo {nome_arquivo} excluído com sucesso.")
    except FileNotFoundError:
        print("Arquivo não encontrado.")

def exercicio_7_6():
    nome_arquivo_origem = input("Digite o nome do arquivo de origem: ")
    nome_arquivo_destino = input("Digite o nome do arquivo de destino (com extensão .cópia): ")
    try:
        with open(nome_arquivo_origem, 'r') as arquivo_origem:
            conteudo = arquivo_origem.read()
        
        with open(nome_arquivo_destino, 'w') as arquivo_destino:
            arquivo_destino.write(conteudo)
        
        print(f"Arquivo copiado com sucesso para {nome_arquivo_destino}.")
    except FileNotFoundError:
        print("Arquivo de origem não encontrado.")

def exercicio_7_10():
    import zipfile
    
    nome_dir = "Textos"
    nome_arquivo_zip = "Textos.zip"
    
    # Criando diretório e arquivos
    os.makedirs(nome_dir, exist_ok=True)
    for i in range(1, 4):
        with open(f"{nome_dir}/arquivo{i}.txt", 'w') as arquivo:
            arquivo.write("Python Essencial")
    
    # Compactando o diretório
    with zipfile.ZipFile(nome_arquivo_zip, 'w') as zipf:
        for pasta_raiz, _, arquivos in os.walk(nome_dir):
            for arquivo in arquivos:
                caminho_completo = os.path.join(pasta_raiz, arquivo)
                zipf.write(caminho_completo, os.path.relpath(caminho_completo, nome_dir))
    
    print(f"Diretório '{nome_dir}' e arquivos criados e compactados em '{nome_arquivo_zip}'.")

def main():
    while True:
        exibir_menu()
        opcao = input("Digite o número do exercício que deseja executar (ou '0' para sair): ")
        if opcao == '0':
            print("Encerrando o programa.")
            break
        elif opcao == '1':
            exercicio_7_1()
        elif opcao == '2':
            exercicio_7_3()
        elif opcao == '3':
            exercicio_7_5()
        elif opcao == '4':
            exercicio_7_6()
        elif opcao == '5':
            exercicio_7_10()
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
