def reverse(*str):
    for i in str:
        if len(i)<0 or len(i)>10:
            return "the length exceeds"
        else :
            return i[::-1]
        
sai=input("enter a string :")
obj=reverse(sai)
print(obj)