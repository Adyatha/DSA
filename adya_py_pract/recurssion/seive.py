n=20
i=2
prime=[False]*(n+1)
while(i*i <= n ):
    if not prime[i]:
        for j in range(i*i,n+1,i):
            prime[j] = True 
    i+=1

for i in range(2, n+1):
    if not prime[i]:
        print(i, end=" ")


