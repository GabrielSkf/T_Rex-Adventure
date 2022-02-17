# Esse programa foi criado para armazenar a pontuação obtida na tela Game
import sqlite3
# Aqui estamos criando uma classe que recebera os valores para a criação das linhas e colunas do banco de dados
class Pont:
    def __init__(self, id, nome, email, rank):
        self.id = id
        self.nome = nome
        self.email = email
        self.rank = rank

#Aqui estamos armazenando os dados recebidos
class BancodeDadosPoints:
    def novoPlayer(self,novo_play):
        conn  =sqlite3.connect('PONTUACAO.db')
        cursor = conn.cursor()
        cursor.execute("""
                       INSERT INTO Pont(id, nome, email, rank)
                       VALUES(?,?,?,?)""",
                       (novo_play.id, novo_play.nome, novo_play.email, novo_play.rank)
        )
        conn.commit()
        conn.close()
#Aqui estamos analisando os pontos
    def listarPont(self):
        conn  =sqlite3.connect('PONTUACAO.db')
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT*
                       FROM    Pont
                       """
        )
        registro = list()
        for reg in cursor.fetchall():
            registro.append(Pont(reg[0],reg[1],reg[2], reg[3]))
        conn.close()
        # Aqui estamos separando para que o valor mais recente seja armazenado com o jogador mais recente
        if registro != []:
            return registro
        else:
            return None
    def pega_ponto(self):
        return self.listarPont()[-1].rank
            
