n1 = int(input("Digite a sua primeira nota"))
p1 = int(input("Digite o peso da sua primeira nota"))
n2 = int(input("Digite a sua segunda nota"))
p2 = int(input("Digite o peso da sua segunda nota"))
n3 = int(input("Digite a sua terceira nota"))
p3 = int(input("Digite o peso da sua terceira nota"))
somap = p1+p2+p3
media = ((n1*p1) + (n2*p2) + (n3*p3)) / (somap)
print("A media aritmética das suas notas é ", media)
