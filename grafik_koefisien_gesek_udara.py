# MATPLOTLIB HANYA BISA DIGUNAKAN APABILA X DAN Y NYA ADALAH LIST,
# JADI KITA HARUS MENGUBAH C DAN W MENJADI LIST

import matplotlib.pyplot as plt       # --> Mengimport Library matplotlib.pyplot
from math import exp

g = 9.8
m = 68
v = 40
t = 10
N = 15
H = (19 - (-2)) / N

d = []      # --> INISISASI d MENJADI TIPE DATA LIST
r = []      # --> INISISASI r MENJADI TIPE DATA LIST

for i in range(0, 16):
    for c in range(-2, -1):
        c = c + (i * H)
        d.append(c)          # --> MEMASUKKAN c AGAR MENJADI LIST DI VARIABEL d
        print("c sekarang adalah = ", c)
        C = c                # --> MEMBEDAKAN ANTARA c dan C, agar tidak tercampur
        W = ((g * m) / C) * (1 - exp(-(C / m) * t)) - v
        print('W = ', W)
        r.append(W)          # --> MEMASUKKAN W AGAR MENJADI LIST DI VARIABEL r
        print('-------------------------')

plt.plot(d, r)           # --> command nya, jadi rumus nya plt.plot(x, y) , x itu sumbu x, y itu sumbu y
plt.xlabel("c")          # --> memberi label sumbu x menjadi c
plt.ylabel("W")          # --> memberi label sumbu y menjadi W
plt.title("Grafik Koefisien Gesek Udara")        # --> memberi Judul
plt.grid(True)          # --> membuat kotak kotak agar mudah dipahami
plt.show()              # --> menampilkan plot
