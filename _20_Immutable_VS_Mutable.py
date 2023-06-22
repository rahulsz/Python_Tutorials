# result = True
# another_result = result

# print(id(result))
# print(id(another_result))

# print()

# result = False  # new id is created but it's not changed it's orginal address
# print(id(result))



# 10 =4340939712 -------binded -------(result)
result = 10
print(id(result))

print()

# 11 = 4340939744 -------re-binding------(result)
result = 11
print(id(result))

print()

name = "Rahul"
print(id(name))
print(name)

print()

name += "Tate"
print(name)
print(id(result))

# if you tried to change thr value contained in an immutable object , so rather thn the object updating 
# its own value, a new ID/address(cpython) is created for that new value and the immutable object is
# unbinded from previous ID and binding now, the new ID of value.


grocery = [ "eggs", "coffee", "milk" , "bread"]

another_grocery = grocery

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





























































#result = "PrepInsta"
#print(id(result))
#print(result)

#print()

#result += "Prime"
#print(result)
#print(id(result))

# If you try to change the value contained in an immutable object, so rather than the object updating
# its own value, a new ID/address(cpython) is created for that new value and the immuatble object is
# unbinded from previous ID and binding now, the new ID of value
