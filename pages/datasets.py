import streamlit as st
import pandas as pd
from utils.db_connection import get_connection
from queries import GET_TABLES

def show():
    st.title("📊 Listado de Tablas por Base de Datos")

    # Seleccionar la base de datos
    database = st.selectbox("Selecciona la base de datos:", ["DESA_RIESGOS", "DESA_MODELOS"])

    if st.button("Mostrar Tablas"):
        conn = get_connection()
        query = GET_TABLES.format(database=database)
        df = pd.read_sql(query, conn)
        conn.close()

        if df.empty:
            st.warning(f"No se encontraron tablas en {database}.")
        else:
            st.dataframe(df, use_container_width=True)
