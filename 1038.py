id, quantidade = map(int,input().split())
valor = 0
if id == 1:
    valor = 4.00
elif id == 2:
    valor = 4.50
elif id == 3:
    valor = 5.00
elif id == 4:
    valor = 2.00
elif id == 5:
    valor = 1.50
total = valor * quantidade
print(f"Total: R$ {total:.2f}")