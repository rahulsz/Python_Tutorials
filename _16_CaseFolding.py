name = "Rahul"
# casefold forces to convert the string into lowercase
char = input("Enter the character: ").casefold()

if char in name.casefold():
    print("Char is present in that name")
else:
    print("Char is not present in the name")