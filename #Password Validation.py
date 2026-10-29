#Password Validation
password = input("Enter your password: ")

if len(password) >= 8:
    print("Valid Password")
else:
    print("Password must contain at least 8 characters")

