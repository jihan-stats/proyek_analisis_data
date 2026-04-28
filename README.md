# Bike Sharing Analysis Dashboard

## Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis data penyewaan sepeda dari sistem **Capital Bikeshare** selama periode 2011–2012.  
Analisis dilakukan untuk menjawab tiga pertanyaan bisnis utama:

1. **Perbedaan rata‑rata penyewaan antara hari kerja dan akhir pekan** pada tiap musim di tahun 2012, beserta implikasinya terhadap alokasi armada.
2. **Jam sibuk dan pengaruh cuaca** terhadap lonjakan permintaan di hari kerja tahun 2012.
3. **Perbandingan total penyewaan per musim** antara tahun 2011 dan 2012, serta musim dengan peningkatan year‑over‑year tertinggi.

Dashboard interaktif dibangun menggunakan **Streamlit** untuk memvisualisasikan hasil analisis.

## Dataset
Dataset yang digunakan berasal dari [Bike Sharing Dataset](https://archive.ics.uci.edu/ml/datasets/bike+sharing+dataset) yang telah dibersihkan dan diolah menjadi dua file CSV:

- `hour_clean.csv` – Data penyewaan per jam (2011–2012)
- `day_clean.csv`  – Data agregat per hari (2011–2012)

Kedua file tersebut harus ditempatkan di dalam folder `dashboard/` (bersama dengan `dashboard.py`).

## Cara Menjalankan Dashboard

### 1. Clone atau Ekstrak Proyek
Pastikan struktur folder proyek seperti berikut:
submission/
├── dashboard/
│ ├── hour_clean.csv
│ ├── day_clean.csv
│ └── dashboard.py
├── notebook.ipynb
├── requirements.txt
├── README.md
└── url.txt (jika deploy)

### 2. Buat Virtual Environment (Opsional tapi disarankan)
```bash
python -m venv bike_env
# Aktifkan virtual environment
# Windows:
bike_env\Scripts\activate
# Mac/Linux:
source bike_env/bin/activate 
```
### 3. Install Dependensi
Jalankan perintah berikut di terminal yang telah diarahkan ke folder root proyek:

```bash
pip install -r requirements.txt
```
Jika Anda tidak memiliki requirements.txt, buat file tersebut dengan isi:

```text
streamlit==1.28.1
pandas==2.0.3
numpy==1.24.3
matplotlib==3.7.2
seaborn==0.12.2
```

###4. Jalankan Dashboard
Pindah ke folder dashboard dan jalankan Streamlit:

```bash
cd dashboard
streamlit run dashboard.py
```
Dashboard akan terbuka di browser (biasanya http://localhost:8501).

### Fitur Dashboard
Sidebar Filter: Pilih tahun (2011/2012) dan musim (Spring, Summer, Fall, Winter) untuk menyaring data.

Pertanyaan 1 – Bar chart perbandingan rata‑rata penyewaan per jam antara hari kerja dan akhir pekan di setiap musim.

Pertanyaan 2 – Line chart pola penyewaan per jam pada hari kerja dengan warna berbeda untuk setiap kondisi cuaca.

Pertanyaan 3 – Bar chart total penyewaan per musim (2011 vs 2012) untuk melihat pertumbuhan tahunan.

Analisis Lanjutan:

Binning Suhu: rata‑rata penyewaan berdasarkan kategori suhu.

Heatmap Korelasi: hubungan antar variabel numerik (suhu, kelembaban, kecepatan angin, dll.).

### Catatan
Pastikan file hour_clean.csv dan day_clean.csv berada di folder yang sama dengan dashboard.py.

Jika Anda melakukan deploy ke Streamlit Cloud, upload kedua file CSV tersebut ke repository GitHub Anda.

Untuk detail proses analisis data, lihat file notebook.ipynb yang telah disertakan.
