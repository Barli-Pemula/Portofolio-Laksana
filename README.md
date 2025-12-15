# Temperature Converter

Program sederhana berbasis Python untuk mengkonversi suhu antara skala Celsius, Fahrenheit, dan Kelvin.

## Deskripsi

Program ini memungkinkan pengguna untuk mengkonversi suhu antara berbagai skala (Celsius, Fahrenheit, Kelvin) melalui antarmuka command line sederhana. Program ini dirancang sesederhana mungkin, tanpa dependensi eksternal selain Python standar.

## Penjelasan Kode

Berikut adalah penjelasan baris per baris dari kode dalam file `temperature_converter.py`:

```python
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
```
- **Fungsi `celsius_to_fahrenheit`**: Mengambil parameter `c` (suhu dalam Celsius) dan mengembalikan hasil konversi ke Fahrenheit menggunakan rumus matematika standar: `(c * 9/5) + 32`.

```python
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9
```
- **Fungsi `fahrenheit_to_celsius`**: Mengambil parameter `f` (suhu dalam Fahrenheit) dan mengembalikan hasil konversi ke Celsius menggunakan rumus: `(f - 32) * 5/9`.

```python
def celsius_to_kelvin(c):
    return c + 273.15
```
- **Fungsi `celsius_to_kelvin`**: Mengambil parameter `c` (suhu dalam Celsius) dan mengembalikan hasil konversi ke Kelvin menggunakan rumus: `c + 273.15`.

```python
def kelvin_to_celsius(k):
    return k - 273.15
```
- **Fungsi `kelvin_to_celsius`**: Mengambil parameter `k` (suhu dalam Kelvin) dan mengembalikan hasil konversi ke Celsius menggunakan rumus: `k - 273.15`.

```python
def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15
```
- **Fungsi `fahrenheit_to_kelvin`**: Mengambil parameter `f` (suhu dalam Fahrenheit) dan mengembalikan hasil konversi ke Kelvin menggunakan rumus gabungan: `(f - 32) * 5/9 + 273.15`.

```python
def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32
```
- **Fungsi `kelvin_to_fahrenheit`**: Mengambil parameter `k` (suhu dalam Kelvin) dan mengembalikan hasil konversi ke Fahrenheit menggunakan rumus gabungan: `(k - 273.15) * 9/5 + 32`.

```python
print("Konverter Suhu Sederhana")
print("1. Celsius ke Fahrenheit")
print("2. Fahrenheit ke Celsius")
print("3. Celsius ke Kelvin")
print("4. Kelvin ke Celsius")
print("5. Fahrenheit ke Kelvin")
print("6. Kelvin ke Fahrenheit")
```
- **Output menu**: Menampilkan judul program dan opsi pilihan kepada pengguna (6 opsi konversi).

```python
choice = input("Pilih (1-6): ")
temp = float(input("Masukkan suhu: "))
```
- **Input pengguna**: Meminta pengguna memilih opsi (1-6 untuk berbagai konversi) dan memasukkan nilai suhu sebagai angka desimal.

```python
if choice == '1':
    result = celsius_to_fahrenheit(temp)
    print(f"{temp} C = {result:.2f} F")
elif choice == '2':
    result = fahrenheit_to_celsius(temp)
    print(f"{temp} F = {result:.2f} C")
elif choice == '3':
    result = celsius_to_kelvin(temp)
    print(f"{temp} C = {result:.2f} K")
elif choice == '4':
    result = kelvin_to_celsius(temp)
    print(f"{temp} K = {result:.2f} C")
elif choice == '5':
    result = fahrenheit_to_kelvin(temp)
    print(f"{temp} F = {result:.2f} K")
elif choice == '6':
    result = kelvin_to_fahrenheit(temp)
    print(f"{temp} K = {result:.2f} F")
else:
    print("Pilihan tidak valid")
```
- **Logika utama**: Berdasarkan pilihan pengguna, memanggil fungsi konversi yang sesuai, menghitung hasil, dan menampilkan output dengan format 2 desimal. Mendukung 6 opsi konversi. Jika pilihan tidak valid, tampilkan pesan error.

## Persyaratan

- Python 3.x (sudah terinstall di sistem)

## Cara Menjalankan

1. Pastikan Anda berada di direktori yang sama dengan file `temperature_converter.py`.
2. Jalankan perintah berikut di terminal:
   ```
   python temperature_converter.py
   ```
   (Atau gunakan path lengkap jika diperlukan, misalnya di Windows PowerShell: `& "path/to/python.exe" temperature_converter.py`)

3. Ikuti instruksi di layar: Pilih opsi dan masukkan suhu.

## Contoh Penggunaan

```
Konverter Suhu Sederhana
1. Celsius ke Fahrenheit
2. Fahrenheit ke Celsius
3. Celsius ke Kelvin
4. Kelvin ke Celsius
5. Fahrenheit ke Kelvin
6. Kelvin ke Fahrenheit
Pilih (1-6): 1
Masukkan suhu: 25
25.0 C = 77.00 F
```

Contoh lain:
```
Pilih (1-6): 3
Masukkan suhu: 25
25.0 C = 298.15 K
```

## Lisensi

Program ini bersifat open-source dan dapat digunakan secara bebas untuk tujuan edukasi atau pribadi.