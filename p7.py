def count_vowels(s):
    vowels=0
    for i in s :
        if i.lower() in "aeiou":
            vowels+=1
    return vowels
    
a=input("enter a string :")
obj=count_vowels(a)
print(obj)