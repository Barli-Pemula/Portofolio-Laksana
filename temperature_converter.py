def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9


print("Konverter Suhu Sederhana")
print("1. Celsius ke Fahrenheit")
print("2. Fahrenheit ke Celsius")

choice = input("Pilih (1 atau 2): ")
temp = float(input("Masukkan suhu: "))

if choice == '1':
    result = celsius_to_fahrenheit(temp)
    print(f"{temp} C = {result:.2f} F")
elif choice == '2':
    result = fahrenheit_to_celsius(temp)
    print(f"{temp} F = {result:.2f} C")
else:
    print("Pilihan tidak valid")
