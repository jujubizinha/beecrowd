import math
x_1, y_1 = map(float,input().split())
x_2, y_2 = map(float,input().split())
distancia = math.sqrt( ((x_2-x_1)**2) + ((y_2-y_1)**2))
print("%.4f"%distancia)