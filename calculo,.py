aparelho = input("Digite o aparelho que deseja calcular:")
potencia = int(input("Indique a potência do seu aparelho:"))
horasDia = int(input("Coloque o tempo diário de consumo:"))

consumoMensal = (potencia * horasDia * 30) / 1000
print("O consumo mensal do aparelho", aparelho, "é de:", consumoMensal, "kWh/mês")