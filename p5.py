def copy(*str):
    for i in str:
        if len(i)<0 or len(i)>10:
            return "the length exceeds"
        else :
            return i
        
sai=input("enter a string :")
obj=copy(sai)
print(obj)

