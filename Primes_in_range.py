def prime(n):
    if n==1: return 0
    for i in range(2,int(n**(0.5))+1):
        if n%i==0:
            return 0
    return 1

m = int(input())
n = int(input())
p = 0
for i in range(m,n+1):
    if prime(i): p+=1
print(p)