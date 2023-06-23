grocery = [ "eggs", "coffee", "milk" , "bread"]

another_grocery = grocery

list1 = list2 = list3 = list4 = grocery  # basically 1 id/address is created we are refering from multiple names that's it

grocery.append("butter")
# grocery = grocery + ["butter"]

print(grocery)

print(list1)



# append


choice ="_"
grocery_things = []

while choice !="0":
    choice = input("Enter name of item , you want to add to big Basket Cart: ")
    if choice != "0":
        grocery_things.append(choice)

print(grocery_things)
