import pyodbc
from config import NETEZZA_CONFIG

def get_connection():
    """Conectar a Netezza y devolver la conexión."""
    conn_str = (
        f"DRIVER={NETEZZA_CONFIG['DRIVER']};"
        f"SERVER={NETEZZA_CONFIG['HOST']};"
        f"PORT={NETEZZA_CONFIG['PORT']};"
        f"DATABASE={NETEZZA_CONFIG['DATABASE']};"
        f"UID={NETEZZA_CONFIG['USER']};"
        f"PWD={NETEZZA_CONFIG['PASSWORD']};"
    )
    conn = pyodbc.connect(conn_str)
    return conn
