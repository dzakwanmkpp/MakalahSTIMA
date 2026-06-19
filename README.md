# Maximizing Profit in Charizard Pokémon Card PSA Grading Submissions: A 0/1 Knapsack Dynamic Programming Approach

**Author:** Dzakwan Muhammad Khairan Putra Purnama (13524145)  
**Course:** IF2211 Strategi Algoritma - Institut Teknologi Bandung  

## 📌 Deskripsi Proyek
Repositori ini berisi kode sumber, dataset, dan hasil eksperimen untuk makalah evaluasi optimasi profit pengajuan *grading* kartu Pokémon Charizard ke PSA (Professional Sports Authenticator). 

Penelitian ini memodelkan proses *grading* sebagai masalah **0/1 Knapsack** dan membandingkan dua pendekatan algoritmik:
1. **Dynamic Programming (DP):** Algoritma eksak untuk menjamin solusi optimal global.
2. **Greedy Algorithm:** Algoritma heuristik berbasis kepadatan (*profit-to-cost ratio*).

## 🗂️ Struktur Repositori
- `main.py` : Skrip utama berisi implementasi algoritma DP dan Greedy, serta fungsi untuk mengeksekusi skenario komparasi.
- `generate_chart.py` : Skrip untuk menghasilkan visualisasi *Bar Chart* perbandingan waktu eksekusi.
- `dataset_charizard_75_final.csv` : Dataset empiris berisi 75 kartu Charizard beserta metrik biaya grading dan estimasi profit.
- `requirements.txt` : Daftar dependensi Python yang dibutuhkan (`pandas`, `matplotlib`, `numpy`).
- `Fig5_Execution_Time_Comparison.png` : Hasil *plot* grafik komparasi waktu komputasi.

## 🚀 Cara Menjalankan Program

### 1. Persiapan Lingkungan (Virtual Environment)
Disarankan menggunakan *virtual environment* agar dependensi terisolasi:
```bash
python -m venv venv

# Aktivasi di Windows:
.\venv\Scripts\activate

# Aktivasi di Mac/Linux:
source venv/bin/activate
```

### 2. Instalasi Dependensi
```bash
pip install -r requirements.txt
```

### 3. Menjalankan Komparasi Algoritma
Eksekusi file utama untuk melihat output komparasi 3 skenario modal ($100, $250, $500):
```bash
python main.py
```

### 4. Menghasilkan Grafik Evaluasi
Untuk membuat grafik batang perbandingan *Execution Time*:
```bash
python generate_chart.py
```

## 📊 Ringkasan Hasil Eksperimen
Dari eksperimen dataset Charizard ini, algoritma **Greedy berhasil mencapai profit maksimal yang sama persis (100% konvergen) dengan Dynamic Programming** di semua skenario modal, namun dengan waktu komputasi yang **~275 kali lebih cepat** pada modal maksimal. Hal ini membuktikan bahwa metode heuristik sangat efisien untuk dataset TCG dengan distribusi harga tertentu.

## 🔗 Tautan Penting
- **Video Presentasi YouTube:** `[Masukkan Tautan Video]`
- **Dokumen Makalah (PDF):** `[Masukkan Tautan Makalah]`
