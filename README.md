# Analisis Faktor Penyebab Drop Out Jaya Jaya Institute dan Pembuatan Model Prediksi
## Business Understanding
* Permasalahan:

 Jaya Jaya Institut adalah sebuah institusi pendidikan tinggi yang telah menghasilkan banyak lulusan berkualitas sejak tahun 2000. Namun, institusi ini menghadapi tantangan serius berupa tingginya angka siswa yang tidak menyelesaikan pendidikan alias dropout. Fenomena ini tidak hanya mencederai reputasi institusi, namun juga menandakan adanya permasalahan sistemik yang perlu segera diatasi.
 Tingginya angka dropout dapat disebabkan oleh berbagai faktor, seperti performa akademik yang rendah, kurangnya keterlibatan siswa, tekanan ekonomi, dan kurangnya bimbingan. Oleh karena itu, deteksi dini terhadap siswa yang berpotensi dropout menjadi sangat krusial agar pihak institusi dapat memberikan intervensi dan bimbingan yang tepat waktu.

* Tujuan:
  * Mengembangkan model machine learning yang mampu memprediksi kemungkinan seorang siswa akan dropout berdasarkan data historis dan akademik.
  * Menyediakan dashboard interaktif yang dapat digunakan oleh pihak institusi untuk memantau performa siswa dan mengidentifikasi potensi risiko dropout.
  * Memberikan rekomendasi aksi konkret (action items) untuk mendukung pengambilan keputusan berbasis data.

* Cakupan Proyek:
Cakupan proyek ini mencakup seluruh tahapan data science sebagai berikut:
   - Business Understanding: Merumuskan permasalahan dan tujuan bisnis.
   - Data Understanding: Eksplorasi dan pemahaman terhadap dataset performa siswa.
   - Data Preparation: Pembersihan dan transformasi data untuk keperluan analisis.
   - Modeling: Pengembangan model prediksi dropout menggunakan algoritma machine learning.
   - Evaluation: Evaluasi performa model dengan metrik yang relevan.
   - Deployment: Pembuatan prototype sistem prediksi dropout menggunakan Streamlit dan integrasi ke cloud.
   - Data Visualization: Pembuatan dashboard performa siswa dengan Looker Studio, atau Tableau.


* Persiapan
  * Sumber Data: Data yang digunakan dalam proyek ini diperoleh dari repositori publik di GitHub dengan detail sebagai berikut:
    1. Link Data: [Dataset Students' Performance](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)
    2. Isi Data: Informasi mengenai atribut-atribut siswa saat tahap pendaftaran (seperti usia, jenis kelamin, dan faktor sosial-ekonomi) dan kinerja akademik mahasiswa pada akhir semester pertama dan kedua. 
  * Setup Environment: Untuk melaksanakan proyek ini, jalankan perintah berikut di terminal
    
Membuat virtual environment:
Mac/Linux:
```
python3 -m venv .venv
```

Windows:
```
python -m venv .venv
```

Mengaktifkan virtual environment:
Mac/Linux:
```
source .venv/bin/activate
```

Windows:
```
.venv/Scripts/activate
```

     
## Business Dashboard
Dashboard dibuat dengan menggunakan Google Looker Studio. Dashboard dapat diakses pada link berikut ini:
```
https://lookerstudio.google.com/reporting/d7547cec-4b73-4030-8895-525db4a09658
```
### Insight dari Dashboard

Berdasarkan dashboard yang sudah dibuat drop out terbanyak dilakukan pada siswa kelas pagi yang sudah melakukan pembayaran, namun pada grafik debtor (hutang) dropout terbesar dilakukan pada orang yang tidak melakukan debtor dan siswa yang tidak terlantar. Pada grafik pie chart dropout masih lebih sedikit dibandingkan dengan siswa yang dropout terbanyak bergender laki-laki sebesar 66,4%
| Faktor                      | Insight                                                                                                                               |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| **Penunggak**              | Mahasiswa yang memiliki tunggakan pembayaran (penunggak) **lebih banyak** yang dropout dibandingkan dengan yang membayar tepat waktu. |
| **Terlantar (Displaced)**  | Dropout lebih umum terjadi pada mahasiswa yang **terlantar / merantau**, menunjukkan pentingnya dukungan adaptasi atau logistik.      |
| **Beasiswa**               | Mahasiswa **tanpa beasiswa** lebih sering dropout daripada penerima beasiswa, menunjukkan pentingnya bantuan finansial.               |
| **Kuliah Malam**           | Dropout lebih tinggi pada mahasiswa **kelas malam**, kemungkinan karena mereka bekerja atau memiliki tanggung jawab lain.             |
| **Mahasiswa Internasional**| Mahasiswa **internasional lebih rentan dropout**, mungkin karena hambatan bahasa, budaya, atau administratif.                         |


## Menjalankan Sistem Machine Learning
Jelaskan cara menjalankan protoype sistem machine learning yang telah dibuat. Selain itu, sertakan juga link untuk mengakses prototype tersebut.
1. Buka terminal
2. Aktifkan virtual environment yang telah dibuat sebelumnya
3. Masuk ke lokasi dimana file streamlit (app.py) berada
4. Jalankan file streamlit dengan perintah berikut ini:
```
streamlit run app.py
```
### Bagaiamana mencoba prototype secara online?
Melalui link dibawah ini:
```
https://jaya-insitute-intansartika.streamlit.app/
```

## Conclusion
- Komposisi siswa terdiri dari 65.6% Laki-laki dan 34.4% Perempuan.
- Tingkat kelulusan siswa (Graduation Rate) sebesar 60.9%% sedangkan tingkat ketidaklulusan (Dropout Rate) sebesar 39,1% dari 3.630 siswa
- Penerima beasiswa terdapat (26,7%) dan siswa yang bukan penerima (73,3%)
- Dari 1.421 siswa yang dropout terdapat 1.214 siswa (85.43%) yang mengikuti kelas pagi dan 207 siswa (14.57%) yang mengikuti kelas malam
- Selain itu, faktor curricular units dan tuition fees juga cukup berpengaruh pada tingkat kelulusan siswa.
### Rekomendasi Action Items
| Area                            | Rekomendasi                                                                                                                     |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **Finansial**                   | Buat program penjadwalan pembayaran atau diskon untuk **penunggak**. Pantau status pembayaran sejak awal semester.              |
| **Dukungan Mahasiswa Merantau** | Sediakan **layanan orientasi dan pendampingan khusus** untuk mahasiswa **terlantar / luar daerah**.                             |
| **Beasiswa**                    | Perluas cakupan **beasiswa berbasis risiko dropout**, bukan hanya prestasi. Prioritaskan yang nilai masuk atau semester rendah. |
| **Kelas Malam**                 | Berikan **bimbingan fleksibel** untuk mahasiswa malam (online mentoring, akses rekaman materi, dll).                            |
| **Mahasiswa Internasional**     | Bentuk **unit layanan khusus internasional**: dukungan bahasa, birokrasi, dan penyesuaian budaya akademik.                      |
