import streamlit as st
import pandas as pd
from utils.db_connection import get_connection
from queries import GET_DATASET_DETAIL

def show():
    st.title("🔍 Buscar Dataset")

    table_name = st.text_input("Ingrese el nombre del dataset:")
    
    if st.button("Buscar") and table_name:
        conn = get_connection()
        df = pd.read_sql(GET_DATASET_DETAIL.format(table_name=table_name), conn)
        conn.close()

        st.dataframe(df, use_container_width=True)
