import math

# 1. Kuadrat (a)
kuadrat = lambda x: x ** 2

# 2. Pythagoras/Jarak (b)
jarak = lambda x, y: math.sqrt(x**2 + y**2)

# 3. Rata-rata (c)
rata_rata = lambda *args: sum(args) / len(args)

# 4. Filter Karakter Unik dan Gabung (d)
unik_dan_gabung = lambda s: " ".join(set(s))

# --- Cek Hasil ---
print(f"Kuadrat(5): {kuadrat(5)}")
print(f"Jarak(3, 4): {jarak(3, 4)}")
print(f"Rata-rata(10, 20, 30): {rata_rata(10, 20, 30)}")
print(f"Unik('hello world'): '{unik_dan_gabung('hello world')}'")