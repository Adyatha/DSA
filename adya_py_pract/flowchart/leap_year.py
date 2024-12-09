# Input a year and find whether it is a leap year or not.

yr = int(input("enter the year"))
if((yr % 400 == 0) and (yr % 100 == 0)):
    print("its a leap year")
elif((yr % 4 == 0) and (yr % 100 != 0)):
    print("its a leap year")
else:
    print("not a leap year")

# method 2

# if((yr % 400 == 0) or (yr % 100 != 0) and (yr % 4 == 0)):
#     print("its a leap year")
# else:
#     print("not a leap year")

