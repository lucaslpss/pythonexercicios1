totalCabeças = int(input("Digite o total de cabeças no cercado"))
totalPatas = int(input("Digite o total de patas no cercado"))
max = (totalCabeças * 4)
min = (totalCabeças * 2)
if totalCabeças > max:
    print("Inválido")
if totalCabeças < min:
    print ("Inválido")
else: print("Ok, prosseguir")