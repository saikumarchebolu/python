def plaindrome(str):
    for i in str:
        reverse=i[::-1]
        if i==reverse:
            return "your string is plaindrome"
        else :
            return "your string is not a plaindrome"
        
sai=input("enter a string :")
obj=plaindrome(sai)
print(obj)