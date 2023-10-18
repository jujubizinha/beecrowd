nome_vendedor = str(input(""))
salario = float(input(""))
vendas = float(input(""))
comissao = vendas * 0.15
salario= salario + comissao
print(f"TOTAL = R$ {salario:.2f}")