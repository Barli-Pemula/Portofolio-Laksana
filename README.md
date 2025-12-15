# Temperature Converter

Program sederhana berbasis Python untuk mengkonversi suhu antara skala Celsius dan Fahrenheit.

## Deskripsi

Program ini memungkinkan pengguna untuk mengkonversi suhu dari Celsius ke Fahrenheit atau sebaliknya melalui antarmuka command line sederhana. Program ini dirancang sesederhana mungkin, tanpa dependensi eksternal selain Python standar.

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
print("Konverter Suhu Sederhana")
print("1. Celsius ke Fahrenheit")
print("2. Fahrenheit ke Celsius")
```
- **Output menu**: Menampilkan judul program dan opsi pilihan kepada pengguna.

```python
choice = input("Pilih (1 atau 2): ")
temp = float(input("Masukkan suhu: "))
```
- **Input pengguna**: Meminta pengguna memilih opsi (1 untuk Celsius ke Fahrenheit, 2 untuk sebaliknya) dan memasukkan nilai suhu sebagai angka desimal.

```python
if choice == '1':
    result = celsius_to_fahrenheit(temp)
    print(f"{temp} C = {result:.2f} F")
elif choice == '2':
    result = fahrenheit_to_celsius(temp)
    print(f"{temp} F = {result:.2f} C")
else:
    print("Pilihan tidak valid")
```
- **Logika utama**: Berdasarkan pilihan pengguna, memanggil fungsi konversi yang sesuai, menghitung hasil, dan menampilkan output dengan format 2 desimal. Jika pilihan tidak valid, tampilkan pesan error.

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
Pilih (1 atau 2): 1
Masukkan suhu: 25
25.0 C = 77.00 F
```

## Lisensi

Program ini bersifat open-source dan dapat digunakan secara bebas untuk tujuan edukasi atau pribadi.