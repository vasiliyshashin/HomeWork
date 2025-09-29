year = int(input("Введите год: "))
if year % 4 == 0:
    year = "Високосный"
else:
    year = "Обычныый год"
print(year)