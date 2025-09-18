def add(*num):
    sum=0
    for i in num :
        sum=sum+i
    return sum

n1=int(input("enter first number :"))
n2=int(input("enter 2 nd number :"))
sai=add(n1,n2)
print(sai)