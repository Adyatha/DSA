a="komal"
tar=input("enter the character to be searched")

def linear(a,tar):
    s=list(a)
    for idx,i in enumerate(s):
        if i == tar:
            return idx
    return -1

res = linear(a,tar)

if res != -1:
    print(f"value found at index {res}")
else:
    print("value not found")
    