
# print(*(f"{i}*{j} = {i*j} \t\t" if j==10 else f"{i}*{j} = {i*j}"for i in range(2,11) for j in range(2,11)))

print(*(f"{j}*{i} = {i*j}\n" if j==10 else "".join(f"{j}*{i} = {i*j} ") for i in range(2,11) for j in range(2,11)))
