# a=int(input("enter a"))
# n1=0
# n2=1
# nextnum = n2
# c=0
# while (c<a):
#     print(nextnum , end= " ")
#     n1,n2 = n2,nextnum
#     nextnum = n1+n2
#     c+=1
# print()

# method 2

def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1) + fib(n-2)
        
t=int(input("enter num"))

for i in range(0,t):  
    print(fib(i))