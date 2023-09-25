n=int(input("enter the number of n "))
s=0
count=1
if n<1:
    print("invalid input")
else:
    while count<=n:
        s=s+(1/count)
        count+=1
print(f'{s:.9f}')