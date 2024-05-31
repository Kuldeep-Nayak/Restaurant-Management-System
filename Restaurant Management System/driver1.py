import user1
import owner1
print("<<< WELCOME >>>")
print("You are:")
print("1:Customer 2:Owner1")
ch = int(input())
if ch == 1:
    user1.login()
elif ch == 2:
    owner1.owner1()
else:
    print("Enter Valid choice")
