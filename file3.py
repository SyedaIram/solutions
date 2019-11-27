n=int(input("enter the number"))
sum1=0
for i in range(1,n+1):
    sum1=sum1+(i*i)
sum2=0
for i in range(1,n+1):
    sum2=sum2+i
sum3=(sum2*sum2)-sum1
print(sum3)
    
