import sqlite3

class Missao():
    def __init__(self):
        self.create_table()

    def abrirConexao(self):
        try:
            self.connection = sqlite3.connect('database.db')
        except sqlite3.Error as error:
            print("Falha ao se conectar ao banco de dados", error)

    def create_table(self):
        self.abrirConexao()
        create_table_query = """CREATE TABLE IF NOT EXISTS missoes (id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_missao TEXT NOT NULL,
        lancamento DATE NOT NULL,
        destino TEXT NOT NULL,
        estado_missao TEXT NOT NULL,
        tripulacao TEXT NOT NULL,
        carga TEXT NOT NULL,
        duracao TEXT NOT NULL,
        custo REAL NOT NULL,
        status TEXT NOT NULL
        );"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_query)
        except sqlite3.Error as error:
            print(error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                
    def inserirDados(self,nome,lancamento,destino,estado,tripulacao,carga,duracao,custo,status):
        self.abrirConexao()
        insert_query = """INSERT INTO missoes(nome_missao,lancamento,destino,estado_missao,
        tripulacao,carga,duracao,custo,status) VALUES (?,?,?,?,?,?,?,?,?)"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(insert_query,(nome,lancamento,destino,estado,tripulacao,carga,duracao,custo,status))
            self.connection.commit()
        except sqlite3.Error as error:
            print('Falha ao inserir dados', error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
    
    def select_missoes(self):
        viagens = []
        self.abrirConexao()
        select_query = "SELECT * FROM missoes ORDER BY lancamento DESC"
        try:
            cursor = self.connection.cursor()
            cursor.execute(select_query)
            viagens = cursor.fetchall()
        except sqlite3.Error as error:
            print("Falha ao retornar missões", error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
        return viagens 
    
    def select_filtro_id(self,filtro_id):
        viagens = []
        self.abrirConexao()
        filtro_id_query = "SELECT * FROM missoes WHERE id=?"
        try:
            cursor = self.connection.cursor()
            cursor.execute(filtro_id_query,(filtro_id,))
            viagens = cursor.fetchall()
        except sqlite3.Error as error:
            print("Falha ao retornar missões", error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
        return viagens 
    
    def select_intervalo(self,data_inicio,data_fim):
        viagens=[]
        self.abrirConexao()
        intervalo_query = "SELECT * FROM missoes WHERE lancamento BETWEEN ? AND ?"
        try:
            cursor = self.connection.cursor()
            cursor.execute(intervalo_query,(data_inicio,data_fim,))
            viagens = cursor.fetchall()

        except Exception as erro:
            print("Falha ao retornar",erro)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
        return viagens
        
    def update_missoes(self,missao_id,nome_missao,lancamento,destino,estado_missao,tripulacao,carga,duracao,custo,status):
        self.abrirConexao()
        update_query = """UPDATE missoes SET nome_missao=?, lancamento=?, destino=?, estado_missao=?, tripulacao=?, carga=?, duracao=?, custo=?, status=?  WHERE id = ? """
        try:
            cursor = self.connection.cursor()
            cursor.execute(update_query,(nome_missao,lancamento,destino,estado_missao,tripulacao,carga,duracao,custo,status,missao_id))
            self.connection.commit()
        except sqlite3.Error as error:
            print("Falha ao atualizar o Missão", error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()

    def delete_missoes(self, missao_id):
        self.abrirConexao()
        delete_query = "DELETE FROM missoes WHERE id = ?"
        try:
            cursor = self.connection.cursor()
            cursor.execute(delete_query, (missao_id,))
            self.connection.commit()
        except sqlite3.Error as error:
            print('Falha ao excluir missão', error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                
    def select_missoes_filtradas(self,filtrar_id):
        missoes_filtradas = []
        self.abrirConexao()
        select_query_filtro = "SELECT * FROM missoes WHERE id = ?"
        try:
            cursor = self.connection.cursor()
            cursor.execute(select_query_filtro,(filtrar_id))
            missoes_filtradas = cursor.fetchall()
        except sqlite3.Error as error:
            print("Falha ao retornar missões", error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
        return missoes_filtradas 
