input_weight = input("What's your weight: ")

weight_unit = input("(L)bs or (K)g: ")

unit = ''

if weight_unit == 'l' or weight_unit == 'L':
    input_weight = int(input_weight) * 0.45
    unit = 'kilos'

elif weight_unit == 'k' or weight_unit == 'K':
    input_weight = int(input_weight) // 0.45
    unit = 'pounds'

print(f"You weigh {input_weight} {unit}")
