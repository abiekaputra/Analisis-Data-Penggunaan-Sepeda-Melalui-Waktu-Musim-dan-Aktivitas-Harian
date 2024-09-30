# Analisis Data Penggunaan Sepeda: Waktu, Musim, dan Aktivitas Harian 🚴‍♂️

Proyek ini melakukan analisis mendalam tentang pola penggunaan sepeda berdasarkan berbagai faktor seperti **musim**, **hari kerja/libur**, dan **waktu dalam sehari**. Analisis ini menggunakan dataset dari penggunaan sepeda harian dan per jam. Proyek ini juga mencakup visualisasi interaktif menggunakan **Streamlit** serta analisis lebih lanjut terkait faktor suhu dan musim.

## Fitur Utama 🚀

- **Exploratory Data Analysis (EDA)**: Menyediakan analisis eksploratif untuk mendapatkan pola umum dalam data, termasuk distribusi penggunaan sepeda dan korelasi antar variabel seperti suhu dan juml ah pengguna.
- **Visualisasi Pola Penggunaan**: Menampilkan pola penggunaan sepeda berdasarkan musim, hari kerja/libur, dan waktu dalam sehari.
- **Analisis Lanjutan**: Mengamati pengaruh suhu terhadap penggunaan sepeda, serta tren pengguna sepeda berdasarkan jam dan kondisi cuaca.
- **Interaktif**: Pengguna dapat memfilter data berdasarkan musim dan hari kerja/libur untuk memeriksa pola yang lebih spesifik.

## Struktur Proyek 📂

Proyek ini terdiri dari beberapa file dan direktori:
- `notebook.ipynb`: Notebook Jupyter yang berisi analisis mendalam terkait pola penggunaan sepeda, data wrangling, EDA, serta analisis visual.
- `data/`: Direktori yang berisi data penggunaan sepeda harian dan per jam.
  - `day.csv`: Data penggunaan sepeda harian.
  - `hour.csv`: Data penggunaan sepeda per jam.
- `dashboard/`: Direktori yang berisi script python untuk menjalankan program.
  - `dashboard.py`: File ini berisi kode untuk menjalankan dasbor interaktif menggunakan **Streamlit**.
- `README.md`: File ini yang berisi penjelasan tentang proyek.
- `url.txt`: File ini berisi tautan menuju deploy aplikasi Streamlit.
- `requirements.txt`: Daftar pustaka Python yang diperlukan untuk menjalankan proyek.

## Cara Menjalankan Proyek 💻

### 1. Menjalankan Jupyter Notebook
Untuk menjalankan analisis di **Jupyter Notebook**:
1. Pastikan semua dependensi sudah terpasang dengan perintah berikut:
   ```bash
   pip install -r requirements.txt
   ```
2. Jalankan Jupyter Notebook:
   ```bash
   jupyter notebook notebook.ipynb
   ```

### 2. Menjalankan Dasbor Streamlit
Proyek ini juga dapat diubah menjadi aplikasi interaktif menggunakan **Streamlit**.
1. Instal semua dependensi menggunakan:
   ```bash
   pip install -r requirements.txt
   ```
2. Jalankan aplikasi Streamlit:
   ```bash
   streamlit run dashboard.py
   ```

## Insight Utama 📊

1. **Pola Penggunaan Berdasarkan Musim dan Hari Kerja/Libur**:
   - Penggunaan sepeda lebih tinggi pada musim semi dan musim panas.
   - Pada hari kerja, jumlah pengguna sepeda lebih tinggi dibandingkan hari libur.

2. **Pola Penggunaan Berdasarkan Waktu dalam Sehari**:
   - Puncak penggunaan sepeda terjadi pada jam 8 pagi dan 5 sore, yang bertepatan dengan jam berangkat dan pulang kerja/sekolah.
   - Penggunaan sepeda berkurang di luar jam sibuk, terutama pada malam hari.

3. **Hubungan Suhu dengan Penggunaan Sepeda**:
   - Terdapat hubungan positif antara suhu dan jumlah pengguna sepeda, dengan peningkatan jumlah pengguna saat suhu nyaman.