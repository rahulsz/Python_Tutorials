




#                       1         2
#             01234567890123456789012345
alphabets = " abcdefghijklmnopqrstuvwxyz "
#            -65432109876543210987654321
#                   2          1
# mno
print(alphabets[12:15])
print(alphabets[-14:-11])
print()

# onm
print(alphabets[14:11:-1])
print(alphabets[-12:-15:-1])
print(alphabets[-12:11:-1])
print(alphabets[14:-15:-1])
print()

# ehkn
print(alphabets[4:15:3])
print(alphabets[-22:-10:3])
print()

# nkhe
print(alphabets[-13:3:-3])
print(alphabets[-13:-23:-3])
print()

# abcdefgh
print(alphabets[0:8])
print(alphabets[:8])
print(alphabets[-26:8])
print(alphabets[-26:-18])
print()

# last 20 characters( in reverse order)
print(alphabets[-1:21:-1])
print(alphabets[25:5:-1])
print()

# first 20 characters
print(alphabets[0:20])
print(alphabets[:20])

# checking length
print(len(alphabets))
print(len(alphabets[0:20]))
