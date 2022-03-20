boleto = float(input("Informe o valor do boleto cobrado"))
juros = float(input("Informe o percentual de juros cobrado"))
dias = float(input("Informe a quantidade de dias que o boleto está atrasado"))
s = boleto + (boleto * (juros/100))+ dias
print("O novo valor a ser pago do boleto é: ", s)
