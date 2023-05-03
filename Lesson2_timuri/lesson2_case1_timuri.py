a = float(input("Введите длину стороны квадрата в см: "))
per = round(a + a + a + a, 2)
plosh = round(a * a, 2)
dia = round(a * (2 ** 0.5), 2)

result = f"""
Периметр квадрата = {per} см
Площадь квадрата = {plosh} см2
Диагональ квадрата = {dia} см
"""

print(result)
