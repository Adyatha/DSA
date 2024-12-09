#  To find Armstrong Number between two given number.
def armstrong(n):
    sum=0
    org=n
    while (n/10 != 0):
        num = n % 10
        sum = sum + (num *num *num)
        n = n//10
    return sum == org

a = int(input("enter num a"))
b = int(input("enter num b"))

while a<=b :
    if armstrong(a):
       print(a)
    a+=1


