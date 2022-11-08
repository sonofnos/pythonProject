# for x in range(4):
#     print(x)
#
# for x in range(4):
#     for y in range(3):
#         print(f'{x}, {y}')
# numbers = [5, 2, 5, 2, 2]

numbers = [2, 2, 2, 6, 6]
for x in numbers:
    # print("x" * x)
    output = ''
    for count in range(x):
        output += 'x'
    print(output)

