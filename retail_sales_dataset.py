import streamlit as st
import pandas as pd
import plotly.express as px

# Konfigurasi Halaman Dashboard
st.set_page_config(page_title="Dashboard Analisis Transaksi", layout="wide")

st.title("📊 Dashboard Analisis Transaksi Penjualan")

# Fitur Upload File
uploaded_file = st.file_uploader("Upload file CSV atau Excel kamu di sini, untuk data yang digunakan pada dashboard ini bisa didownload di: https://www.kaggle.com/datasets/mohammadtalib786/retail-sales-dataset/data", type=["csv", "xlsx"])

if uploaded_file is not None:
    if uploaded_file.name.endswith(".csv"):
        # Tambahkan sep=';' di sini agar kolomnya terpisah dengan benar!
        df = pd.read_csv(uploaded_file, sep=';')
    else:
        df = pd.read_excel(uploaded_file)      
else:
    # Data sampel...
    # Data sampel sementara jika belum ada file yang di-upload
    data = {
        "Transaction ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "Date": ["2023-05-01", "2023-05-02", "2023-05-03", "2023-05-04", "2023-05-06", "2023-05-07", "2023-05-08", "2023-05-09", "2023-05-10", "2023-05-11"],
        "Customer ID": ["CUST001", "CUST002", "CUST003", "CUST004", "CUST005", "CUST006", "CUST007", "CUST008", "CUST009", "CUST010"],
        "Gender": ["Male", "Female", "Male", "Male", "Male", "Female", "Male", "Male", "Male", "Female"],
        "Age": [34, 26, 50, 37, 30, 45, 46, 30, 63, 52],
        "Product Category": ["Beauty", "Clothing", "Electronics", "Clothing", "Beauty", "Beauty", "Clothing", "Electronics", "Electronics", "Clothing"],
        "Quantity": [3, 2, 1, 1, 2, 1, 2, 4, 2, 4],
        "Price per Unit": [50, 500, 30, 500, 50, 30, 25, 25, 300, 50],
        "Total Amount": [150, 1000, 30, 500, 100, 30, 50, 100, 600, 200]
    }
    df = pd.DataFrame(data)
    st.info("Menampilkan contoh data sementara. Upload file kamu di atas untuk analisis data asli.")

# Sidebar Filter Interaktif
st.sidebar.header("Filter Data")
gender_filter = st.sidebar.multiselect("Gender:", options=df["Gender"].unique(), default=df["Gender"].unique())
category_filter = st.sidebar.multiselect("Kategori Produk:", options=df["Product Category"].unique(), default=df["Product Category"].unique())

# Terapkan Filter
df_filtered = df[(df["Gender"].isin(gender_filter)) & (df["Product Category"].isin(category_filter))]

# Ringkasan KPI Utama
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Pendapatan", f"${df_filtered['Total Amount'].sum():,.2f}")
col2.metric("Total Kuantitas Terjual", f"{df_filtered['Quantity'].sum():,}")
col3.metric("Total Transaksi", len(df_filtered))
col4.metric("Rata-Rata Usia", f"{df_filtered['Age'].mean():.1f} Tahun")

st.markdown("---")

# Statistika Deskriptif
st.subheader("📌 Statistika Deskriptif")
st.write("Ringkasan statistik numerik:")
numeric_cols = ["Age", "Quantity", "Price per Unit", "Total Amount"]
# Hanya ambil kolom yang ada di dataset
valid_cols = [col for col in numeric_cols if col in df_filtered.columns]
st.dataframe(df_filtered[valid_cols].describe().T)

st.markdown("---")

# Diagram Batang
st.subheader("📊 Visualisasi Diagram Batang")

col_left, col_right = st.columns(2)

with col_left:
    # Diagram Batang 1: Pendapatan per Kategori
    rev_by_cat = df_filtered.groupby("Product Category")["Total Amount"].sum().reset_index()
    fig1 = px.bar(rev_by_cat, x="Product Category", y="Total Amount", 
                  title="Total Pendapatan per Kategori Produk",
                  color="Product Category", text_auto=True)
    st.plotly_chart(fig1, use_container_width=True)

with col_right:
    # Diagram Batang 2: Kuantitas Terjual per Kategori
    qty_by_cat = df_filtered.groupby("Product Category")["Quantity"].sum().reset_index()
    fig2 = px.bar(qty_by_cat, x="Product Category", y="Quantity", 
                  title="Total Kuantitas Terjual per Kategori Produk",
                  color="Product Category", text_auto=True)
    st.plotly_chart(fig2, use_container_width=True)

# Diagram Batang 3: Pendapatan Berdasarkan Gender
rev_by_gender = df_filtered.groupby("Gender")["Total Amount"].sum().reset_index()
fig3 = px.bar(rev_by_gender, x="Gender", y="Total Amount", 
              title="Total Pendapatan berdasarkan Gender",
              color="Gender", text_auto=True)
st.plotly_chart(fig3, use_container_width=True)