import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Criar a tabela vendas se não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS vendas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        categoria TEXT NOT NULL,
        valor REAL NOT NULL
    )
''')

# Inserir dados de exemplo
cursor.execute("INSERT INTO vendas (categoria, valor) VALUES ('eletronicos', 100.50)")
cursor.execute("INSERT INTO vendas (categoria, valor) VALUES ('livros', 25.99)")
cursor.execute("INSERT INTO vendas (categoria, valor) VALUES ('eletronicos', 200.75)")
cursor.execute("INSERT INTO vendas (categoria, valor) VALUES ('roupas', 300.75)")


# Salvar as mudanças e fechar a conexão
conn.commit()
conn.close()