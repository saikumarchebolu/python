import random
n=random.randint(1,100)
i=-1
guesses=0
while(i!=n):
    guesses+=1
    i=int(input("enter a two digit number : "))
    if(i>n):
        print("enter lower number")
    elif(i<n):
        print("enter higher number")
print(f"you guess the correct number in {guesses} guesses ,and the number is {n}")