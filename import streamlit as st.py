import streamlit as st
import pandas as pd

# Fungsi untuk memuat CSV
@st.cache_data
def load_database():
    try:
        return pd.read_csv("database.csv", on_bad_lines='skip', encoding='utf-8')
    except Exception as e:
        st.error(f"Gagal memuat database: {e}")
        return pd.DataFrame()

df = load_database()

# Tampilkan nama-nama kolom asli
st.write("📋 Kolom dalam database:", df.columns.tolist())

# Deteksi kolom email secara fleksibel
email_column = next((col for col in df.columns if 'email' in col.lower()), None)
nama_column = next((col for col in df.columns if 'nama' in col.lower()), None)
username_column = next((col for col in df.columns if 'username' in col.lower()), None)
password_column = next((col for col in df.columns if 'password' in col.lower()), None)

# Validasi kolom
if not email_column:
    st.error("❌ Kolom 'Email' tidak ditemukan. Harap periksa kembali file CSV Anda.")
    st.stop()

# Input Email
st.title("🔐 Cari Data Login")
email_input = st.text_input("Masukkan Email Anda").strip().lower()

if st.button("Cari Data"):
    if not email_input:
        st.warning("⚠️ Silakan masukkan email terlebih dahulu.")
    else:
        result = df[df[email_column].str.lower() == email_input]

        if result.empty:
            st.error("🚫 Email tidak ditemukan dalam database.")
        else:
            data = result.iloc[0]  # Ambil satu data pertama
            st.success("✅ Data ditemukan!")

            if nama_column:
                st.write("**Nama:**", data[nama_column])
            if username_column:
                st.write("**Username:**", data[username_column])
            if password_column:
                st.write("**Password:**", data[password_column])
