grocery = [ "eggs", "coffee", "milk" , "bread"]

another_grocery = grocery.copy()

print(grocery)
print(id(grocery))


print()

print(another_grocery)
print(id(another_grocery))

print()

grocery += ["tea"]
print(grocery)
print(id(grocery))

print()

print(another_grocery)
print(id(another_grocery))
