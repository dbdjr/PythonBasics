#
# Exemplo de acesso a uma base de dados SQLite
#

import sqlite3


def manipulaDados(bancoDados, comando):
    conexao = sqlite3.connect(bancoDados)
    cursor = conexao.cursor()
    cursor.execute(comando)
    conexao.commit()
    conexao.close()



def selectData(bancoDados, comando):
    conexao = sqlite3.connect(bancoDados)
    cursor = conexao.cursor()
    cursor.execute(comando)
    linhas = cursor.fetchall()

    for linha in linhas:
        print(linha)

def ManipulacaoDados():
    comandoInsert = "INSERT INTO estados (nome_estado, sigla_estado, nome_capital) VALUES ('Estado Teste', 'EI', 'Teste')"
    pathBD = "D:\\git\\arquivos_de_exercicios_descubra_o_python\\Cap. 06\\teste.db"
    comandoSELECT = "SELECT nome_estado, sigla_estado, nome_capital FROM estados"
    manipulaDados(pathBD, comandoInsert)
    selectData(pathBD, comandoSELECT)


ManipulacaoDados()
