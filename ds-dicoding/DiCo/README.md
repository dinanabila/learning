# DiCo - Dicoding Collection Dashboard ✨

## Background
_cerita hanya fiktif belaka, dibuat untuk tujuan belajar analisis data_

Dicoding Collection, lebih dikenal sebagai DiCo, merupakan sebuah perusahaan yang bergerak di bidang fashion. Ia memproduksi berbagai item fashion dan menjualnya melalui platform online. 

![DiCo Logo](https://github.com/dicodingacademy/assets/raw/main/logo.png)

Sebagai perusahaan kekinian, DiCo menyadari betapa pentingnya data bagi perkembangan sebuah bisnis. Oleh karena itu, ia menyimpan semua history penjualan beserta informasi terkait produk dan customers dalam sebuah database. Database ini terdiri dari empat buah tabel, antara lain customers, orders, products, dan sales.

## Dataset
Dataset yang digunakan adalah [DicodingCollection](https://github.com/dicodingacademy/dicoding_dataset/tree/main/DicodingCollection). Dataset ini merupakan hasil modifikasi dari dataset [Shopping Cart Database](https://www.kaggle.com/datasets/ruchi798/shopping-cart-database) yang dipublikasi dalam platform kaggle. Proses modifikasi ini bertujuan untuk memastikan dataset yang digunakan cukup merepresentasikan semua masalah yang umum dijumpai di industri.

## Setup Environment - Shell/Terminal
```
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Run Streamlit App
```
streamlit run dashboard.py
```
