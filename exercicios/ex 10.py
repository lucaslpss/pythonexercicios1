valorVendido = float(input("Insira o valor total vendido da loja neste mês"))
salarioVendedor = 1800
comissão = valorVendido * 3/100
salarioTotal = salarioVendedor + comissão
print(f"Seu salário mensal é de R${salarioVendedor} mais R${comissão} de comissão, totalizando R${salarioTotal}")
