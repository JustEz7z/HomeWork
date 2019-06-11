# task 1
# def findSum(*num):
#     n = len(num)
#     sum = 0
#     for x in num:
#         sum += x
#     result = sum / n
#     print(result)
# findSum(1,2,3,4)
#  task 2
# somenum = int(input("Enter some number: "))
# def absval(num):
#     if 0 > num:
#         print(-num)
#     else:
#         print(num)
# absval(somenum)
# task 3
# def maxNumber(*nums):
#     """ We found the max number """
#     print(max(nums))

# maxNumber(15,100)
# print(maxNumber.__doc__)
# task 4
# def findAreaRectangle(a,b):
#     print("Are of rectangle is",a*b)

# def findAreaTriangle(a,b,c):
#     p = (a+b+c)/2
#     s = (p*(p-a)*(p-b)*(p-c))**0.5
#     print("Area of triangle is",s)

# def findAreaCircle(r):
#     s = 3.14*(r**2)
#     print("Area of Circle is",s)

# print("Enter pls some from thise > circle \n"+ " "*28 + "triangle\n" + " "*28 + "rectangle")
# figure = str(input("What figure?: "))

# if figure == "circle" or figure == "Circle":
#     r = float(input("Enter area: "))
#     findAreaCircle(r)
# elif figure == "triangle" or figure == "Triangle":
#     a = float(input("Enter area of a: "))
#     b = float(input("Enter area of b: "))
#     c = float(input("Enter area of c: "))
#     findAreaTriangle(a,b,c)
# elif figure == "rectangle" or figure == "Rectangle":
#     a = float(input("Enter area of a: "))
#     b = float(input("Enter area of b: "))
#     findAreaRectangle(a,b)

    
