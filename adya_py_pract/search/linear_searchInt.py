a=[1,45,44,2]
tar=int(input("enter the number to be searched"))

def linear(a,tar):
    for idx,i in enumerate(a):
        if i == tar:
            return idx
    return -1

res = linear(a,tar)

if res != -1:
    print(f"value found at index {res}")
else:
    print("value not found")
    