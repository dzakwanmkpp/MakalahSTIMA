import matplotlib.pyplot as plt
import numpy as np

# Data dari hasil eksperimen terminal kita
budgets = ['$100', '$250', '$500']
dp_times = [0.001932, 0.006388, 0.013196]
greedy_times = [0.000047, 0.000072, 0.000048]

x = np.arange(len(budgets))  # Lokasi label di sumbu X
width = 0.35  # Lebar setiap batang (bar)

fig, ax = plt.subplots(figsize=(8, 6))
# Membuat bar untuk DP (warna merah muda) dan Greedy (warna biru muda)
rects1 = ax.bar(x - width/2, dp_times, width, label='Dynamic Programming', color='#ef4444', edgecolor='black')
rects2 = ax.bar(x + width/2, greedy_times, width, label='Greedy Algorithm', color='#3b82f6', edgecolor='black')

# Menambahkan teks label, judul, dan modifikasi sumbu X dan Y
ax.set_ylabel('Execution Time (seconds)', fontsize=11, fontweight='bold')
ax.set_xlabel('Budget Constraint (USD)', fontsize=11, fontweight='bold')
ax.set_title('Fig. 5. Execution Time Comparison: DP vs Greedy', fontsize=13, fontweight='bold', pad=15)
ax.set_xticks(x)
ax.set_xticklabels(budgets, fontsize=11)
ax.legend(fontsize=10)

# Fungsi untuk menambahkan angka spesifik di atas setiap batang agar terbaca jelas
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height:.6f}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 poin ke atas dari ujung bar
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=9)

autolabel(rects1)
autolabel(rects2)

# Menambahkan grid horizontal agar nilai lebih mudah dibaca
ax.grid(axis='y', linestyle='--', alpha=0.7)

fig.tight_layout()

# Menyimpan grafik sebagai file PNG beresolusi tinggi (300 dpi) standar IEEE / Jurnal
file_name = 'Fig5_Execution_Time_Comparison.png'
plt.savefig(file_name, dpi=300)
print(f"Grafik berhasil dibuat dan disimpan sebagai '{file_name}' di folder Anda!")
