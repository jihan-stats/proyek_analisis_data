# 🚲 Bike Sharing Analysis Dashboard

## 📌 Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis data penyewaan sepeda dari sistem **Capital Bikeshare** selama periode 2011–2012.  
Analisis dilakukan untuk menjawab tiga pertanyaan bisnis utama:

1. **Perbedaan rata‑rata penyewaan antara hari kerja dan akhir pekan** pada tiap musim di tahun 2012, beserta implikasinya terhadap alokasi armada.
2. **Jam sibuk dan pengaruh cuaca** terhadap lonjakan permintaan di hari kerja tahun 2012.
3. **Perbandingan total penyewaan per musim** antara tahun 2011 dan 2012, serta musim dengan peningkatan year‑over‑year tertinggi.

Dashboard interaktif dibangun menggunakan **Streamlit** untuk memvisualisasikan hasil analisis.

## 📂 Dataset
Dataset yang digunakan berasal dari [Bike Sharing Dataset](https://archive.ics.uci.edu/ml/datasets/bike+sharing+dataset) yang telah dibersihkan dan diolah menjadi dua file CSV:

- `hour_clean.csv` – Data penyewaan per jam (2011–2012)
- `day_clean.csv`  – Data agregat per hari (2011–2012)

Kedua file tersebut harus ditempatkan di dalam folder `dashboard/` (bersama dengan `dashboard.py`).

## 🛠️ Cara Menjalankan Dashboard

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

