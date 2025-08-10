weight = int(input('Weight: '))
unit = input("(G)rams or (K)gs: ")
converted = weight / 1000
if unit.upper() == 'G':
    print(f"You are {converted} kilos")
elif unit.upper() == 'K':
    converted = weight *1000
    print(f"You are {converted} grams")