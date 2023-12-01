import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Fungsi untuk memuat dataset (contoh menggunakan dataset Iris)
def load_data():
    mobil = pd.read_csv("CarPrice.csv")
    return mobil

# Fungsi untuk menampilkan gambar
def show_image(image_path):
    st.image(image_path, caption='Image', use_column_width=True)

# Fungsi untuk menampilkan dataset dalam bentuk tabel
def show_dataset(data):
    st.write("Dataset:")
    st.dataframe(data)

# Fungsi untuk menampilkan grafik sesuai pilihan pada selectbox
def show_plot(data):
    plt.figure(figsize=(10,4))
    plt.subplot(1,2,1)
    plt.title('Car Prize Distribution Plot')
    sns.histplot(data.price)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.pyplot()
    

def main():
    st.sidebar.title("Menu")
    menu = st.sidebar.selectbox("Pilih Menu", ["Image", "Dataset", "Grafik"])

    if menu == "Image":
        st.title("Tampilan Gambar")
        image_path = "aurora.jpg"  
        show_image(image_path)

    elif menu == "Dataset":
        st.title("Tampilan Dataset")
        data = load_data()
        show_dataset(data)

    elif menu == "Grafik":
        st.title(f"Tampilan Grafik")
        data = load_data()
        show_plot(data)

if __name__ == "__main__":
    main()
