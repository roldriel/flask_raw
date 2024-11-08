# Usa una imagen de Python 3.11
FROM python:3.11-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo de requerimientos y lo instala
COPY install/requirements.txt .

# Instala las dependencias de Python
RUN python3 -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código fuente de la aplicación en el contenedor
COPY src/ /app

# Expone el puerto 8000 para Flask
EXPOSE 8000

# Define la variable de entorno para Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8000

# Comando de entrada para ejecutar la aplicación
CMD ["flask", "run"]
