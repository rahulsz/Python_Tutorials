# the default precision in Python after decimal is 15
print("{0}".format(22/7))

# Filling Characters
print("{0:100}".format(22/7))


# Fill with atleast 100 characters
print(len("{0:100}".format(22/7))) #100
print(len("{0:<100}".format(22/7))) #100

print()
print("{0:0100}".format(22/7))
# 000000000000000000000000000000000000000000000000000000000000000000000000000000000003.142857142857143
print()

# if we use just f then we mean after decimal points there must be 6 character after decimal
print("{0:100f}".format(22/7))

print()

# forcing editor to print only 2 decimal values
print("{0:.2f}".format(22/7))
#3.14

print()
print("{0:100f}".format(22/7))
print("{0:100.2f}".format(22/7))
print("{0:0100f}".format(22/7))

print()
print("{0:.100f}".format(22/7))
#3.1428571428571427937015414499910548329353332519531250000000000000000000000000000000000000000000000000


# Precision takes more precedence(importance) than filled with
print("0:3.6f".format(22/7))

# the max decimal precision in python is 51 or 52 or 53 or 54
print("{0:.78f}".format(22/7))



