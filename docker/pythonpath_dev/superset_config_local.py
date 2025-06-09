# --- CONFIGURACIÓN DE ÚLTIMO RECURSO ---
# Escribimos los valores directamente en el código.

# 1. Base de datos de Metadatos
SQLALCHEMY_DATABASE_URI = "postgresql://neondb_owner:npg_7KGXYVSi4Amz@ep-lucky-morning-a8gtu4mi-pooler.eastus2.azure.neon.tech/neondb?sslmode=require"

# 2. Clave Secreta
SECRET_KEY = "65bca6cb-64de-41f7-8a79-55b62bebe164"

# 3. Pequeño extra: Forzar que se permita subir archivos CSV
CSV_TO_DATABASE_UPLOAD = True

# --- Mensajes de depuración para confirmar que se carga ---
print("--- DEBUG v2: Cargando config local HARCODED ---")
if "SQLALCHEMY_DATABASE_URI" in locals():
    print(f"--- DEBUG v2: Usando Metadata DB que termina en: ...{SQLALCHEMY_DATABASE_URI[-15:]}")
if "SECRET_KEY" in locals():
    print(f"--- DEBUG v2: Usando Secret Key que empieza con: {SECRET_KEY[:5]}...")
