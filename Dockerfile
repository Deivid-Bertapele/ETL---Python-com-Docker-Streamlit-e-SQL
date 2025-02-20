# Usa uma imagem base leve do Python
FROM python:3.9-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos necessários para o contêiner
COPY . /app

# Instala as dependências do projeto
RUN pip install --no-cache-dir streamlit pandas

# Expõe uma porta diferente
EXPOSE 8080

# Comando para rodar a aplicação Streamlit com nova porta
CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]