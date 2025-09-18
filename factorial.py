def factorialofgivennumber():
    n=int(input("enter a number :"))
# i=1
# pp=1
# while(i<=n):
#     pp=pp*i
#     i+=1
# print(pp)

    p=1
    for i in range(1,n+1):
        p=p*i
    print(p)

factorialofgivennumber()