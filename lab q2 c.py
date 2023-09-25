n=int(input())
x=int(input())
if n<0 or x<0:
    print("invalid input")
else:
    sum=1
    for i in range(1,n+1):
        sum=sum+((x**i)/i)
    print(f'{sum:.9f}')