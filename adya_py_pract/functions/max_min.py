def max(n1,n2,n3):
    if n1 > n2:
        if n3 > n1:
            return n3
        else:
            return n1
    else:
        if n3 > n2:
            return n3
        else:
            return n2
            
def min(n1,n2,n3):
    if n1<n2:
        if n3<n1:
            return n3
        else:
            return n1
    else:
        if n3<n2:
            return n3
        else:
            return n2

print(min(1,45,66))
print(max(1,45,66))
