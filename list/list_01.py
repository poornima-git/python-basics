#Without using Function 

# nm = [1, 2, 3, 4, 5, 6]
# num = []
# for i in range(len(nm)):
#     if

# my_num =[1,2,3,4,5]
# print(type(my_num))
# pos = int(input("Enter the position : "))
# value_l =  list(input("enter the number"))
# print(type(value_l))
# result_l = my_num[:pos] + value_l + my_num[pos:]
# print(result_l)

# my_list = [1,2,3,4]
# val_i =input("enter number(comma seperate):").split(',')
# val_i = [int(value.strip()) for value in val_i]
# pos= int(input("enter the index"))
# my_list = my_list[:pos] + val_i + my_list[pos:]
# print("list is:", my_list)

# list1 = [1, 2, 3, 4, 5]
# list2 = [x for x in list1 if x != 2]
# print(list2)


# list_1 = [1,2,3,4,5]
# del_pos = int(input("enter the position"))

# my_list = list(input("Entrer "))
# index_r = int(input("enter a position:"))
# my_list = my_list[:index_r - 1] + my_list[index_r:]
# print (my_list)

# num = int(input("enter any number"))
# for i in range(0, num):
#     for j in range(0, i+1):
#      print("*", end= " ")
#     print()       

# for i in range(5):
#     for j in range(i):
#         print("*", end = " ")
#     print()


my_list = input("enter number(comma seperate):").split(',')
my_list = [int(i.strip()) for i in my_list]
index_r = int(input("enter a position:"))
my_list = my_list[:index_r-1] + my_list[index_r:]
print (my_list)