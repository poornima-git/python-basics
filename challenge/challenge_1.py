from challenge import find_max
# challenge.find_max()

numbers = [10,3,6,2]
max = find_max(numbers)
print(max)



#   this is saved in challenge .py   
def find_max(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max 