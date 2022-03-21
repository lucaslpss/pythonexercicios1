dias = float(input("Digite a quantidade de dias trabalhados dentro de um mês"))
salarioDia = 70
salario = dias * salarioDia
desconto = (dias * salarioDia) * 8/100
valorFinal = salario - desconto
print("O salário liquido do encanador neste mês é: ", valorFinal)