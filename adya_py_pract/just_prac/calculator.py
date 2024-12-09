a=int(input("enter a"))
b=int(input("enter b"))
op=input("enter operator")
match op:
    case "+": print (f"addition of {a} and {b} is : {a+b}")
    case "-": print (f"substraction of {a} and {b} is : {a-b}")
    case "*": print (f"multiplication of {a} and {b} is : {a*b}")
    case "/": print (f"division of {a} and {b} is : {a/b}")