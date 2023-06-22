#          012345678      
string1 = "Rahul Zmr"
#         -8      -1

print()
number = "1,487,678,890,908,890,987"
sep = number[1::4]
print(sep)  # important concept a lot of MNC are working on it.

values = "".join(char if char not in sep else " " for char in number).split()
print([int(val) for val in values])  # real world scenario
print()

# Backward Slicing

alphabets = 'abcdefghijklmnopqrstuvwxyz'

print(alphabets[0:26])
print(alphabets[25::-1]) # important thing when we say -1 automatically program know this line should print from backward .
print(alphabets[::-1])
print(alphabets[25::-1])
