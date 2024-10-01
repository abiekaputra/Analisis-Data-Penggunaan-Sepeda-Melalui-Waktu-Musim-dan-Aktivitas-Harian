import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul dashboard
st.title("Dashboard Analisis Data Penggunaan Sepeda: Waktu, Musim, dan Aktivitas Harian")

# Memuat dataset (Data Gathering)
day_data = pd.read_csv('data/day.csv')
hour_data = pd.read_csv('data/hour.csv')

# Bagian Data Wrangling
st.header("1. Data Wrangling")

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
    day_data_cleaned = day_data.copy()
    st.write("Tidak ada duplikasi di dataset 'day.csv'.")

if hour_duplicates > 0:
    st.write(f"Ada {hour_duplicates} duplikat di dataset 'hour.csv'. Data akan dibersihkan.")
    hour_data_cleaned = hour_data.drop_duplicates()
else:
    hour_data_cleaned = hour_data.copy()
    st.write("Tidak ada duplikasi di dataset 'hour.csv'.")

# Menampilkan data yang sudah dibersihkan
st.subheader("Data Setelah Dibersihkan")
st.write("Dataset 'day.csv' yang sudah dibersihkan:")
st.write(day_data_cleaned.head())
st.write("Dataset 'hour.csv' yang sudah dibersihkan:")
st.write(hour_data_cleaned.head())

# Sidebar Filters
st.sidebar.header("Filters")

# Musim (Season) Filter
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

# Hari Kerja dan Libur Filter
st.sidebar.header("Pilih Hari Kerja dan Libur")
is_working_day = st.sidebar.checkbox('Hari Kerja', value=True)
is_holiday = st.sidebar.checkbox('Hari Libur', value=True)

working_day_value = []
if is_holiday:
    working_day_value.append(0)
if is_working_day:
    working_day_value.append(1)

# **Menghilangkan Filter Jam dalam Sehari**
# Jadi, kita tidak lagi memerlukan slider untuk memilih jam

# Filter data berdasarkan input pengguna (musim dan hari kerja/libur)
filtered_day_data = day_data_cleaned[day_data_cleaned['season'].isin(selected_seasons)]
filtered_day_data = filtered_day_data[filtered_day_data['workingday'].isin(working_day_value)]

# Karena kita menghilangkan filter jam, kita gunakan seluruh data untuk jam
filtered_hour_data = hour_data_cleaned.copy()

# Exploratory Data Analysis (EDA)
st.header("2. Visualization, Explanatory Analysis & Advanced Analysis")

# Visualisasi distribusi penggunaan sepeda per hari
st.subheader("Distribusi Penggunaan Sepeda Per Hari")
plt.figure(figsize=(10, 6))
hist_data = sns.histplot(filtered_day_data['cnt'], kde=True, color='#6495ED', edgecolor='black')

heights = [p.get_height() for p in hist_data.patches]
max_height = max(heights)
max_height_index = heights.index(max_height)
hist_data.patches[max_height_index].set_facecolor('#4169E1')

plt.title('Distribusi Penggunaan Sepeda Per Hari', fontsize=14, fontweight='bold')
plt.xlabel('Jumlah Pengguna', fontsize=12)
plt.ylabel('Frekuensi', fontsize=12)
st.pyplot(plt)

# Matriks Korelasi
st.subheader("Korelasi Antar Variabel Numerik")
corr_matrix = filtered_day_data[['temp', 'atemp', 'hum', 'windspeed', 'cnt']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Matriks Korelasi Variabel', fontsize=14, fontweight='bold')
st.pyplot(plt)

# Rata-rata pengguna sepeda per musim dengan highlight balok tertinggi
st.subheader("Visualisasi penggunaan sepeda per musim menggunakan manual grouping untuk menjawab pertanyaan 1")
season_grouping = filtered_day_data.groupby('season')['cnt'].mean().reset_index()
season_grouping['season'] = season_grouping['season'].map(season_map)

plt.figure(figsize=(8, 6))
base_color = '#ADD8E6'
highlight_color = '#4169E1'
bars = sns.barplot(x='season', y='cnt', hue='season', data=season_grouping, palette=[base_color] * len(season_grouping), dodge=False, legend=False)

heights = [bar.get_height() for bar in bars.patches]
max_height = max(heights)
for bar in bars.patches:
    if bar.get_height() == max_height:
        bar.set_facecolor(highlight_color)

plt.title('Rata-rata Pengguna Sepeda Berdasarkan Musim', fontsize=14, fontweight='bold')
plt.xlabel('Musim', fontsize=12)
plt.ylabel('Rata-rata Pengguna', fontsize=12)
st.pyplot(plt)

# Penggunaan sepeda pada hari kerja vs libur
st.subheader("Visualisasi penggunaan sepeda pada hari kerja dan libur menggunakan manual grouping untuk menjawab pertanyaan 1")
working_day_grouping = filtered_day_data.groupby('workingday')['cnt'].mean().reset_index()
working_day_grouping['workingday'] = working_day_grouping['workingday'].map({0: 'Hari Libur', 1: 'Hari Kerja'})

plt.figure(figsize=(8, 6))
base_color = '#ADD8E6'
highlight_color = '#4682B4'
bars = sns.barplot(x='workingday', y='cnt', data=working_day_grouping, hue='workingday', palette=[base_color, base_color], dodge=False)

heights = [bar.get_height() for bar in bars.patches]
max_height = max(heights)
for bar in bars.patches:
    if bar.get_height() == max_height:
        bar.set_color(highlight_color)

plt.title('Penggunaan Sepeda pada Hari Kerja vs Libur', fontsize=14, fontweight='bold')
plt.xlabel('Hari', fontsize=12)
plt.ylabel('Rata-rata Pengguna', fontsize=12)
st.pyplot(plt)

# Penggunaan sepeda berdasarkan jam
st.subheader("Visualisasi penggunaan sepeda berdasarkan jam menggunakan binning untuk menjawab pertanyaan 2")

hour_grouping = hour_data_cleaned.groupby('hr')['cnt'].mean().reset_index()
hour_grouping = hour_grouping.sort_values('hr').reset_index(drop=True)
hour_grouping['cnt_diff'] = hour_grouping['cnt'].diff()
hour_grouping['cnt_diff'].fillna(0, inplace=True)

top_increases = hour_grouping.nlargest(2, 'cnt_diff')

# Mendapatkan jam dan nilai cnt pada lonjakan tertinggi
peak_hours = top_increases['hr'].tolist()
peak_values = top_increases['cnt'].tolist()

# Plot rata-rata pengguna sepeda per jam
plt.figure(figsize=(10, 6))
sns.lineplot(x='hr', y='cnt', data=hour_grouping, marker='o', color='green')

# Highlight pada dua lonjakan tertinggi
for peak, peak_value in zip(peak_hours, peak_values):
    plt.scatter(peak, peak_value, color='red', zorder=5, s=100)
    plt.text(peak, peak_value + 10, f'{int(peak)}:00', color='red', fontsize=10, ha='center')

plt.title('Rata-rata Pengguna Sepeda Berdasarkan Jam', fontsize=14, fontweight='bold')
plt.xlabel('Jam', fontsize=12)
plt.ylabel('Rata-rata Pengguna', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
st.pyplot(plt)