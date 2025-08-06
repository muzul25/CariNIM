import streamlit as st
import pandas as pd

# Fungsi memuat CSV
@st.cache_data
def load_database():
    try:
        return pd.read_csv("database.csv", on_bad_lines='skip', encoding='utf-8')
    except Exception as e:
        st.error(f"Gagal memuat database: {e}")
        return pd.DataFrame()

df = load_database()

# Tampilkan nama kolom untuk membantu debugging
st.write("Kolom di file:", df.columns.tolist())

# Judul
st.title("🔐 Cari Username & Password Berdasarkan Email")

# Input email
email_input = st.text_input("Masukkan Email Anda").strip().lower()

# Coba deteksi nama kolom email yang benar
possible_email_columns = [col for col in df.columns if 'email' in col.lower()]
if possible_email_columns:
    email_column = possible_email_columns[0]  # Ambil yang pertama cocok
else:
    st.error("Kolom email tidak ditemukan dalam file.")
    st.stop()

# Tombol pencarian
if st.button("Cari Data"):
    if email_input:
        result = df[df[email_column].str.lower() == email_input]

        if not result.empty:
            user_data = result.iloc[0]
            # Coba cari kolom nama, username, dan password
            nama_col = next((c for c in df.columns if 'nama' in c.lower()), None)
            user_col = next((c for c in df.columns if 'username' in c.lower()), None)
            pass_col = next((c for c in df.columns if 'password' in c.lower()), None)

            st.success("✅ Data ditemukan!")
            if nama_col: st.write(f"**Nama**: {user_data[nama_col]}")
            if user_col: st.write(f"**Username**: {user_data[user_col]}")
            if pass_col: st.write(f"**Password**: {user_data[pass_col]}")
        else:
            st.error("🚫 Email tidak ditemukan.")
    else:
        st.warning("⚠️ Masukkan email terlebih dahulu.")
