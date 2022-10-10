# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

def find_numbers(num):
    numbers=[]
    i=2
    while num>1:
        if num%i==0:
            numbers.append(i)
            while num%i==0:
                num/=i
        else:
            i+=1
    return numbers

num = find_numbers(int(input('Input number:')))
print(num)