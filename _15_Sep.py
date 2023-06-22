number = "121,333,555,555,555,5555,555,555,5888,999"
sep = ""
value =""

#for char in number:
 #   if not char.isnumeric():
    #    sep = sep + char

#print(seperator)

for char in number:
    if char.isnumeric():
        value = value + char
print(value)
print([int(val) for val in value])
