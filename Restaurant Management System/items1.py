import random
def list():
    print("=="*50)
    print(" << CHOOSE ITEMS FROM THE MENU >> ")
    print("=="*50)
    print(" << ITEMS LIST >> ")
    print("=="*50)
    print('No,Dish,Price\n')

    fp = open('items1.txt','r')
    records = fp.readlines()
    fp.close()
    for i in records:
        print(i)
    orderno = str(random.randint(1000,9000))
    items1 = "Orderno: " +orderno+"\n\n"
    order = str(orderno)
    total = 0

    while True:
        dish = input("Choose the dish number:")
        quantity = int(input("Enter Quantity:"))
        for i in range(len(records)):
            rec = records[i].rstrip().split(",")
            if rec[0] == dish:
                price = int(rec[2])*quantity
                total += price
                items1 = items1+rec[1]+" "+str(quantity)+"\n"
                order = order+","+rec[1]+" "+str(quantity)+","
                break
        else:
                print("Invalid Input,Enter correct dish number")
        c = input("Press y to choose another dish: ").lower()
        if c != "y":
                break
    print("\n*********YOUR ORDER********")
    print(items1)
    print(f'------->TOTAL AMOUNT: Rs.{total} <--------')
    confirm = input("Confirm(y): ").lower()
    if confirm == "y":
            fp = open('orderlist1.txt','a')
            order=order+"\n"
            fp.writelines(order)
            fp.close()
    print("\n******** ORDER CONFIRMED **********")

def update():
    print("1:Add New Item")
    print("2:Delete Item")
    print("3:Update Price")
    ch = int(input("-----Choose 1/2/3------"))
    if ch == 1:
        no = input("Item number:")
        name = input("Item name:")
        price = input("Item price:")
        rec = "\n"+no+","+name+","+price+"\n"
        fp = open('items1.txt','a')
        fp.write(rec)
        fp.close()
    elif ch == 2:
        no = input("Enter the item number to be deleted:")
        fp = open('items1.txt','r')
        records = fp.readlines()
        fp.close()
        for i in range(len(records)):
            if no == records[i].split(',')[0]:
                del records[i]
                break
        else:
                print("Input correct item number")
        fp = open('items1.txt','w')
        fp.writelines(records)
        fp.close()
           
    elif ch == 3:
        n = input("item name:")
        no = input("Enter item number:")
        newprice = input("Enter updated price:")
        fp = open('items1.txt')
        records = fp.readlines()
        fp.close()
        for i in range(len(records)):
            if no in records[i]:
                records[i] = "\n"+no+","+n+","+newprice+"\n"
                print('Price updated')
                print(records)
                fp = open('items1.txt','w')
                fp.writelines(records)
                fp.close()
            else:
                print("Invalid")
                
def dispatch():
    print("=="*50)
    print("  ------------ ORDERS IN THE LIST -------  ")
    print("=="*50)
    fp = open("orderlist1.txt")
    details = fp.readlines()
    fp.close()
    for i in range(len(details)):
        print(details[i])
    while True:
        l1 = []
        flag = 0
        inp = (input("Enter the order no: "))
        for i in range(len(details)):
            k = details[i].rstrip().split(",")
            if k[0] == inp:
                flag = 1
            else:
                l1.append(details[i])
        if flag == 0:
            print("The order number do not exist choose another item number")
            continue
        else:
            print(l1)
            fp = open("orderlist1.txt","w")
            fp.writelines(l1)
            fp.close()
            print("-----Order dispatched!!!-----")
            break

            
            


