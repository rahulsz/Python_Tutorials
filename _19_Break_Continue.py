shopping_items = ["eggs","bananas","maggie","stale apples","bread","curd"]

for item in shopping_items:
    if item !="statle apples":
       print("{0} Added to cart".format(item))

print()
print()

for item in shopping_items:
    if item == "stale apples":
        continue
    print("{0} Added to cart".format(item))

print()
print()

for item in shopping_items:
    if item == "stale apples":
        break
    print("{0} Added to cart".format(item))