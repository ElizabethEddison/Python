def AddStock():
    addmore = input("Do you want to add stock?")
    while addmore == "yes":
        item_name = input("Enter item name")
        item_type = input("Enter type")
        item_manu =input("Enter manufacturer")
        item_price = input("Enter price")
        file = open ("stocklist.doc", "a")
        file.write(item_name + "\t")
        file.write(item_type+ "\t")
        file.write(item_manu + "\t" +"\t")
        file.write(item_price+ "\t")
        file.write("\n")
        file.close()
        addmore = input("Do you want to add more?")
        
def AddCustomer():
    addmore = input("Do you want to add a customer?")
    while addmore == "yes":
        cmname = input("Customers name?")
        cmaddress = input("Customers address?")
        cmemail = input("Customer email address?")
        cmphone = input("Customer phone number?")
        file = open("customerlist.doc", "a")
        file.write(cmname + "\t")
        file.write(cmaddress+ "\t")
        file.write(cmemail + "\t" +"\t")
        file.write(cmphone+ "\t")
        file.write("\n")
        file.close()
        addmore = input("Do you want to add more?")

def AddSale():
    addmore = input("Do you want to add a sale?")
    while addmore == "yes":
        saledate = input("Date of sale")
        item = input("Item purchased?")
        price = float(input("Price of item"))
        qty = int(input("Quantity"))
        totalprice = price * qty
        price2 = str(price)
        qty2 = str(qty)
        totalp = str(totalprice)
        file = open("salelist.doc", "a")
        file.write(saledate  + "\t")
        file.write(item+ "\t")
        file.write(price2 +"\t" )
        file.write(qty2 + "\t")
        file.write(totalp + "\t")
        file.write("\n")
        file.close()
        addmore = input("Do you want to add more?")
    
def ViewStock():
    file = open("stocklist.doc", "r")
    print(file.read())
    file.close()

def ViewCustomers():
    file = open("customerlist.doc", "r")
    print(file.read())
    file.close()

def ViewSales():
    file = open("salelist.doc", "r")
    print(file.read())
    file.close()
    
while True:
    print("please chose an option")
    print("option 1: Add new stock item")
    print("option 2: Add customer")
    print("option 3: Add new sale")
    print("option 4: View stock")
    print("option 5: View customer")
    print("option 6: View sales")

    option = input("Enter option")

    if option == "1":
        AddStock()
    elif option =="2":
        AddCustomer()
    elif option =="3":
        AddSale()
    elif option =="4":
        ViewStock()
    elif option =="5":
        ViewCustomers()
    elif option =="6":
        ViewSales()
