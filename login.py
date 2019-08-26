enteredusername = input("Enter your username: ")
enteredpassword = input("Enter your password: ")
username = enteredusername
password = str(enteredpassword)


if username == "john":
    if password == str(1234):
        print("login successful")
    else:
        print("login unsuccessful")
else:
    print("login unsuccessful")


