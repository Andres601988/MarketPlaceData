import streamlit as st
import pandas as pd
import plotly.express as px
from utils.db_connection import get_connection
from queries import GET_DATASET_DETAIL

def show():
    st.title("📈 Análisis de Datos")

    table_name = st.text_input("Ingrese el nombre del dataset:")

    if st.button("Cargar Datos") and table_name:
        conn = get_connection()
        df = pd.read_sql(GET_DATASET_DETAIL.format(table_name=table_name), conn)
        conn.close()

        st.write("Vista previa:")
        st.dataframe(df.head(), use_container_width=True)

        col_to_plot = st.selectbox("Selecciona una columna para graficar:", df.columns)
        fig = px.histogram(df, x=col_to_plot, title=f"Distribución de {col_to_plot}")
        st.plotly_chart(fig)
