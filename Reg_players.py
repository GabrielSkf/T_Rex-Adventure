# Programa responsável pelo armazenamento de dados dos jogadores.
import sqlite3
#Essa classe armazena os dados obtidos na tela de SignUp, assim como a pontuação obtida no jogo
class Rank:
    def __init__(self, id, nome, email):
        self.nome = nome
        self.id = id
        self.email = email
    
class BancodeDadosPlayers:
    def novoPlayer(self,novo_play):
        conn  =sqlite3.connect('TABELA_RANK.db')
        cursor = conn.cursor()
        cursor.execute("""
                       INSERT INTO rank(id, nome, email)
                       VALUES(?,?,?)""",
                       (novo_play.id, novo_play.nome, novo_play.email)
        )
        conn.commit()
        conn.close()
    
    def listarPlayersRank(self):
        conn  =sqlite3.connect('TABELA_RANK.db')
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT*
                       FROM rank
                       """)
        registro = list()
        for reg in cursor.fetchall():
            registro.append(Rank(reg[0],reg[1], reg[2]))
        conn.close()
        # Aqui estamos separando para que o valor mais recente seja armazenado com o jogador mais recente
        if registro != []:
            return registro
        else:
            return None
    def peganome(self):
        return self.listarPlayersRank()[-1].nome
    def pegaemail(self):
        return self.listarPlayersRank()[-1].email
        