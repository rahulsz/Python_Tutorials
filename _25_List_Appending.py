
# append

choice ="_"

# 1. Curd
# 2. Bread

# 12345 0

grocery_items =[]

while choice !='0':

    if choice in "1234":
        print("Adding {0} to Big Basket Cart".format(choice))

        if choice == "1":
            grocery_items.append("Butter")
        if choice == "2":
            grocery_items.append("Bread") 
        if choice == "3":
            grocery_items.append("Milk")
        if choice == "4":
            grocery_items.append("Tea Bag")

    else:
        print("Add items for the following available ones: ")
        print("1. Butter")        
        print("2. Bread")        
        print("3. Milk")        
        print("4. Tea Bag")
        print("0. Exit")

    choice = input()
print(grocery_items)


