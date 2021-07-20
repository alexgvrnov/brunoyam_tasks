l = 109
t = int(input("Время:"))
v = int(input("Скорость:"))
otm = (t * v) - ((t * v) // l) * l
print("Отметка:",otm)