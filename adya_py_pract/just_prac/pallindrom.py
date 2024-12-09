# To find out whether the given String is Palindrome or not.
str1 = input("enter the string")
str1l = list(str1)
print(str1l)
str1l.reverse()
str2 = "".join(str1l)
if str1 == str2:
    print("pallindrome")
else:
    print("not pallindrome")