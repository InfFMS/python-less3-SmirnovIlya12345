# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить сумму тех введённых чисел, которые делятся на 5.
a=0
while True:
    b=int(input())
    if b%5==0 and b!=0:
        a+=b
    elif b==0:
        break
print("Сумма чисел, делящихся на 5:", a)