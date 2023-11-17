A, B, C = sorted(list(map(float, input().split())))[::-1]
if A >= B + C or B >= A + C or C >= A + B:
    print("NAO FORMA TRIANGULO")
else:

        if (A * A) == (B * B) + (C * C):
            print("TRIANGULO RETANGULO")
        if (A * A) > (B * B) + (C * C):
            print("TRIANGULO OBTUSANGULO")
        if (A * A) < (B * B) + (C * C):
            print("TRIANGULO ACUTANGULO")

        if A == B and B == C:
            print("TRIANGULO EQUILATERO")
        if ((A == B or B == C) and not (A == B and C == B)):
            print("TRIANGULO ISOSCELES")