salario = float(input("Informe sua renda mensal"))
despesas = float(input("Informe suas despesas mensais"))
s = (salario - despesas) * 12
milionario = 1000000 / s
print(f"Você levará {milionario} anos para atingir seu objetivo")
