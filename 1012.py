A, B, C = map(float,input().split())
area_triangulo = 0.5 * A * C
pi = 3.14159
area_circulo = pi * C**2
area_trapezio = ((A + B) / 2) * C
area_quadrado = B*B
area_retangulo = A * B


print(f'TRIANGULO: {area_triangulo:.3f}')
print(f'CIRCULO: {area_circulo:.3f}')
print(f'TRAPEZIO: {area_trapezio:.3f}')
print(f'QUADRADO: {area_quadrado:.3f}')
print(f'RETANGULO: {area_retangulo:.3f}')