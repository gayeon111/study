odd=0
even=0

for i in range(1,101):
    if(i%2==0):
        even=even+i
    else:
        odd=odd+i
print(odd,even, even-odd)
