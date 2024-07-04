import streamlit as st
import cv2 as cv
import numpy as np
from PIL import Image, ImageEnhance
import os
from features.detect_face import detect_face
from features.detect_eye import detect_eye

def main():
    menu = ['Home', 'Deteksi Gambar', 'Tentang Pengembang']
    pilihan = st.sidebar.selectbox('Menu', menu)

    if pilihan == 'Deteksi Gambar':
        st.subheader('Deteksi Gambar')
        st.text('Silahkan upload gambar yang ingin di deteksi')

        tipe_gambar = ['jpg', 'jpeg', 'png']
        file_gambar = st.file_uploader('Unggah file', type=tipe_gambar)

        if file_gambar is not None:
            tampil_gambar = Image.open(file_gambar)
            st.image(tampil_gambar, 'Gambar Orisinal')
        
            menu = ['Orisinal', 'Abu-abu', 'Kecerahan', 'Kontras', 'Blur', 'Ketajaman']
            pilihan_menu = st.sidebar.radio('Ubah Gambar', menu)

            if pilihan_menu == 'Abu-abu':
                gambar_orisinal = np.array(tampil_gambar.convert('RGB'))
                gambar_abu2 = cv.cvtColor(gambar_orisinal, cv.COLOR_BGR2GRAY)
                st.image(gambar_abu2, 'Gambar Abu-abu')
            elif pilihan_menu == 'Kecerahan':
                nilai_kecerahan = st.sidebar.slider('Nilai Kecerahan', 0.0, 8.0)
                kecerahan = ImageEnhance.Brightness(tampil_gambar)
                gambar_cerah = kecerahan.enhance(nilai_kecerahan)
                st.image(gambar_cerah, 'Kecerahan Gambar')
            elif pilihan_menu == 'Kontras':
                nilai_kontras = st.sidebar.slider('Nilai Kontras', 0.5, 6.0)
                kontras = ImageEnhance.Contrast(tampil_gambar)
                gambar_kontras = kontras.enhance(nilai_kontras)
                st.image(gambar_kontras, 'Gambar Kontras')
            elif pilihan_menu == 'Blur':
                nilai_blur = st.sidebar.slider('Nilai Blur', 0.0, 7.0)
                gambar_blur = cv.GaussianBlur(np.array(tampil_gambar), (15, 15), nilai_blur)
                st.image(gambar_blur, 'Gambar Blur')
            elif pilihan_menu == 'Ketajaman':
                nilai_ketajaman = st.sidebar.slider('Nilai Ketajaman', 0.0, 14.0)
                ketajaman = ImageEnhance.Sharpness(tampil_gambar)
                gambar_ketajaman = ketajaman.enhance(nilai_ketajaman)
                st.image(gambar_ketajaman, 'Gambar Ketajaman')

            menu = ['Wajah', 'Mata']
            pilihan = st.sidebar.selectbox('Pilihan Fitur', menu)

            if st.button('Proses...'):
                if pilihan == 'Wajah':
                    gambar, wajah = detect_face(tampil_gambar)
                    st.image(gambar, 'Hasil deteksi')
                    st.success('{} wajah terdeteksi'.format(len(wajah)))
                elif pilihan == 'Mata':
                    gambar, mata = detect_eye(tampil_gambar)
                    st.image(gambar, 'Hasil deteksi')
                    st.success('{} mata terdeteksi'.format(len(mata)))

        

    elif pilihan == 'Tentang Pengembang':
        st.subheader('Tentang Pengembang')
        st.text('''
        Nama        : Muhamad Daffa Maulana Arrasyid
        Kelas       : TI.22.A.4
        NIM         : 312210335
        Mata Kuliah : Pengolahan Citra
        ''')
    elif pilihan == 'Home':
        st.title("Aplikasi Website untuk Pengolahan Citra Digital")
        st.text("Ubah berbagai macam citra gambar anda disini!")

if __name__ == "__main__":
    main()