

# creating an empty list
my_list = []
 
# number of elements as input
n = int(input("Enter number of elements : "))
 
# iterating till the range
for i in range(0, n):
    ele = int(input())
    # adding the element
    my_list.append(ele)

my_list = input("enter a lists(comma:").split(',')
my_list = [i.strip() for i in my_list]
guk = list(my_list)
list_pos = int(input("enter the position"))
my_list = my_list[:list_pos - 1] + my_list[list_pos:]
print(list(my_list))
print(type(list_pos))
