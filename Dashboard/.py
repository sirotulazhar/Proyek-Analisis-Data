import os
import pandas as pd
import streamlit as st

# Mendapatkan direktori dari file script ini
script_dir = os.path.dirname(os.path.abspath(__file__))
st.write(f"Direktori script: {script_dir}")

# Membuat path absolut ke file CSV
csv_path = os.path.join(script_dir, 'PRSA_Data_cleaned.csv')  # Sesuaikan jika file berada di subfolder 'Dashboard'
st.write(f"Path ke CSV: {csv_path}")

# Cek apakah file ada
if not os.path.exists(csv_path):
    st.error("File CSV tidak ditemukan!")
else:
    df = pd.read_csv(csv_path)
    st.success("File CSV berhasil dibaca.")
    st.write(df.head())  # Menampilkan beberapa baris pertama dari DataFrame

