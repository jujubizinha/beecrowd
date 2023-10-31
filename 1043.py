A, B, C = map(float,input().split())
perimetro = A + B + C
area = (A + B) * C / 2
if A + B > C and A + C > B and B + C > A:
    print(f"Perimetro = {perimetro:.1f}")
else:
    print(f"Area = {area:.1f}")