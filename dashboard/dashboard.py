import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
day_df = pd.read_csv("data/day.csv")
hour_df = pd.read_csv("data/hour.csv")

# Streamlit UI
st.title("Bike Sharing Dashboard")

# Sidebar interaktif
st.sidebar.header("Filter Data")
selected_season = st.sidebar.selectbox("Pilih Musim:", options=["All", 1, 2, 3, 4], format_func=lambda x: "Semua" if x == "All" else ["Spring", "Summer", "Fall", "Winter"][x-1])
selected_weather = st.sidebar.selectbox("Pilih Kondisi Cuaca:", options=["All", 1, 2, 3, 4], format_func=lambda x: "Semua" if x == "All" else ["Clear", "Cloudy", "Light Rain", "Heavy Rain"][x-1])
selected_day = st.sidebar.selectbox("Pilih Hari:", options=["All", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
selected_month = st.sidebar.selectbox("Pilih Bulan:", options=["All"] + list(range(1, 13)), format_func=lambda x: "Semua" if x == "All" else f"Bulan {x}")
selected_hour = st.sidebar.selectbox("Pilih Jam:", options=["All"] + list(range(24)), format_func=lambda x: "Semua" if x == "All" else f"Jam {x}")

# Filter data berdasarkan pilihan
filtered_df = day_df.copy()
if selected_season != "All":
    filtered_df = filtered_df[filtered_df["season"] == selected_season]
if selected_weather != "All":
    filtered_df = filtered_df[filtered_df["weathersit"] == selected_weather]
if selected_day != "All":
    filtered_df = filtered_df[filtered_df["weekday"] == selected_day]
if selected_month != "All":
    filtered_df = filtered_df[filtered_df["mnth"] == selected_month]
filtered_hour_df = hour_df.copy() if selected_hour == "All" else hour_df[hour_df["hr"] == selected_hour]

# Narasi dinamis
st.markdown("## Analisis")
season_text = "semua musim" if selected_season == "All" else ["Spring", "Summer", "Fall", "Winter"][selected_season-1]
weather_text = "semua kondisi cuaca" if selected_weather == "All" else ["Clear", "Cloudy", "Light Rain", "Heavy Rain"][selected_weather-1]
day_text = "semua hari" if selected_day == "All" else selected_day
month_text = "semua bulan" if selected_month == "All" else f"Bulan {selected_month}"
hour_text = "semua jam" if selected_hour == "All" else f"Jam {selected_hour}"
st.markdown(f"Saat ini, data yang ditampilkan adalah penggunaan sepeda berdasarkan **{season_text}**, dengan kondisi cuaca **{weather_text}**, pada **{day_text}**, di **{month_text}**, dan pada **{hour_text}**.")

# Visualisasi 1: Distribusi penggunaan sepeda berdasarkan musim
st.subheader("Distribusi Penggunaan Sepeda Berdasarkan Musim")
fig, ax = plt.subplots(figsize=(10, 5))
sns.boxplot(x="season", y="cnt", data=filtered_df, palette="Set2", ax=ax)
ax.set_xticklabels(["Spring", "Summer", "Fall", "Winter"])
st.pyplot(fig)

# Visualisasi 2: Distribusi penggunaan sepeda berdasarkan cuaca
st.subheader("Distribusi Penggunaan Sepeda Berdasarkan Kondisi Cuaca")
fig, ax = plt.subplots(figsize=(10, 5))
sns.boxplot(x="weathersit", y="cnt", data=filtered_df, palette="coolwarm", ax=ax)
ax.set_xticklabels(["Clear", "Cloudy", "Light Rain", "Heavy Rain"])
st.pyplot(fig)

# Visualisasi 3: Distribusi penggunaan sepeda berdasarkan hari
st.subheader("Distribusi Penggunaan Sepeda Berdasarkan Hari")
fig, ax = plt.subplots(figsize=(10, 5))
sns.boxplot(x="weekday", y="cnt", data=filtered_df, palette="pastel", ax=ax)
st.pyplot(fig)

# Visualisasi 4: Distribusi penggunaan sepeda berdasarkan bulan
st.subheader("Distribusi Penggunaan Sepeda Berdasarkan Bulan")
fig, ax = plt.subplots(figsize=(10, 5))
sns.boxplot(x="mnth", y="cnt", data=filtered_df, palette="Blues", ax=ax)
st.pyplot(fig)

# Visualisasi 5: Waktu paling ramai dan paling sepi penggunaan sepeda dalam sehari
st.subheader("Waktu Paling Ramai dan Paling Sepi Penggunaan Sepeda")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x="hr", y="cnt", data=filtered_hour_df, marker="o", ax=ax)
ax.set_xlabel("Jam")
ax.set_ylabel("Jumlah Pengguna Sepeda")
ax.set_title("Tren Penggunaan Sepeda dalam Sehari")
st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("© 2025 Bagus Darmawan. All Rights Reserved.")
