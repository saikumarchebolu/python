def mul(*num):
    sum=1
    for i in num :
        if i<1 and i>100:
            return "enter number between 1 and 100"
        else :
            sum=sum*i
    return sum

n1=int(input("enter first number :"))
n2=int(input("enter 2 nd number :"))
n3=int(input("enter 3rd numbber :"))
sai=mul(n1,n2,n3)
print(sai)