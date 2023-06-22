# Print the tables for number from 1 to 5 till 10
for i in range(1,6):  #(5 times)
    for j in range (1,11):  #(10 times)
        print("{0} x {1} = {2}".format(i,j,i*j))
    print("----------")