import random
otp=random.randint(000000,999999)
# print(f"your otp is : {otp}")

entered_otp=int(input("enter your 6 digits otp : "))
if entered_otp==otp:
    print("authentication sucess")
else:
    print("invalid otp,please try again")
