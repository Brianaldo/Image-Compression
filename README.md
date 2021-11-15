# Algeo02-20112
Tugas Besar 2 IF 2123 Aljabar Linier dan Geometri Aplikasi Nilai Eigen dan Vektor Eigen dalam Kompresi Gambar  Semester I Tahun 2021/2022

# Directories

    .
    ├── doc                             # Documentation files (Laporan tugas besar)
    ├── src                             # Source files
    │    ├── frontend                   # Front End (source code untuk tampilan website menggunakan React.JS)
    │    └── backend/imageProcessing    # Back End (source code untuk kompresi gambar menggunakan python)
    ├── test                            # Images for testing
    └── README.md

# Cara menjalankan

## Instalasi Flask
1. Pada terminal, lakukan cd ke folder imageProcessing dalam folder backend
2. Lakukan instalasi flask pada terminal
    - MacOS<br />
        ```python3 -m venv venv```<br />
        ```. venv/bin/activate```<br />
        ```pip install Flask```<br />
    - Window<br />
        ```py -3 -m venv venv```<br />
        ```venv\Scripts\activate```<br />
        ```pip install Flask```<br />
3. `pip install -r requirements.txt`
4. `flask run`

## Instalasi React.JS
1. Pada terminal, lakukan cd ke folder frontend
2. ```npm install```
3. ```npm start```

## Run
1. Access ```http://localhost:3000/```
2. Upload foto yang akan dikompresi dan atur convertion rate
3. Setelah menunggu beberapa saat, hasil kompresi akan muncul
4. Tekan tombol download untuk mendownload hasil
