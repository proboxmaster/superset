import os

# Mensaje 1: Para confirmar que este archivo se está cargando.
print("--- DEBUG: CARGANDO ARCHIVO superset_config_local.py ---")

# Mensaje 2: Leemos las variables de entorno de Render.
SECRET_KEY_FROM_ENV = os.environ.get("SECRET_KEY")
METADATA_URI_FROM_ENV = os.environ.get("METADATA_DATABASE_URI")

# Mensaje 3: Mostramos en el log lo que encontramos.
print(f"--- DEBUG: SECRET_KEY encontrada en el entorno: {SECRET_KEY_FROM_ENV}")
print(f"--- DEBUG: METADATA_URI encontrada en el entorno: {METADATA_URI_FROM_ENV}")

# Lógica principal: Si encontramos la llave, la usamos.
if SECRET_KEY_FROM_ENV:
    SECRET_KEY = SECRET_KEY_FROM_ENV
    print("--- DEBUG: EXITO! Se ha sobreescrito la SECRET_KEY desde la variable de entorno.")
else:
    # Si no la encontramos, lo decimos claramente.
    print("--- DEBUG: ERROR! No se pudo encontrar la variable de entorno SECRET_KEY.")

# Lógica para la base de datos
if METADATA_URI_FROM_ENV:
    SQLALCHEMY_DATABASE_URI = METADATA_URI_FROM_ENV
    print("--- DEBUG: EXITO! Se ha sobreescrito la SQLALCHEMY_DATABASE_URI.")
else:
    print("--- DEBUG: ERROR! No se pudo encontrar la variable de entorno METADATA_DATABASE_URI.")

print("--- DEBUG: FINALIZADA LA CARGA DE superset_config_local.py ---")
