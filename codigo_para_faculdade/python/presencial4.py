# ==================
# Calcule seu IMC
# ==================

'''

Progrma para calcular imc
- Solicita peso e altura do usuário
- Valida entradas (não aceita string, nem valores <= 0)
- Calcula imc e exibe a classificação

'''


try: # "try:" Tenta transformar todas as entradas em float. Caso o usuario use str, teremos o erro ValueError
    
    #Coleta de peso e altura com input.
    peso = float(input("Digite seu peso em kg:"))
    altura = float(input("Digite sua altura em metros:"))

    # Este primero if exibe uma mensagem de erro caso o usuário utilize 0 nas entradas.Caso contrario, "else:" é executado.
    if peso <= 0 or altura <= 0:
        print("Valores inválidos. Peso e altura devem ser maiores que 0")
    else:
        # Calculo de IMC com print do valor imc.
        imc = peso / (altura ** 2)
        print(f"Seu IMC é: {imc:.2f}") # ":.2f" serve para o número não ir além de 2 casas decimais.

        # Condicionais principais do programa.
        if imc < 18.5:
            print("Você está abaixo do peso")
        elif 18.5 <= imc <= 24.9:
            print("Seu peso está normal")
        elif 25.0 <= imc <= 29.9:
            print("Você está com sobrepeso")
        elif 30.0 <= imc <= 34.9:
            print("Você está com obesidade grau I ")
        else: # imc maior que 34.9.
            print("Você está com obesidade II ou III")

        # Mensagem sempre exibida
        print("Fim do programa!")

except ValueError: # "exept" captura o erro "ValueError" exibe o print.
    print("Você digitou algo inválido. Por favor, use números.")
