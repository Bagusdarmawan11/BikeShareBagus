import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

# Load dataset
day_df = pd.read_csv("data/day.csv")
hour_df = pd.read_csv("data/hour.csv")

# Mapping season and weather categories
season_mapping = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
weather_mapping = {1: "Clear", 2: "Mist", 3: "Light Snow/Rain", 4: "Heavy Snow/Rain"}

day_df["season"] = day_df["season"].map(season_mapping)
day_df["weathersit"] = day_df["weathersit"].map(weather_mapping)

# Sidebar
st.sidebar.title("🔍 Filter dan Navigasi")
st.sidebar.write("Gunakan filter untuk menyesuaikan tampilan data.")

# Filter berdasarkan tanggal dengan try-exception
st.sidebar.subheader("📅 Filter berdasarkan Tanggal")
try:
    start_date = st.sidebar.date_input("Mulai Tanggal", pd.to_datetime(day_df['dteday']).min())
    end_date = st.sidebar.date_input("Akhir Tanggal", pd.to_datetime(day_df['dteday']).max())
    day_df = day_df[(pd.to_datetime(day_df['dteday']) >= pd.to_datetime(start_date)) &
                     (pd.to_datetime(day_df['dteday']) <= pd.to_datetime(end_date))]
except Exception as e:
    st.sidebar.warning("⚠️ Pastikan tanggal yang dipilih valid!")

# Filter berdasarkan cuaca atau parameter lain
parameter_filter = st.sidebar.selectbox("Pilih Parameter untuk Filter:", ["Semua", "Cuaca", "User Type"])
if parameter_filter == "Cuaca":
    selected_weather = st.sidebar.selectbox("Pilih Cuaca:", day_df["weathersit"].unique())
    day_df = day_df[day_df["weathersit"] == selected_weather]
elif parameter_filter == "User Type":
    selected_user_type = st.sidebar.selectbox("Pilih User Type:", ["Casual", "Registered"])
    if selected_user_type == "Casual":
        hour_df = hour_df[hour_df["casual"] > 0]
    else:
        hour_df = hour_df[hour_df["registered"] > 0]

# Pilihan visualisasi
selected_viz = st.sidebar.selectbox("Pilih Visualisasi:", [
    "Jumlah pengguna berdasarkan musim",
    "Rata-rata pengguna per jam",
    "Hasil Clustering"
])

# Judul Dashboard
st.title("📊 Bike Sharing Data Dashboard")

# Statistik Ringkasan
st.subheader("📊 Statistik Ringkasan")
st.write(f"Total Pengguna Sepeda: {day_df['cnt'].sum()}")
st.write(f"Rata-rata Pengguna Harian: {day_df['cnt'].mean():.2f}")
st.write(f"Jumlah Hari dalam Dataset: {day_df.shape[0]}")

# Visualisasi Data
st.subheader("📈 Visualisasi Data")
if selected_viz == "Jumlah pengguna berdasarkan musim":
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.boxplot(x="season", y="cnt", data=day_df, palette="Set2", ax=ax)
    ax.set_xlabel("Musim")
    ax.set_ylabel("Jumlah Pengguna Sepeda")
    ax.set_title("Distribusi Penggunaan Sepeda Berdasarkan Musim")
    st.pyplot(fig)

elif selected_viz == "Rata-rata pengguna per jam":
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(x="hr", y="cnt", data=hour_df, estimator="mean", ci=None, marker="o", color="b", ax=ax)
    ax.set_xlabel("Jam dalam Sehari")
    ax.set_ylabel("Rata-rata Jumlah Pengguna Sepeda")
    ax.set_title("Rata-rata Penggunaan Sepeda Berdasarkan Jam dalam Sehari")
    st.pyplot(fig)

elif selected_viz == "Hasil Clustering":
    st.subheader("🎯 Hasil Clustering")
    clustering_features = hour_df[["hr", "season", "weathersit", "cnt"]]
    scaler = MinMaxScaler()
    scaled_features = scaler.fit_transform(clustering_features)
    
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    hour_df["cluster"] = kmeans.fit_predict(scaled_features)
    
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.scatterplot(x=hour_df["hr"], y=hour_df["cnt"], hue=hour_df["cluster"], palette="Set1", ax=ax)
    ax.set_xlabel("Jam dalam Sehari")
    ax.set_ylabel("Jumlah Pengguna Sepeda")
    ax.set_title("Hasil Clustering Pola Penggunaan Sepeda")
    st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("© 2025 Bagus Darmawan. All rights reserved.")
