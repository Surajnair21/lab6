n=int(input("enter the number of n "))
s=0
fact=1
count=1
if n<1:
    print("invalid input")
else:
    while count<=n:
        fact=fact*count
        s=s+(1/fact)
        count+=1
print(f'{s:.9f}')