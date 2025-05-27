import streamlit as st

st.title("selamat datanggg di web informatika")
st.write("informatika seru")
st.image("20230831_160803.jpg")





st.title("Aplikasi Sederhana")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("tulis sebuah angka", value=0, step=1)

if(angka % 2) ==0:
  st.write(f"{angka} adalah bilangan genap")
else:
  st.write(f"{angka} adalah bilangan ganjil")
