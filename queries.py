# SQL para listar las tablas de una base de datos en Netezza
GET_TABLES = """
SELECT DISTINCT TABLENAME
FROM _V_TABLE
WHERE UPPER(DATABASE) = UPPER('{database}');
"""
# SQL para obtener detalles de un dataset específico
GET_DATASET_DETAIL = """
SELECT *
FROM {table_name}
LIMIT 100;
"""