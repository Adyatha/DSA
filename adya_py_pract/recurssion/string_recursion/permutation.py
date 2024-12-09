def permutation(p,up,l):
    if not up:
        l.append(p)
        return

    char = up[0]

    for i in range(0,len(p)+1):
        permutation(p[0:i]  + char + p[i:], up[1:],l)
        
    return l

def perm(s):
    l=[]
    p=""
    up=s
    permutation(p,up,l)
    return l

s="abc"
l= perm(s)
print(l)