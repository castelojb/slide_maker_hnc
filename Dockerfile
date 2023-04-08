FROM python:3.10

WORKDIR /code

COPY ./server_requeriments.txt /code/server_requeriments.txt

RUN pip install --no-cache-dir --upgrade -r /code/server_requeriments.txt

COPY ./server /code/server

COPY ./setup.py /code/setup.py

COPY ./main.py /code/main.py

EXPOSE 8080

CMD ["python", "main.py"]
