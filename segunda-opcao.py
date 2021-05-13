velocidade_max = 80
multa = 7

velocidade = float(input("Insira a velocidade do veiculo em km: "))
velocidade_total = velocidade - velocidade_max
valor_multa = velocidade_total * multa

if velocidade > velocidade_max:
    print("Seu veiculo foi multado em R$" + valor_multa)

else:
    print("Tudo numa boa!")
