import pyodbc

DRIVER_NAME = '{ODBC Driver 17 for SQL Server}'

SERVER_NAME = 'localhost' 
DATABASE_NAME = 'CandidatasDB' 
CONNECTION_STRING = (
    f"DRIVER={DRIVER_NAME};"
    f"SERVER={SERVER_NAME};"
    f"DATABASE={DATABASE_NAME};"
    "Trusted_Connection=yes;"
)

def get_db_connection():
    try:
        conn = pyodbc.connect(CONNECTION_STRING)
        return conn
    except pyodbc.Error as ex: 
        sqlstate = ex.args[0]
        if sqlstate == 'HY000':
            print("ERRO: Verifique se o banco de dados e o servidor estão corretos.")
        else:
            print(f"ERRO DE CONEXÃO COM O SQL SERVER: {ex}")
        return None
    

def inicializar_bd():

    conn = get_db_connection()
    if conn is None:
        return
        
    cursor = conn.cursor()
    
    try:

        cursor.execute("""
            IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Candidatas' AND xtype='U')
            CREATE TABLE Candidatas (
                Id INT IDENTITY(1,1) PRIMARY KEY,
                Nome NVARCHAR(255) NOT NULL,
                Clube NVARCHAR(255) NOT NULL,
                ImagemCandidata VARBINARY(MAX), -- Simula o byte[] do C#
                ImagemClube VARBINARY(MAX)
            )
        """)
        conn.commit()
        print(f"Tabela 'Candidatas' inicializada no banco de dados '{DATABASE_NAME}'.")

    except pyodbc.Error as err:
        print(f"Erro ao inicializar tabela: {err}")
    finally:
        conn.close()

def inserir_candidata_db(nome, clube):

    conn = get_db_connection()
    if conn is None:
        return None 

    cursor = conn.cursor()
    
    try:
        sql = """
            INSERT INTO Candidatas (Nome, Clube, ImagemCandidata, ImagemClube) 
            VALUES (?, ?, ?, ?)
        """
        valores = (nome, clube, None, None) 
        
        cursor.execute(sql, valores)
        
        conn.commit()
        
        cursor.execute("SELECT SCOPE_IDENTITY()")
        
        row = cursor.fetchone()        

        if row and row[0] is not None:
            last_id = row[0]
            return int(last_id)
        else:

            print("Aviso: A inserção foi concluída, mas o ID não foi retornado pelo SQL Server.")
            return None

    except pyodbc.Error as err:
        print(f"Erro ao inserir no SQL Server: {err}")
        return None
        
    finally:
        if conn:
            conn.close()


def listar_candidatas_db():   
    conn = get_db_connection()
    if conn is None:
        return []
        
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT Id, Nome, Clube FROM Candidatas ORDER BY Id ASC")     
        candidatas = cursor.fetchall() 
        return candidatas

    except pyodbc.Error as err:
        print(f"Erro ao listar do SQL Server: {err}")
        return []
        
    finally:
        conn.close()