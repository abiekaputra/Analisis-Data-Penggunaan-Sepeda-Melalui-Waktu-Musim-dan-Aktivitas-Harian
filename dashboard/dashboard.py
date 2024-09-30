import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul dashboard
st.title("Dashboard Analisis Data Penggunaan Sepeda: Waktu, Musim, dan Aktivitas Harian")

# Data Wrangling
st.header("1. Data Wrangling")

# Memuat dataset (Data Gathering)
day_data = pd.read_csv('data/day.csv')
hour_data = pd.read_csv('data/hour.csv')

# Menampilkan data mentah
st.subheader("Raw Data")
st.write("Dataset 'data/day.csv':")
st.write(day_data.head())
st.write("Dataset 'data/hour.csv':")
st.write(hour_data.head())

# Penilaian data (Assessing Data)
st.subheader("Assesing Data")
st.write("Ringkasan dari dataset 'day.csv':")
st.write(day_data.describe())
st.write("Ringkasan dari dataset 'hour.csv':")
st.write(hour_data.describe())

# Mengecek data kosong
st.subheader("Cek Data Kosong")
st.write("Data kosong dari 'day.csv':")
st.write(day_data.isnull().sum())
st.write("Data kosong dari 'hour.csv':")
st.write(hour_data.isnull().sum())

# Proses Cleaning Data
st.subheader("Cleaning Data")
# Memeriksa duplikasi
day_duplicates = day_data.duplicated().sum()
hour_duplicates = hour_data.duplicated().sum()

# Membersihkan data jika ada duplikasi
if day_duplicates > 0:
    st.write(f"Ada {day_duplicates} duplikat di dataset 'day.csv'. Data akan dibersihkan.")
    day_data_cleaned = day_data.drop_duplicates()
else:
    st.write("Tidak ada duplikasi di dataset 'day.csv'.")

if hour_duplicates > 0:
    st.write(f"Ada {hour_duplicates} duplikat di dataset 'hour.csv'. Data akan dibersihkan.")
    hour_data_cleaned = hour_data.drop_duplicates()
else:
    st.write("Tidak ada duplikasi di dataset 'hour.csv'.")

# Menampilkan data yang sudah dibersihkan
st.subheader("Data Setelah Dibersihkan")
st.write("Dataset 'day.csv' yang sudah dibersihkan:")
st.write(day_data_cleaned.head() if day_duplicates > 0 else day_data.head())
st.write("Dataset 'hour.csv' yang sudah dibersihkan:")
st.write(hour_data_cleaned.head() if hour_duplicates > 0 else hour_data.head())

# Exploratory Data Analysis (EDA)
st.header("2. Exploratory Data Analysis (EDA)")

# Visualisasi distribusi penggunaan sepeda per hari
st.subheader("Distribusi Penggunaan Sepeda Per Hari")
fig_dist, ax_dist = plt.subplots()
sns.histplot(day_data['cnt'], kde=True, ax=ax_dist, color='purple')
ax_dist.set_title('Distribusi Penggunaan Sepeda Per Hari')
ax_dist.set_xlabel('Jumlah Pengguna')
ax_dist.set_ylabel('Frekuensi')
st.pyplot(fig_dist)

# Korelasi antara variabel numerik
st.subheader("Korelasi Antar Variabel Numerik")
corr_matrix = day_data[['temp', 'atemp', 'hum', 'windspeed', 'cnt']].corr()

fig_corr, ax_corr = plt.subplots()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax_corr)
ax_corr.set_title('Matriks Korelasi Variabel')
st.pyplot(fig_corr)

# Sidebar
st.sidebar.header("Filters")

# Checkbox untuk musim dengan label sesuai nama musim
spring = st.sidebar.checkbox('Semi', value=True)
summer = st.sidebar.checkbox('Panas', value=True)
fall = st.sidebar.checkbox('Gugur', value=True)
winter = st.sidebar.checkbox('Dingin', value=True)

# Mapping musim untuk ditampilkan
season_map = {1: 'Semi', 2: 'Panas', 3: 'Gugur', 4: 'Dingin'}
selected_seasons = []
if spring:
    selected_seasons.append(1)
if summer:
    selected_seasons.append(2)
if fall:
    selected_seasons.append(3)
if winter:
    selected_seasons.append(4)

# Checkbox untuk hari kerja dan libur
st.sidebar.header("Pilih Hari Kerja dan Libur")
is_working_day = st.sidebar.checkbox('Hari Kerja', value=True)
is_holiday = st.sidebar.checkbox('Hari Libur', value=True)

# Konversi pilihan checkbox ke format numerik
working_day_value = []
if is_holiday:
    working_day_value.append(0)
if is_working_day:
    working_day_value.append(1)

