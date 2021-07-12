y=int(input("입력:"))

sum=0
for x in range(1,y):
    if(x%4==0 and x%100!=0 or x%400==0):
        sum+= 365
    else:
        sum+=354
print("y년의 1월 1일은", sum, "번째 날입니다.")
