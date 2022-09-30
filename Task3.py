# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n 
# и выведите на экран их сумму.
# Для n = 6: [2, 2, 2, 2, 2, 3] -> 13

n = int(input("n = "))
my_list = []
digit_sum = 0
for i in range(1, n + 1):
    val = round((1 + 1 / i) ** i)
    my_list.append(val)
    digit_sum += val

print(my_list)
print(digit_sum)

