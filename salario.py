import os
os.system("cls")

print("=== Calculadora de Salário Mensal ===")

valor = float(input("Informe quanto você ganha por hora:"))
horas = int(input("Informe quantas horas você trabalha por mês:"))

total_salario = valor * horas

print(f"Seu salario do mês é: {total_salario:.2f}")