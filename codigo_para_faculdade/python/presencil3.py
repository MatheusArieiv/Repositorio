valor_da_compra = float(input("Digite o valor da compra: R$ "))
dia_semana = input("Digite o dia da semana: ").lower() # lower() transforma str em minúscolo

if valor_da_compra > 100.0 and (dia_semana == "sabado" or dia_semana == "domingo"):
    print("Você ganhou um desconto de 10%!")
else:
    print("Nenhum desconto aplicado no momento.")