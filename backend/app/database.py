from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# 1. Obtener la URL de la base de datos desde las variables de entorno
# En local Docker usará la del docker-compose, en AWS usará la del RDS
SQLALCHEMY_DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql://user_admin:password123_pro@db:5432/analytics_db"
)

# 2. Configurar el motor de la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 3. Crear una fábrica de sesiones (para hacer consultas)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Clase base para nuestros modelos (tablas)
Base = declarative_base()

# 5. Definición de la tabla 'feedbacks'
class Feedback(Base):
    __tablename__ = "feedbacks"

    id = Column(Integer, primary_key=True, index=True)
    user = Column(String, index=True)
    comment = Column(String)