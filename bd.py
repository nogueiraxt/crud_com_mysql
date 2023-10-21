# pymysql - biblioteca para conectar com o banco de dados

import pymysql.cursors

try:
    # connection = > abre a conexão com o banco de dados
    conexao = pymysql.connect(host='localhost',
                              user='root',
                              password='',
                              database='escola',
                              port=3306,
                              cursorclass=pymysql.cursors.DictCursor)
    print("Conexão estabelecida com sucesso!")
except Exception as erro:
    print(f"Erro ao conectar com o banco: {erro}")

# cursor
cursor = conexao.cursor()


def select():
    try:
        sql = "SELECT * FROM alunos"
        cursor.execute(sql)
        # fetch() => sepadando os alunos da tabela
        alunos = cursor.fetchall()
        for aluno in alunos:
            print(f'Nome: {aluno["nome"]} - Nota: {aluno["nota"]}')
    except Exception as error:
        print(f"Erro ao buscar: {error}")


def insert(nome, idade, nota):
    try:
        sql = "INSERT INTO alunos (nome, idade, nota)" \
              "VALUE (%s, %s, %s)"  # feito com %s para não ter invasão de SQL INJECT
        cursor.execute(sql, (nome, idade, nota))
        conexao.commit()
        print("Dados cadastrados com sucesso!!")
    except Exception as error:
        print(f"Erro ao cadastrar: {error}")


# insert("Nogueira", 31, 10.0)
#
# select()


def update(nome, idade, nota, matricula):
    try:
        if alunoExiste(matricula):
            sql = "UPDATE alunos SET nome = %s, idade = %s, nota = %s WHERE matricula = %s"
            cursor.execute(sql, (nome, idade, nota, matricula))
            conexao.commit()
            print("Dados alterados com sucesso!")
        else:
            print("Aluno não encontrado!")
    except Exception as error:
        print(f"Erro ao atualizar os dados: {error}")


# update("Nogueira Pinheiro", 30, 9.5, 3)


def delete(matricula):
    try:
        if alunoExiste(matricula):
            sql = "DELETE from alunos where matricula=%s"
            cursor.execute(sql, matricula)
            conexao.commit()
            print("Aluno deletado com sucesso!")
        else:
            print("Aluno não existe!")
    except Exception as error:
        print(f"Erro ao deletar aluno: {error}")


def alunoExiste(matricula):
    try:
        sql = "SELECT * FROM alunos WHERE matricula = %s"
        cursor.execute(sql, matricula)
        qtd = len(cursor.fetchall())
        if qtd == 1:
            print('ok')
            return True
        else:
            return False
    except Exception as error:
        print(f"Erro ao consultar dados {error}")
#
# update("Nogueira Pinheiro", 30, 9.5, 5)
# select()
print(alunoExiste(3))