n=str(input("enter the sentence"))
l=len(n)
s=1
vcount=0
ccount=0
c=" "
v="aeiou"
for char in n:
    if char in v:
        vcount+=1
    elif char in c:
        s+=1
    else:
        ccount+=1
print("vowels ",vcount)
print("consonants ",ccount)
print("words ",s)
