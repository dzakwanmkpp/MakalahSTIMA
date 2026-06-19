"""
Proyek Makalah Strategi Algoritma
Judul: Maximizing Profit in Charizard Pokémon Card PSA Grading Submissions: A 0/1 Knapsack Dynamic Programming Approach
Author: Dzakwan Muhammad Khairan Putra Purnama
"""

import pandas as pd
import time

FILE_PATH = 'dataset_charizard_75_final.csv' 
DAFTAR_MODAL = [100, 250, 500]  # Menguji skenario modal kecil, menengah, dan besar

def muat_data(filepath):
    df = pd.read_csv(filepath)
    names = df['Nama_Kartu'].tolist()
    weights = df['Biaya_Grading_USD'].tolist()  
    values = df['Profit_Bersih_USD'].tolist()   
    return names, weights, values, len(values)

def knapsack_dp(W, weights, values, n):
    # Inisialisasi matriks K dengan nol
    K = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    # Membangun matriks (Bottom-Up)
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weights[i-1] <= w:
                K[i][w] = max(values[i-1] + K[i-1][w-weights[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    
    # Proses Backtracing untuk menemukan item terpilih
    res = K[n][W]
    w = W
    item_terpilih = []
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == K[i-1][w]:
            continue
        else:
            item_terpilih.append(i-1)
            res -= values[i-1]
            w -= weights[i-1]
    return K[n][W], item_terpilih

def knapsack_greedy(W, weights, values, n):
    items = []

    # 1. Menghitung rasio profit terhadap biaya (density ratio)
    for i in range(n):
        rasio = values[i] / weights[i] if weights[i] > 0 else 0
        items.append({'index': i, 'rasio': rasio, 'weight': weights[i], 'value': values[i]})
    
    # 2. Mengurutkan kartu berdasarkan rasio tertinggi (Descending)
    items.sort(key=lambda x: x['rasio'], reverse=True)
    
    total_profit = 0
    total_weight = 0
    item_terpilih = []

    # 3. Iterasi seleksi kartu (Local Optimum Choice)
    for item in items:
        # Jika kartu masih muat di dalam sisa modal, masukkan ke subset
        if total_weight + item['weight'] <= W:
            item_terpilih.append(item['index'])
            total_profit += item['value']
            total_weight += item['weight']
    return total_profit, item_terpilih

def cetak_item_terpilih(indices, names, weights, values):
    for i in indices:
        print(f"  - {names[i]} (Biaya: ${weights[i]}, Profit: ${values[i]})")

def jalankan_komparasi():
    names, weights, values, n = muat_data(FILE_PATH)
    print("="*60)
    print(f"ANALISIS PROFIT GRADING CHARIZARD (N={n} Kartu)")
    print("="*60)
    
    for modal in DAFTAR_MODAL:
        print(f"\n>>> SKENARIO BATAS MODAL: ${modal} <<<")
        
        # Eksekusi DP
        start_dp = time.perf_counter()
        profit_dp, pilihan_dp = knapsack_dp(modal, weights, values, n)
        waktu_dp = time.perf_counter() - start_dp
        biaya_dp = sum([weights[i] for i in pilihan_dp])
        
        print(f"[DYNAMIC PROGRAMMING]")
        print(f"Profit: ${profit_dp} | Biaya Terpakai: ${biaya_dp} | Sisa: ${modal - biaya_dp}")
        print(f"Waktu: {waktu_dp:.6f} detik")
        print("Kartu Terpilih:")
        cetak_item_terpilih(pilihan_dp, names, weights, values)
        
        # Eksekusi Greedy
        start_greedy = time.perf_counter()
        profit_greedy, pilihan_greedy = knapsack_greedy(modal, weights, values, n)
        waktu_greedy = time.perf_counter() - start_greedy
        biaya_greedy = sum([weights[i] for i in pilihan_greedy])
        
        print(f"\n[GREEDY ALGORITHM]")
        print(f"Profit: ${profit_greedy} | Biaya Terpakai: ${biaya_greedy} | Sisa: ${modal - biaya_greedy}")
        print(f"Waktu: {waktu_greedy:.6f} detik")
        print("Kartu Terpilih:")
        cetak_item_terpilih(pilihan_greedy, names, weights, values)
        
        # Kesimpulan Skenario
        selisih = profit_dp - profit_greedy
        print(f"\n[KESIMPULAN SKENARIO ${modal}]")
        if selisih > 0:
            print(f"-> DP MENANG! Menghasilkan profit lebih besar ${selisih} dari Greedy.")
        elif selisih == 0:
            print("-> IMBANG! Keduanya menghasilkan profit yang sama maksimal.")
        print("-" * 60)

if __name__ == "__main__":
    jalankan_komparasi()
