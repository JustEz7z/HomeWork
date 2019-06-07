# 1
# number = int(input("Enter number: "))
# if number % 2 == 0:
#     print("{} is parne".format(number))
# else:
#     print("{} is neparne".format(number))
# ################################################

# num = int(input("Enter some number: "))
# i = 1
# factorial = 1
# while i <= num:
#     factorial *= i
#     i+= 1
#     print(factorial)

#################################################
# 2
# num = list(range(100))
# leng = len(num)
# i = 0
# while i <= leng:
#     i += 1
#     if i == leng:
#         continue
#     elif i % 2 == 0:
#         print(i)
#     else:
#         pass
# print("\n")
# for ind in num:
#     if ind == 0:
#         continue
#     elif ind % 2 == 0:
#         print(ind)

###################################################
# 3
# num = list(range(100))
# leng = len(num)
# i = 0
# while i < leng:
#     if i % 2 == 0:
#         print(i+1)
#     else:
#         pass
#     i += 1
    
# print("\n")
# for ind in num:
#     if ind % 2 == 0:
#         print(ind+1)
#     else:
#         continue

#####################################################
# 4
# list_number = list(range(10))
# j = 0
# for x in list_number:
#     list_number[j] = float(x)
#     j += 1
# print(list_number)
####################################################
# 5
# list_number = []
# x = 0
# j = 0
# i = 1
# n = int(input("Enter number: "))
# for x in range(n):
#     list_number.append(int(input("Enter some number: ")))
# while j <= n :
#     result = list_number[j] + list_number[i]
#     list_number.append(result)
#     j+=1
#     i+=1
# print(list_number)

####################################################
# 6
list_string = []
for x in range(4):
    list_string.append(input("Enter some text type string: "))
for x in list_string:
    print(x)
    # 7
    print(x,end='#')
#####################################################