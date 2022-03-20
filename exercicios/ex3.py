cotacao = float (input("Digite a cotação do dolar"))
reais = float (input("Digite o valor que você possui em reais"))
s = reais / cotacao
print(f"Você possui {s:,.2f} dólares")