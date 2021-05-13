velocidade = float(input("Insira a velocidade em KM:\n")) """variável criada para armazenar a km """


""" se a velocidade for maior que 80km/h ""
if velocidade > 80 : """valida se a velocidade inserida para o usuário é maior que 80 se sim irá imprimir(print) a mensagem abaixo"""

    print("Seu veiculo foi multado. Devido ter ultrapassado o limite de velocidade irá pagar uma multa de R$ ((velocidade-80)*7:.2f)")

"""senão imprime a mensagem abaixo"""
else:
    print("Tudo numa boa!")
