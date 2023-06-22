instock_items=["Butter",
               "Bread",
               "Cream",
               "Milk",
               "Curd"
               ]

choice ="_"
grocery_items=[]

while choice !='0':
    if choice in "12345":
        print(("Adding {0}".format(choice)))
        if choice == '1':
            grocery_items.append("Butter")
        if choice == '2':
            grocery_items.append("Bread")
        if choice == '3':
            grocery_items.append("Cream")
        if choice == '4':
            grocery_items.append("Milk")
        if choice == '5':
            grocery_items.append("Curd")
    
    else:
        print("0 to Exit if not then, ")
        print("Add items to basket from the following:")
        for item in instock_items:
            print("{0}. {1}".format(instock_items.index(item) + 1, item))
    
    choice = input()

print(grocery_items)