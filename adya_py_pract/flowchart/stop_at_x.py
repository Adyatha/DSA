# Keep taking numbers as inputs till the user enters ‘x’, after that print sum of all.
c=0
while(True):
    n=input("enter num")
    if( n == "x"):
        print(c)
        break
    else:
        c = c+int(n)