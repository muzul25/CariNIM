import streamlit as st
import pandas as pd

# Ganti dengan nama file CSV kamu
CSV_PATH = "database.csv"

@st.cache_data
def load_data():
    try:
        df = pd.read_csv(CSV_PATH)
        return df
    except Exception as e:
        st.error(f"Gagal memuat data: {e}")
        return pd.DataFrame()

def main():
    st.title("🔐 Cek Akun Aplikasi Anda")
    st.write("Masukkan email Anda untuk melihat username & password.")

    df = load_data()

    email = st.text_input("Masukkan email:")

    if email:
        result = df[df['email'].str.lower() == email.lower()]
        if not result.empty:
            st.success("✅ Data ditemukan!")
            st.dataframe(result)
        else:
            st.warning("❌ Email tidak ditemukan.")

if _name_ == "_main_":
    main()
