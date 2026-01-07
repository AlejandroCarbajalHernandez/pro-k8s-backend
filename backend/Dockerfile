FROM python:3.11-slim

# 1. Directorio de trabajo
WORKDIR /app

# 2. Instalamos dependencias del sistema necesarias para PostgreSQL y compilación
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# 3. Instalamos las librerías de Python directamente
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiamos el código de la app
COPY . .

# 5. Exponemos el puerto
EXPOSE 8000

# 6. Comando de ejecución (usando la ruta directa de python)
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]