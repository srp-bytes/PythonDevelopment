weight = float(input("Weight: "))
type = input("(K)g or (L)bs: ")
upper_type = type
if upper_type == 'K':
    weight_in_lb = weight * 0.45
    print("Weight in (L)bs: " + str(weight_in_lb))
elif upper_type == 'L':
    weight_in_kg = weight // 0.45
    print("Weight in (K)g: " + str(weight_in_kg))
else:
    print("Invalid input" + str(upper_type))
