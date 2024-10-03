import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv('day.csv')

# Konfigurasi tampilan dashboard
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

# Header Dashboard
st.title("Bike Sharing System Dashboard")
st.markdown("Dashboard ini menampilkan hasil analisis dari penggunaan sistem berbagi sepeda berdasarkan waktu, musim, dan faktor cuaca.")

# Mapping tahun
year_mapping = {0: 'Tahun 2011', 1: 'Tahun 2012'}
# Mapping musim
season_mapping = {
    1: 'Musim Semi',
    2: 'Musim Panas',
    3: 'Musim Gugur',
    4: 'Musim Dingin'
}

# Ambil pilihan unik dari kolom tahun dan musim
year_options = data['yr'].unique()  # Daftar unik tahun
season_options = data['season'].unique()  # Daftar unik musim

# Ubah tahun dan musim sesuai mapping
year_options_display = [year_mapping[year] for year in year_options]
season_options_display = [season_mapping[season] for season in season_options]
# Ubah tahun dan musim sesuai mapping
year_options_display = [year_mapping[year] for year in year_options]
season_options_display = [season_mapping[season] for season in season_options]

# Sidebar untuk memilih tahun dan musim
st.sidebar.header("Filter Data")

# Pilihan tahun berdasarkan data
selected_year = st.sidebar.multiselect(
    'Pilih Tahun',
    options=year_options_display,
    default=year_options_display  # Secara default, semua tahun dipilih
)

# Pilihan musim berdasarkan data
selected_season = st.sidebar.multiselect(
    'Pilih Musim',
    options=season_options_display,
    default=season_options_display  # Secara default, semua musim dipilih
)

# Mengonversi kembali pilihan ke nilai numerik untuk filter data
selected_year_numeric = [year for year, display in year_mapping.items() if display in selected_year]
selected_season_numeric = [season for season, display in season_mapping.items() if display in selected_season]

# Filter data berdasarkan pilihan user
filtered_data = data[(data['yr'].isin(selected_year_numeric)) & (data['season'].isin(selected_season_numeric))]

# Menampilkan data yang telah difilter
st.write("Data setelah difilter:")
st.dataframe(filtered_data)

# Visualisasi 1: Penggunaan sepeda berdasarkan musim
st.subheader("Penggunaan Sepeda Berdasarkan Musim")
season_data = filtered_data.groupby('season')['cnt'].mean().reset_index()
plt.figure(figsize=(10, 5))
sns.barplot(x='season', y='cnt', data=season_data)
plt.title("Rata-rata Penggunaan Sepeda per Musim")
st.pyplot(plt)

# Visualisasi 2: Penggunaan sepeda per hari dalam seminggu
st.subheader("Penggunaan Sepeda Berdasarkan Hari dalam Seminggu")
weekday_data = filtered_data.groupby('weekday')['cnt'].mean().reset_index()
plt.figure(figsize=(10, 5))
sns.barplot(x='weekday', y='cnt', data=weekday_data)
plt.title("Rata-rata Penggunaan Sepeda per Hari dalam Seminggu")
st.pyplot(plt)

# Visualisasi 3: Pengaruh cuaca terhadap penggunaan sepeda
st.subheader("Pengaruh Cuaca Terhadap Penggunaan Sepeda")
weather_data = filtered_data.groupby('weathersit')['cnt'].mean().reset_index()
plt.figure(figsize=(10, 5))
sns.barplot(x='weathersit', y='cnt', data=weather_data)
plt.title("Rata-rata Penggunaan Sepeda Berdasarkan Kondisi Cuaca")
st.pyplot(plt)

# Visualisasi 4: Pengaruh suhu terhadap penggunaan sepeda
st.subheader("Pengaruh Suhu Terhadap Penggunaan Sepeda")
plt.figure(figsize=(10, 5))
sns.scatterplot(x='temp', y='cnt', data=filtered_data)
plt.title("Penggunaan Sepeda Berdasarkan Suhu")
st.pyplot(plt)

# Footer
st.markdown("Dashboard ini menampilkan tren penggunaan sepeda dan faktor yang memengaruhi penggunaan berdasarkan data historis.")
