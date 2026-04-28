import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

# ==================== HELPER FUNCTIONS ====================
@st.cache_data
def load_data():
    hour_df = pd.read_csv("hour_clean.csv")
    day_df = pd.read_csv("day_clean.csv")
    hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
    day_df['dteday'] = pd.to_datetime(day_df['dteday'])
    return hour_df, day_df

def filter_by_year(df, year):
    return df[df['dteday'].dt.year == year]

# ==================== LOAD DATA ====================
hour_df, day_df = load_data()

# ==================== SIDEBAR ====================
with st.sidebar:
    st.image("https://raw.githubusercontent.com/jihan-stats/proyek_analisis_data/main/PedalMetrics.png", width=150)  # ganti dengan logo Anda
    st.markdown("## Filter Data")
    
    # Filter tahun (untuk pertanyaan 1 & 2, kita fokus tahun 2012)
    year_options = ['2011', '2012']
    selected_year = st.selectbox("Pilih Tahun Analisis", year_options, index=1)
    
    # Filter musim (untuk semua visualisasi)
    seasons = hour_df['season_label'].unique().tolist()
    selected_seasons = st.multiselect("Pilih Musim", seasons, default=seasons)

# ==================== MAIN DASHBOARD ====================
st.title("🚲 Bike Sharing Dashboard")
st.markdown("Analisis penyewaan sepeda berdasarkan pertanyaan bisnis SMART.")

# --- Data yang sudah difilter ---
hour_filtered = hour_df[(hour_df['dteday'].dt.year == int(selected_year)) & 
                        (hour_df['season_label'].isin(selected_seasons))]

day_filtered = day_df[(day_df['season_label'].isin(selected_seasons))]

# ------------------- PERTANYAAN 1 -------------------
st.subheader("1. Perbedaan Rata-rata Penyewaan: Hari Kerja vs Akhir Pekan per Musim (2012)")
st.markdown("**Pertanyaan:** Bagaimana perbedaan rata‑rata jumlah penyewaan sepeda antara hari kerja dan akhir pekan pada tiap musim di tahun 2012, dan bagaimana implikasinya terhadap strategi alokasi armada?")

fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.barplot(data=hour_filtered, x='season_label', y='cnt', hue='day_type',
            estimator='mean', order=['Spring','Summer','Fall','Winter'],
            palette='Set2', ax=ax1)
ax1.set_title("Rata-rata Penyewaan per Jam (2012)", fontsize=14)
ax1.set_xlabel("Musim")
ax1.set_ylabel("Rata-rata Jumlah Penyewaan")
ax1.legend(title="Tipe Hari")
st.pyplot(fig1)

with st.expander("Lihat Insight Pertanyaan 1"):
    st.write("""
    - Hari kerja selalu memiliki rata-rata penyewaan lebih tinggi dibanding akhir pekan di semua musim.
    - Musim gugur (Fall) menjadi puncak tertinggi, sementara musim semi (Spring) memiliki selisih terbesar antara hari kerja dan akhir pekan.
    - **Implikasi:** Alokasi armada harus difokuskan pada hari kerja, terutama di musim gugur dan semi. Pada akhir pekan, distribusi dapat dikurangi tetapi tetap cukup untuk kebutuhan rekreasi.
    """)

# ------------------- PERTANYAAN 2 -------------------
st.subheader("2. Jam Sibuk & Pengaruh Cuaca pada Hari Kerja (2012)")
st.markdown("**Pertanyaan:** Pada jam berapa terjadi lonjakan permintaan tertinggi di hari kerja selama tahun 2012, dan bagaimana pengaruh kondisi cuaca terhadap lonjakan tersebut?")

# Filter hanya hari kerja
workday_df = hour_filtered[hour_filtered['workingday'] == 1]

fig2, ax2 = plt.subplots(figsize=(12, 6))
sns.lineplot(data=workday_df, x='hr', y='cnt', hue='weather_label',
             estimator='mean', palette='Set2', linewidth=2, ax=ax2)
