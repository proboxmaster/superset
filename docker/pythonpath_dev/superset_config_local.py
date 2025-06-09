import os

# 1. Leemos la variable de entorno para la SECRET_KEY que pusiste en Render
SECRET_KEY_ENV = os.environ.get("SECRET_KEY")
if SECRET_KEY_ENV:
    SECRET_KEY = SECRET_KEY_ENV

# 2. Leemos la variable de entorno para la base de datos de metadatos
METADATA_DB_URL = os.environ.get("METADATA_DATABASE_URI")
if METADATA_DB_URL:
    SQLALCHEMY_DATABASE_URI = METADATA_DB_URL

# 3. Pequeño extra: Forzar que se permita subir archivos CSV
CSV_TO_DATABASE_UPLOAD = True
