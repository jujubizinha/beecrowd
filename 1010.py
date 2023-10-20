linha_1 = input().split(" ")
linha_2 = input().split(" ")

codigo_peca1, numero_peca1, valor_unitario1 = linha_1
codigo_peca2, numero_peca2, valor_unitario2 = linha_2
total_a_pagar = (int(numero_peca1) * float(valor_unitario1)) + (int(numero_peca2) * float(valor_unitario2))
print(f"VALOR A PAGAR: R$ {total_a_pagar:.2f}")
