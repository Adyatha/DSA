a=int(input("enter a"))
b=int(input("enter b"))

if (a>b):
    mn=b
else:
    mn=a

for i in range(1,mn+1):
    if((a % i == 0) and (b%i == 0) ):
        hcf= i

print(f"HCF of {a} and {b} is {hcf}")

mx=max(a,b)

while(True):
    if((mx%a == 0) and (mx%b == 0)):
        break
    mx=mx+1
print(f"LCM of {a} and {b} is {mx}")