# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# 1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
# - 4 -> [1, 2, 6, 24]

number = int(input())
if number < 0: 
    number *= -1
elif number == 0:
    print ("Error! You've entered 0.")

digit_sum = 1
for i in range(number):
    digit_sum *= i+1
    print(digit_sum, end = " ")        