import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime

# Load dataset
day_df = pd.read_csv("data/day.csv")
hour_df = pd.read_csv("data/hour.csv")

# Streamlit UI
st.title("Bike Sharing Dashboard")

# Sidebar interaktif
st.sidebar.header("Filter Data")
selected_season = st.sidebar.selectbox("Pilih Musim:", options=["All", 1, 2, 3, 4], 
                                       format_func=lambda x: "Semua" if x == "All" else ["Spring", "Summer", "Fall", "Winter"][x-1])
selected_weather = st.sidebar.selectbox("Pilih Kondisi Cuaca:", options=["All", 1, 2, 3, 4], 
                                        format_func=lambda x: "Semua" if x == "All" else ["Clear", "Cloudy", "Light Rain", "Heavy Rain"][x-1])
selected_day = st.sidebar.selectbox("Pilih Hari:", options=["All", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
selected_month = st.sidebar.selectbox("Pilih Bulan:", options=["All"] + list(range(1, 13)), 
                                      format_func=lambda x: "Semua" if x == "All" else f"Bulan {x}")
selected_hour_range = st.sidebar.slider("Pilih Rentang Jam:", 0, 23, (6, 18))

# Filter data berdasarkan pilihan
filtered_df = day_df.copy()
if selected_season != "All":
    filtered_df = filtered_df[filtered_df["season"] == int(selected_season)]
if selected_weather != "All":
    filtered_df = filtered_df[filtered_df["weathersit"] == int(selected_weather)]
if selected_day != "All":
    day_mapping = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}
    filtered_df = filtered_df[filtered_df["weekday"] == day_mapping[selected_day]]
if selected_month != "All":
    filtered_df = filtered_df[filtered_df["mnth"] == int(selected_month)]

filtered_hour_df = hour_df[(hour_df["hr"] >= selected_hour_range[0]) & (hour_df["hr"] <= selected_hour_range[1])]

# Narasi dinamis
st.markdown("## Analisis")
season_text = "semua musim" if selected_season == "All" else ["Spring", "Summer", "Fall", "Winter"][int(selected_season)-1]
weather_text = "semua kondisi cuaca" if selected_weather == "All" else ["Clear", "Cloudy", "Light Rain", "Heavy Rain"][int(selected_weather)-1]
day_text = "semua hari" if selected_day == "All" else selected_day
month_text = "semua bulan" if selected_month == "All" else f"Bulan {selected_month}"
hour_text = f"Jam {selected_hour_range[0]} - {selected_hour_range[1]}"
st.markdown(f"Saat ini, data yang ditampilkan adalah penggunaan sepeda berdasarkan **{season_text}**, dengan kondisi cuaca **{weather_text}**, pada **{day_text}**, di **{month_text}**, dan dalam rentang **{hour_text}**.")

# Mapping untuk mengganti angka menjadi label
season_mapping = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
weather_mapping = {1: "Clear", 2: "Cloudy", 3: "Light Rain", 4: "Heavy Rain"}
weekday_mapping = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}

# Visualisasi 1: Penyewaan sepeda berdasarkan musim
st.subheader("Distribusi Penggunaan Sepeda Berdasarkan Musim")
fig, ax = plt.subplots(figsize=(10, 5))
df_season = filtered_df.groupby("season")["cnt"].sum().reset_index()
df_season["season"] = df_season["season"].map(season_mapping)  # Ubah angka jadi label musim
sns.barplot(data=df_season, x="season", y="cnt", palette="pastel", ax=ax)
plt.title("Jumlah Penyewaan Sepeda Berdasarkan Musim")
st.pyplot(fig)

# Visualisasi 2: Penyewaan sepeda berdasarkan kondisi cuaca
st.subheader("Distribusi Penggunaan Sepeda Berdasarkan Kondisi Cuaca")
fig, ax = plt.subplots(figsize=(10, 5))
df_weather = filtered_df.groupby("weathersit")["cnt"].mean().reset_index()
df_weather["weathersit"] = df_weather["weathersit"].map(weather_mapping)  # Ubah angka jadi label cuaca
sns.barplot(data=df_weather, x="weathersit", y="cnt", palette="coolwarm", ax=ax)
plt.title("Rata-rata Penyewaan Sepeda Berdasarkan Kondisi Cuaca")
st.pyplot(fig)

# Visualisasi 3: Penyewaan sepeda berdasarkan hari dalam seminggu
st.subheader("Distribusi Penggunaan Sepeda Berdasarkan Hari")
fig, ax = plt.subplots(figsize=(10, 5))
df_day = filtered_df.groupby("weekday")["cnt"].mean().reset_index()
df_day["weekday"] = df_day["weekday"].map(weekday_mapping)  # Ubah angka jadi label hari
sns.barplot(data=df_day, x="weekday", y="cnt", palette="pastel", ax=ax)
plt.title("Rata-rata Penyewaan Sepeda Berdasarkan Hari")
st.pyplot(fig)

# Visualisasi 4: Penyewaan sepeda berdasarkan bulan
st.subheader("Distribusi Penggunaan Sepeda Berdasarkan Bulan")
fig, ax = plt.subplots(figsize=(10, 5))
df_month = filtered_df.groupby("mnth")["cnt"].sum().reset_index()
sns.barplot(data=df_month, x="mnth", y="cnt", palette="Blues", ax=ax)
plt.title("Jumlah Penyewaan Sepeda Berdasarkan Bulan")
st.pyplot(fig)

# Visualisasi 5: Waktu paling ramai dan paling sepi penggunaan sepeda dalam rentang jam tertentu
st.subheader("Waktu Paling Ramai dan Paling Sepi Penggunaan Sepeda")
fig, ax = plt.subplots(figsize=(10, 5))
df_hourly = filtered_hour_df.groupby("hr")["cnt"].mean().reset_index()
sns.lineplot(data=df_hourly, x="hr", y="cnt", ax=ax)
plt.title(f"Rata-rata Penyewaan Sepeda dalam Rentang Jam {selected_hour_range[0]} - {selected_hour_range[1]}")
ax.set_xlabel("Jam")
ax.set_ylabel("Jumlah Pengguna Sepeda")
ax.set_title("Tren Penggunaan Sepeda dalam Rentang Jam")
st.pyplot(fig)

# Menambahkan kolom untuk membedakan akhir pekan dan hari kerja
filtered_df['is_weekend'] = filtered_df['weekday'].apply(lambda x: 1 if x in [5, 6] else 0)  # 5 = Saturday, 6 = Sunday

# Visualisasi 6: Penyewaan sepeda berdasarkan akhir pekan vs hari kerja
st.subheader("Penyewaan Sepeda: Akhir Pekan vs Hari Kerja")
fig, ax = plt.subplots(figsize=(10, 5))
df_weekend = filtered_df.groupby("is_weekend")["cnt"].mean().reset_index()
df_weekend["is_weekend"] = df_weekend["is_weekend"].map({0: "Hari Kerja", 1: "Akhir Pekan"})

sns.barplot(data=df_weekend, x="is_weekend", y="cnt", palette="muted", ax=ax)
plt.title("Rata-rata Penyewaan Sepeda pada Hari Kerja vs Akhir Pekan")
ax.set_xlabel("Kategori Hari")
ax.set_ylabel("Rata-rata Jumlah Penyewaan Sepeda")
st.pyplot(fig)


# Footer dengan tahun otomatis
current_year = datetime.datetime.now().year
st.markdown("---")
st.markdown(f"© {current_year} Bagus Darmawan. All Rights Reserved.")
