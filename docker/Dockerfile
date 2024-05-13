FROM python:3.11 as builder

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app

COPY ./src /app

# Exponer el puerto que Uvicorn utilizará
EXPOSE 8001

# Definir el comando que se ejecutará cuando el contenedor esté listo, utilizando el formato exec
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
