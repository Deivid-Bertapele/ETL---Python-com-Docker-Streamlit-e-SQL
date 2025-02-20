
# executar o docker image:
docker build . -t streamlit_image


# Docker container
 ${pwd}:/ - windows     $(pwd):/ - Linux   

docker run --name streamlit_container -p 8501:8501 -d -v "$(pwd)":/code streamlit_image



# docker-compose
docker-compose build
docker-compose up






# ETL---Python-com-Docker-Streamlit-e-SQL
