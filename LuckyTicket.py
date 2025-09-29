number = str(input("Введите номер билета: "))
sum_first = int(number[0]) + int(number[1]) + int(number[2])
sum_second = int(number[3]) + int(number[4]) + int(number[5])

if sum_first == sum_second:
    print("Счастливый билет")
else:
    print("Несчастливый билет")
