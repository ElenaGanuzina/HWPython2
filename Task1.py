# 1. Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.

number = float(input())
digit_sum = 0
sth = len(str(number))
number = number * 10 ** (sth - 2)

while number:
    digit_sum += number % 10
    number //= 10
print (int (digit_sum))
