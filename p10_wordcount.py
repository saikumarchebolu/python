def count(str):
    # s=1
    # a=" "
    # for i in str :
    #     if a in str:
    #         s=s+1
    # return s
        words=str.split()
        return len(words)
sai=input("enter a string :")
obj=count(sai)
print(obj)