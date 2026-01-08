# 1. Imagen base ultra-ligera y segura
FROM python:3.11-alpine

# 2. Directorio de trabajo
WORKDIR /app

# 3. Instalamos dependencias del sistema usando 'apk' (propio de Alpine)
# musl-dev y postgresql-dev son necesarios para compilar drivers de DB en Python
RUN apk add --no-cache \
    postgresql-dev \
    gcc \
    musl-dev \
    libpq-dev

# 4. Instalamos librerías de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiamos el resto de la aplicación
COPY . .

# 6. Exponemos el puerto de FastAPI
EXPOSE 8000

# 7. Comando de ejecución profesional
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]