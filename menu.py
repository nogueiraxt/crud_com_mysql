import bd

while True:
    print("--Bem vido ao menu--")
    print("1- Adicionar Aluno")
    print("2- Editar Aluno")
    print("3- Deletar Aluno")
    print("4- Listar todos os Aluno")
    print("5- SAIR")
    opcao = input("Selecione uma opção: ")

    if opcao == "1":
        nome = input("Digite o Nome do aluno: ")
        idade = int(input("Digite a idade do aluno: "))
        nota = float(input("Digite a nota do aluno: "))
        bd.insert(nome, idade, nota)

    elif opcao == "2":
        nome = input("Digite o Nome do aluno: ")
        idade = int(input("Digite a idade do aluno: "))
        nota = float(input("Digite a nota do aluno: "))
        matricula = int(input("Digite a matricula do aluno: "))
        bd.update(nome, idade, nota, matricula)

    elif opcao == "3":
        matricula = int(input("Digite a matricula do aluno: "))
        bd.delete(matricula)

    elif opcao == "4":
        bd.select()

    elif opcao == "5":
        break

    else:
        print("Opção invalida!")
