a = int(input("Enter some number, what number must be four of number> "))
a1 = a % 10
a2 = int(a / 10) % 10
a3 = int(a / 100) % 10
a4 = int(a / 1000)
a00 = (a1,a2,a3,a4)
print("{4} = {3}-{2}-{1}-{0}".format(a00[0],a00[1],a00[2],a00[3],a))
