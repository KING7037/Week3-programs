a = input("Enter your new password: ")
b = input("Enter your new password again: ")
if a == b:
    if len(a)>=8 and len(a)<=12:
        print("Password Set")
    else:
        print("Password must be 8-12 charcters")