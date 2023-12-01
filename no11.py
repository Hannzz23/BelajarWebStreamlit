import pickle
import streamlit as st
import pandas as pd
import os
import numpy as np
import altair as alt

model = pickle.load(open('model_prediksi_harga_mobil.sav', 'rb'))


# fungsi untuk membaca data dari file CarPrice.csv
def load_data():
    data = pd.read_csv("CarPrice.csv")
    return data
# fungsi untuk melihat profil
def profil() :
    st.markdown("Dibuat Oleh : ")
    # menampilkan gambar
    st.image('mine.jpg', use_column_width=True)
    st.subheader("Raihan Dwindra Kusuma")
    st.caption("NIM     : 223307110")
    st.caption("Kelas   : Teknologi Informasi-3D")
# fungsi untuk melihat dataset
def Dataset() : 
    st.write("Dataset:")
    # menampilkan dataframe
    st.dataframe(data)

# fungsi untuk melihat grafik highway
def Highway() :
    st.write("Grafik Highway-mpg")
    # membuat grafik
    chart_highwaympg = pd.DataFrame(data, columns=["highwaympg"])
    # membuat grafik tersebut menggunakan line(garis)
    st.line_chart(chart_highwaympg)

# fungsi untuk melihat grafik curbweight
def Curbweight() :
    st.write("Grafik curbweight")
    # membuat grafik
    chart_curbweight = pd.DataFrame(data, columns=["curbweight"])
    # membuat grafik tersebut menggunakan line(garis)
    st.line_chart(chart_curbweight)

# fungsi untuk melihat grafik curbweight
def Horsepower() :
    st.write("Grafik horsepower")
    # membuat grafik
    chart_horsepower = pd.DataFrame(data, columns=["horsepower"])
    # membuat grafik tersebut menggunakan line(garis)
    st.line_chart(chart_horsepower)

# fungsi untuk melihat prediksi
def Prediksi() :
    # mengambil nilai berdasarkan inputan user dengan rentang 0 hingga 100000
    highwaympg = st.number_input('Highway-mpg', 0, 100000)
    curbweight = st.number_input('Curbweight', 0, 100000)
    horsepower = st.number_input('Horsepower', 0, 100000)

    # kondisi ketika tombol prediksi ditekan
    if st.button('Prediksi'):
        # menginisiasi variabel car_prediksi yang berfungsi untuk memprediksi model dengan 3 nilai tersebut
        car_prediction = model.predict([[highwaympg, curbweight, horsepower]])
        #  suatu array NumPy yang berisi hasil prediksi harga mobil
        harga_mobil_str = np.array(car_prediction)
        # mengonversi nilai pertama dari array harga_mobil_str menjadi tipe data float
        harga_mobil_float = float(harga_mobil_str[0])
        # memformat nilai float ke dalam bentuk string dengan dua angka desimal dan pemisah ribuan, ":,.2f" berfungsi untuk pembulatan agar jadi 2 desimal
        harga_mobil_formatted = "{:,.2f}".format(harga_mobil_float)
        st.markdown(f'Harga Mobil: $ {harga_mobil_formatted}')

# fungsi main
def main():
    # membuat sidebar
    st.sidebar.title("Menu")
    # membuat pilihan sidebar
    menu = st.sidebar.selectbox("Pilih Menu", ["Profil", "Dataset", "Grafik Highway", "Grafik Curbweight", "Grafik Horsepower", "Prediksi"])

    # kondisi ketika masing-masing side bar dipilih
    if menu == "Profil":
        st.title ("Ini Profil Saya") 
        # memanggil fungsi
        profil()

    elif menu == "Dataset":
        st.title("Tampilan Dataset")
        data = load_data()
        # memanggil fungsi
        Dataset()

    elif menu == "Grafik Highway":
        st.title("Tampilan Grafik Highway")
        # memanggil fungsi
        data = load_data()
        Highway()

    elif menu == "Grafik Curbweight":
        st.title("Tampilan Grafik Curbweight")
        data = load_data()
        # memanggil fungsi
        Curbweight()

    elif menu == "Grafik Horsepower":
        st.title("Tampilan Grafik Horsepower")
        data = load_data()
        # memanggil fungsi
        Horsepower()

    elif menu == "Prediksi" :
        st.title("Prediksikan Keinginanmu")
        # memanggil fungsi
        Prediksi()

# menginisasi apa yang pertama di run 
if __name__ == "__main__":
    main()