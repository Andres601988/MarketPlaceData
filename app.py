import streamlit as st
from pages import home, datasets, search, analytics

# Configuración inicial
st.set_page_config(page_title="Data Marketplace", layout="wide")

# Sidebar para navegación
st.sidebar.title("Navegación")
menu = st.sidebar.radio("Ir a:", ["🏠 Inicio", "📊 Datasets", "🔍 Búsqueda", "📈 Análisis"])

if menu == "🏠 Inicio":
    home.show()
elif menu == "📊 Datasets":
    datasets.show()
elif menu == "🔍 Búsqueda":
    search.show()
elif menu == "📈 Análisis":
    analytics.show()
