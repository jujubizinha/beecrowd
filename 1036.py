import math
A, B, C = map(float,input().split())
delta = ((B * B) -4 * A * C)
if A == 0 or delta < 0:
    print("Impossivel calcular")
else:
    R1 = (-B + math.sqrt(delta)) / (2 * A)
    R2 = (-B - math.sqrt(delta)) / (2 * A)
    print("R1 = {:.5f}".format(R1))
    print("R2 = {:.5f}".format(R2))