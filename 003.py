names = ["Игорь", "Анна", "Васян"]
base_salary = [50000, 60000, 900000]
bonus = ["10.25%", "12.57%", "666.03%"]

# print([i for i in "".join(bonus).split("%") if i != ""])

print(
    {f"{i}": j * float(k)/100 for i, j, k in zip(names, base_salary, [i for i in "".join(bonus).split("%") if i != ""])})
