numbers = [5, 2, 5, 2, 2]


# nested loop
for item in numbers: 
    result = ''
    for i in range(item):
        result += 'X'
    print(result)
    
