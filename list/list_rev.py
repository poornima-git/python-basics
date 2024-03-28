# reverse of a list

# my_list = [100,200,300,400]
# my_list.reverse()
# print(my_list)

# concatenate of 2 lists

# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# a = list1[0] + list2[0]
# b = list1[1] + list2[1]
# c = list1[2] + list2[2]
# d = list1[3] + list2[3]
# print(a,"",b,"",c,"",d)

# concatenation of 2 lists with zip() 

# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# list3 = [i + j for i,j in zip(list1, list2)]
# print(list3)


# turn lists items into squares 

# lists = [2,3,4,5,6,7]
# lists1 = []
# for i in lists:
#    lists1.append(i * i)
# print(lists1)


# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# res = [i + j for i in list1 for j in list2]
# print(res)

# iterate both list simultaneously
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# for i in list1:
#     for j in list2[::-1]:
#         print(i,j)

# rows = 5
# for i in range(rows):
#     for j in range(i+1):
#         print("*", end = " ")
#     print()


# sum = 0
# num = int(input("enter a number"))
# for i in range(1, num+1):
#     sum += i
# print(sum)


# num = 2
# for i in range
# (11):
#     res = i * 2
#     print(num, "*", i ,"=" ,res)

# numbers = [12, 75, 150, 180, 145, 525, 50]
# for i in numbers:
#     if i > 150:
#         continue
#     elif i > 500:
#         break
#     elif i % 5 == 0:
#         print(i)

# reverse number pattern

# rows = int(input("enter any number"))
# for i in range(0,rows):
#     for j in range(rows - i, 0, -1):
#         print(j , end = " ")
#     print()

# list1 = [10, 20, 30, 40, 50]
# list1.reverse()
# print(list1)