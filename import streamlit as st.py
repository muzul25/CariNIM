import streamlit as st
import pandas as pd

# Load database CSV
@st.cache_data
def load_database():
    return pd.read_csv("database.csv")

df = load_database()

# Judul Aplikasi
st.title("Pencarian Data Login Berdasarkan Email")

# Input Email dari Pengguna
email_input = st.text_input("Masukkan Email Anda").strip().lower()

# Proses pencarian saat tombol ditekan
if st.button("Cari Data"):
    if email_input:
        # Filter data berdasarkan email
        result = df[df['Email'].str.lower() == email_input]

        if not result.empty:
            user_data = result.iloc[0]  # Hanya ambil satu data
            st.success("Data ditemukan!")
            st.write(f"**Nama**: {user_data['Nama']}")
            st.write(f"**Username**: {user_data['Username']}")
            st.write(f"**Password**: {user_data['Password']}")
        else:
            st.error("Email tidak ditemukan dalam database.")
    else:
        st.warning("Silakan masukkan email terlebih dahulu.")
