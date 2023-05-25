def fact(r):
    f=1
    while r>0:
        f*=r
        r-=1
    return f
n = int(input())
temp = n
s=0
while temp>0:
    r=temp%10
    a=fact(r)
    s+=a
    temp=temp//10
if s == n:
    print(f"The number {n} is a strong number")
else:
    print(f"The number {n} is not a strong number")