# Filter untuk jam dalam sehari
hour_filter = st.sidebar.slider(
    "Pilih Jam dalam Sehari",
    min_value=int(hour_data['hr'].min()),
    max_value=int(hour_data['hr'].max()),
    value=(int(hour_data['hr'].min()), int(hour_data['hr'].max()))
)

# Filter data berdasarkan input pengguna
filtered_day_data = day_data[day_data['season'].isin(selected_seasons)]
filtered_day_data = filtered_day_data[filtered_day_data['workingday'].isin(working_day_value)]
filtered_hour_data = hour_data[(hour_data['hr'] >= hour_filter[0]) & (hour_data['hr'] <= hour_filter[1])]

# Visual Exploratory Analysis (VEA)
st.header("3. Visual Exploratory Analysis (VEA)")

# Visualisasi 1: Rata-rata pengguna sepeda per musim
st.subheader("Rata-rata Pengguna Sepeda Berdasarkan Musim Menggunakan Manual Grouping")
season_grouping = filtered_day_data.groupby('season')['cnt'].mean().reset_index()
season_grouping['season'] = season_grouping['season'].map(season_map)

fig1, ax1 = plt.subplots()
ax1.bar(season_grouping['season'], season_grouping['cnt'], color='skyblue')
ax1.set_title('Rata-rata Pengguna Berdasarkan Musim')
ax1.set_xlabel('Musim')
ax1.set_ylabel('Rata-rata Pengguna')
st.pyplot(fig1)

# Visualisasi 2: Penggunaan sepeda pada hari kerja vs hari libur
st.subheader("Penggunaan Sepeda pada Hari Kerja vs Libur Menggunakan Manual Grouping")
working_day_grouping = day_data.groupby('workingday')['cnt'].mean().reset_index()
working_day_grouping['workingday'] = working_day_grouping['workingday'].map({0: "Hari Libur", 1: "Hari Kerja"})

fig2, ax2 = plt.subplots()
ax2.bar(working_day_grouping['workingday'], working_day_grouping['cnt'], color='lightblue')
ax2.set_title('Rata-rata Pengguna pada Hari Kerja vs Libur')
ax2.set_xlabel('Hari')
ax2.set_ylabel('Rata-rata Pengguna')
st.pyplot(fig2)

# Visualisasi 3: Penggunaan sepeda berdasarkan jam (dengan filter)
st.subheader("Rata-rata Pengguna Sepeda Berdasarkan Jam Menggunakan Binning")
# Bagian ini menggunakan binning untuk membagi data jam menjadi beberapa interval
hour_grouping = filtered_hour_data.groupby('hr')['cnt'].mean().reset_index()

fig3, ax3 = plt.subplots()
ax3.plot(hour_grouping['hr'], hour_grouping['cnt'], marker='o', color='lightgreen')
ax3.set_title('Rata-rata Pengguna Berdasarkan Jam')
ax3.set_xlabel('Jam')
ax3.set_ylabel('Rata-rata Pengguna')
st.pyplot(fig3)

# Visualisasi 4: Rata-rata pengguna sepeda berdasarkan kondisi cuaca
st.subheader("Rata-rata Pengguna Sepeda Berdasarkan Kondisi Cuaca Menggunakan Manual Grouping")
weather_grouping = day_data.groupby('weathersit')['cnt'].mean().reset_index()

fig4, ax4 = plt.subplots()
ax4.bar(weather_grouping['weathersit'], weather_grouping['cnt'], color='salmon')
ax4.set_title('Rata-rata Pengguna Berdasarkan Kondisi Cuaca')
ax4.set_xlabel('Kondisi Cuaca')
ax4.set_ylabel('Rata-rata Pengguna')
ax4.set_xticks([1, 2, 3])
ax4.set_xticklabels(['Cerah/Berawan', 'Berkabut/Berawan', 'Hujan Ringan/Salju'])
st.pyplot(fig4)

# Bagian 4: Analisis Lanjutan
st.header("4. Analisis Lanjutan")
st.write("""
Pada bagian ini, kita akan melakukan analisis lebih lanjut seperti melihat pengaruh suhu terhadap penggunaan sepeda
dan hubungan antara kondisi cuaca dengan perilaku pengguna.
""")

# Analisis hubungan suhu dengan jumlah pengguna
st.subheader("Hubungan Suhu dengan Penggunaan Sepeda")
fig_temp, ax_temp = plt.subplots()
sns.scatterplot(x='temp', y='cnt', data=day_data, ax=ax_temp)
ax_temp.set_title('Hubungan Suhu dengan Penggunaan Sepeda')
ax_temp.set_xlabel('Suhu')
ax_temp.set_ylabel('Jumlah Pengguna')
st.pyplot(fig_temp)
