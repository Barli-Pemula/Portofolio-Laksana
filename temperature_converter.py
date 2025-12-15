def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9


def celsius_to_kelvin(c):
    return c + 273.15


def kelvin_to_celsius(k):
    return k - 273.15


def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15


def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32


print("Konverter Suhu Sederhana")
print("1. Celsius ke Fahrenheit")
print("2. Fahrenheit ke Celsius")
print("3. Celsius ke Kelvin")
print("4. Kelvin ke Celsius")
print("5. Fahrenheit ke Kelvin")
print("6. Kelvin ke Fahrenheit")

choice = input("Pilih (1-6): ")
temp = float(input("Masukkan suhu: "))

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
