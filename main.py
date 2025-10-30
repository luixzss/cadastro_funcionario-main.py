funcionarios = []

def cadastrarfuncionario():
    print("\n-- Cadastro de Funcionário --")
    nome = input("Nome: ").strip()
    while True:
        try:
            salario = float(input("Salário: R$ "))
            break
        except ValueError:
            print("Valor inválido! Digite um número.")
    funcionarios.append({"Nome": nome, "Salario": salario})
    print(f"Funcionário '{nome}' cadastrado com sucesso!")

def listarfuncionarios():
    print("\n-- Lista de Funcionários --")
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
        return
    for f in funcionarios:
        print(f"Nome: {f['Nome']} | Salário: R$ {f['Salario']:.2f}")

def buscarfuncionario():
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
        return
    termo = input("Buscar por nome: ").strip().lower()
    encontrados = [f for f in funcionarios if termo in f["Nome"].lower()]
    if encontrados:
        print("\n-- Resultados da Busca --")
        for f in encontrados:
            print(f"Nome: {f['Nome']} | Salário: R$ {f['Salario']:.2f}")
    else:
        print("Nenhum funcionário encontrado.")

def calcular_media_salarial():
    print("\n-- Média Salarial --")
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
        return
    media = sum(f["Salario"] for f in funcionarios) / len(funcionarios)
    print(f"Média Salarial: R$ {media:.2f}")

# Loop principal
while True:
    print("\n=== Menu ===")
    print("1 - Cadastrar Funcionário")
    print("2 - Listar Funcionários")
    print("3 - Buscar Funcionário")
    print("4 - Calcular Média Salarial")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        cadastrarfuncionario()
    elif opcao == "2":
        listarfuncionarios()
    elif opcao == "3":
        buscarfuncionario()
    elif opcao == "4":
        calcular_media_salarial()
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida, tente novamente.")
