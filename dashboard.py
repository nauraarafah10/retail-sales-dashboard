import streamlit as st
import pandas as pd

# Judul Utama Dashboard
st.title("Dashboard Statistik Pertamaku")
st.write("Selamat datang! Ini adalah dashboard pertamaku menggunakan Streamlit dan VS Code.")

# Data Contoh (Bentuk Dictionary)
data = {
    'Kategori': ['A', 'B', 'C', 'D'],
    'Nilai': [10, 25, 15, 30]
}
df = pd.DataFrame(data)

# Tampilkan Tabel Data
st.subheader("Tabel Data")
st.dataframe(df)

# Tampilkan Grafik Bar Interaktif
st.subheader("Grafik Bar Interaktif")
st.bar_chart(df.set_index('Kategori'))