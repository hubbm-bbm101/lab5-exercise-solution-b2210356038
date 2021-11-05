def sum_odd (n):
    sum=0
    for i in range(1,n+1):
        if i%2 != 0:
            sum += i
    return sum
def av_even(x):
    bolen=0
    toplam=0
    for i in range(1,x+1):
        if i % 2 ==0:
            bolen += 1
            toplam += i
    ort=toplam/bolen
    return ort


sayi=int(input("enter a number: "))
print("sum of odd numbers: ",sum_odd(sayi))
print("avarage of even numbers: ", av_even(sayi))