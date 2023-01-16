# names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
#
# print(names[2:2])


numbers = [34, 58, 67, 63, 12, 4, 59, 2]
len_num = len(numbers)
x = 0
max_item = 0

for item in numbers:
    while len_num < x:
        x += 1
        if max_item < item:
            max_item = item

print(max_item)
