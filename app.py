import streamlit as st
import sqlite3
import pandas as pd

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('database.db')

def main():
    # Título da aplicação
    st.title("Exemplo Simples com Streamlit e SQLite")

    # Consulta SQL simples
    query = "SELECT * FROM vendas"
    df = pd.read_sql_query(query, conn)

    # Exibir os dados em uma tabela
    st.write("Dados da Tabela Vendas:")
    st.dataframe(df)

    # Filtro interativo
    filtro_categoria = st.selectbox("Filtrar por Categoria:", df['categoria'].unique())
    df_filtrado = df[df['categoria'] == filtro_categoria]

    st.write(f"Dados filtrados para a categoria '{filtro_categoria}':")
    st.dataframe(df_filtrado)

    # Fechar a conexão com o banco de dados
    conn.close()

if __name__ == "__main__":
    main()