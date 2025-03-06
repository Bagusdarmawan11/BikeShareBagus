# 🚲 Bike Sharing Dashboard

Dashboard ini dibuat menggunakan **Streamlit** untuk menganalisis data dari **Bike-sharing-dataset**.

## 📌 Fitur Utama

- 📊 Visualisasi data penggunaan sepeda dengan grafik interaktif
- 📅 Analisis tren penggunaan berdasarkan waktu (harian, mingguan, bulanan)
- 🔍 Penerapan teknik analisis lanjutan seperti **Clustering**
- 🎚️ Filter data berdasarkan musim, cuaca, dan jam operasional
- 📈 Prediksi jumlah pengguna berdasarkan faktor lingkungan
- 🖱️ Interaksi dinamis dengan pengguna melalui slider dan dropdown

## 🛠 Persyaratan

Pastikan sistem Anda memiliki:

- 🐍 **Python 3.8+**
- 📦 **Paket-paket yang diperlukan** (tertera dalam `requirements.txt`)

## 🚀 Cara Menjalankan Dashboard

### 1️⃣ Clone Repository

```bash
git clone <URL_REPOSITORY>
cd <NAMA_FOLDER>
```

### 2️⃣ Buat Virtual Environment (Opsional, tetapi disarankan)

```bash
python -m venv env
source env/bin/activate  # Untuk macOS/Linux
env\Scripts\activate    # Untuk Windows
```

### 3️⃣ Install Dependensi

```bash
pip install -r requirements.txt
```

### 4️⃣ Jalankan Streamlit

```bash
streamlit run dashboard/dashboard.py
```

## 📂 Struktur Folder

```
📁 submission/
│── 📂 dashboard/
│   ├── 📝 dashboard.py
|   ├── 📄 day.csv
│   ├── 📄 hour.csv
│── 📂 data/
│   ├── 📄 day.csv
│   ├── 📄 hour.csv
│── 📄 Proyek_Analisis_Data.ipynb
│── 📄 README.md
│── 📄 requirements.txt
│── 🔗 url.txt
```

## 📌 Deployment

Jika ingin melakukan deployment ke **Streamlit Cloud**, ikuti langkah berikut:

1. 📤 Upload kode ke repository GitHub
2. 🌐 Buka [Streamlit Cloud](https://share.streamlit.io/)
3. 🔗 Hubungkan repository Anda
4. 🏗️ Jalankan aplikasi dengan menentukan file utama (`dashboard/dashboard.py`)
5. 🚀 Klik **Deploy**


---

## Created by Bagus Darmawan

