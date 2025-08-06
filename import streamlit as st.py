import streamlit as st
import pandas as pd

# Fungsi memuat database dengan toleransi terhadap error parsing
@st.cache_data
def load_database():
    try:
        return pd.read_csv("database.csv", on_bad_lines='skip', encoding='utf-8')
    except Exception as e:
        st.error(f"Gagal memuat database: {e}")
        return pd.DataFrame()  # Kembalikan DataFrame kosong jika gagal

df = load_database()

# Judul Aplikasi
st.title("🔐 Pencarian Username & Password Berdasarkan Email")

# Input Email
email_input = st.text_input("Masukkan Email Anda").strip().lower()

# Tombol pencarian
if st.button("Cari Data"):
    if email_input:
        result = df[df['Email'].str.lower() == email_input]

        if not result.empty:
            user_data = result.iloc[0]
            st.success("✅ Data ditemukan!")
            st.write(f"**Nama**: {user_data['Nama']}")
            st.write(f"**Username**: {user_data['Username']}")
            st.write(f"**Password**: {user_data['Password']}")
        else:
            st.error("🚫 Email tidak ditemukan dalam database.")
    else:
        st.warning("⚠️ Silakan masukkan email terlebih dahulu.")
