import items1
fp = open("user1.txt")
details = fp.read()
fp.close()
def login():
    print("=="*50)
    print(" << WELCOME CUSTOMER >> ")
    print("=="*50)
    print("1.New to the app")
    print("2.Existing user")
    ch = int(input("Enter 1 if you are a new user or 2 if you are an existing user:"))
    if ch == 1:
        while True:
            name = input("Enter your name: ")
            if name in details:
                print("Name already taken.....Try Another!!")
                continue
            else:
                break
        while True:
            psr = input("Enter your password: ")
            spe = ["@","#","$","%","!","/","?"]
            if len(psr) < 6:
                print("at least 6 characters required")
                continue
            elif not any (char.isdigit() for char in psr):
                print("at least one digit")
                continue
            elif not any (char.isupper() for char in psr):
                print("at least one capital character")
                continue
            elif not any (char.islower() for char in psr):
                print("at least one small character")
                continue
            elif not any (char in spe for char in psr):
                print("at least one special character")
                continue
            else:
                print("------Login successful----")
                break

        fp = open("user1.txt","a")
        content = name+","+psr+"\n"
        fp.write(content)
        fp.close()
        items1.list()
    elif ch == 2:
        while True:
            name = input("Enter your name: ")
            if name in details:
                pswd = input("Enter password: ")
                if pswd in details:
                    print("------Login successful----")

            
             

