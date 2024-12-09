def subsequence(p,up,l):
    if not up:
        l.append(p)
        return

    char = up[0]
    
    subsequence(p,up[1:],l)
    subsequence(char+p,up[1:],l)
    

def subsequence_with_ascii(p,up,l):
    if not up:
        l.append(p)
        return

    char = up[0]
    
    subsequence_with_ascii(p,up[1:],l)
    subsequence_with_ascii(char+p,up[1:],l)
    subsequence_with_ascii(p + str(ord(char)),up[1:],l)


p=""
up="abc"
l=[]
subsequence(p,up,l)
subsequence_with_ascii(p,up,l)
print(l)