ax2.set_title("Pola Penyewaan per Jam pada Hari Kerja (2012) Berdasarkan Cuaca", fontsize=14)
ax2.set_xlabel("Jam")
ax2.set_ylabel("Rata-rata Jumlah Penyewaan")
ax2.set_xticks(range(0, 24))
ax2.legend(title="Cuaca")
st.pyplot(fig2)

with st.expander("Lihat Insight Pertanyaan 2"):
    st.write("""
    - Lonjakan tertinggi terjadi pada pukul 08.00 pagi dan pukul 17.00-18.00 sore, sesuai dengan jam berangkat dan pulang kerja.
    - Cuaca cerah (Clear) menghasilkan penyewaan tertinggi; hujan ringan (Light Rain) menurunkan permintaan drastis; hujan lebat (Heavy Rain) hampir tidak ada penyewaan.
    - **Implikasi:** Pastikan ketersediaan sepeda maksimal sebelum pukul 07.00 dan 16.00. Pada hari dengan prakiraan hujan, sediakan insentif atau promo untuk mendorong penggunaan.
    """)

# ------------------- PERTANYAAN 3 -------------------
st.subheader("3. Perbandingan Total Penyewaan per Musim (2011 vs 2012)")
st.markdown("**Pertanyaan:** Bagaimana perbandingan total penyewaan sepeda harian antara tahun 2011 dan 2012, dan pada musim apa terjadi peningkatan year-over-year tertinggi?")

# Agregasi total penyewaan per tahun dan per musim
season_yearly = day_filtered.groupby(['year', 'season_label'])['cnt'].sum().unstack()

fig3, ax3 = plt.subplots(figsize=(10, 6))
season_yearly.plot(kind='bar', colormap='Set2', edgecolor='black', ax=ax3)
ax3.set_title("Total Penyewaan per Musim (2011 vs 2012)", fontsize=14)
ax3.set_xlabel("Tahun")
ax3.set_ylabel("Total Penyewaan")
ax3.set_xticklabels(['2011', '2012'], rotation=0)
ax3.legend(title="Musim", bbox_to_anchor=(1.05, 1), loc='upper left')
st.pyplot(fig3)

with st.expander("Lihat Insight Pertanyaan 3"):
    st.write("""
    - Seluruh musim menunjukkan peningkatan dari 2011 ke 2012.
    - Peningkatan absolut terbesar terjadi pada musim gugur (Fall), sedangkan peningkatan persentase tertinggi pada musim semi (Spring).
    - **Kesimpulan:** Pertumbuhan tahunan yang positif mengindikasikan peningkatan adopsi layanan. Fokus ekspansi armada dapat diprioritaskan pada musim gugur dan semi.
    """)

# ------------------- ANALISIS LANJUTAN (Opsional) -------------------
st.subheader("4. Analisis Lanjutan: Pengaruh Suhu dan Korelasi")
col1, col2 = st.columns(2)

with col1:
    st.markdown("**Rata-rata Penyewaan Berdasarkan Kategori Suhu**")
    bins = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
    labels = ['Sangat Dingin', 'Dingin', 'Sejuk', 'Hangat', 'Panas']
    hour_filtered['temp_bin'] = pd.cut(hour_filtered['temp'], bins=bins, labels=labels)
    fig4, ax4 = plt.subplots(figsize=(8,5))
    sns.barplot(data=hour_filtered, x='temp_bin', y='cnt', estimator='mean',
                palette='coolwarm', order=labels, ax=ax4)
    ax4.set_title("Rata-rata Penyewaan vs Suhu")
    ax4.set_xlabel("Kategori Suhu")
    ax4.set_ylabel("Rata-rata Penyewaan")
    st.pyplot(fig4)

with col2:
    st.markdown("**Heatmap Korelasi Variabel Numerik**")
    num_cols = ['temp', 'atemp', 'hum', 'windspeed', 'casual', 'registered', 'cnt']
    corr = hour_filtered[num_cols].corr()
    fig5, ax5 = plt.subplots(figsize=(8,6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, ax=ax5)
    ax5.set_title("Korelasi Antar Variabel")
    st.pyplot(fig5)

# ==================== FOOTER ====================
st.caption("Copyright © 2025 Bike Sharing Analysis Dashboard | Data source: Capital Bikeshare")