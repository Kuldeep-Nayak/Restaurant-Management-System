import items1
fp = open("owner1.txt")
details = fp.read()
fp.close()
def owner1():
    print("=="*50)
    print(" << OWNER PAGE >> ")
    print("=="*50)
    while True:
        pswd = input("Enter password: ")
        if pswd in details:
            print("------Login successful----")
            print("=======what do you want to do=====")
            print("1:Update item list")
            print("2:Dispatch order")
            print("3:view the item list")
            print("4:close")
            ch = int(input())
            if ch == 1:
                items1.update()
            elif ch == 2:
                items1.dispatch()
            elif ch == 3:
                fp = open('items1.txt','r')
                print(fp.read())
                fp.close()
                pass
            elif ch == 4:
                print("THANK YOU")
                break
            else:
                print("Invalid input")
        
        else:
            print("Invalid password")
