#
# is_hot = False
# is_cold = True
#
#
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
#
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
#
# else:
#     print("It's a lovely day")
#
#
# print("Enjoy your day")


house_price = 1000000
has_good_credit = False
down_payment = 0

if has_good_credit:
    print("You need to make a 10% down payment")
    down_payment = house_price//10
else:
    print("You need to make a 20% down payment")
    down_payment = house_price//5

print(f"Your down payment is ${down_payment}")
