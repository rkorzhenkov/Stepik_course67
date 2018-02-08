
""" Когда сумма введенных чисел станет 0,вывести результат суммы квадратов этих чисел """
a1 = int(input())
sum_squares = a1
sum_squares2 = 0 + abs(a1**2)
while sum_squares != 0:
    a1 = int(input())
    sum_squares = sum_squares + a1
    sum_squares2 = sum_squares2 + abs(a1)**2
print(sum_squares2)