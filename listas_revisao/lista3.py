# 1004 – Produto Simples
a = int(input())
b = int(input())
print(f"PROD = {a*b}")


#1005 – Média 1
a = float(input())
b = float(input())
print(f"MEDIA = {(a*3.5+b*7.5)/11:.5f}")


#1011 – Esfera
r = float(input())
print(f"VOLUME = {(4/3) * 3.14159 * r**3:.3f}")


#2416 – Corrida
entry = input()
entry = [int(i) for i in entry.split()]
c, n = entry
print(c % n)


#1015 – Distância Entre Dois Pontos
import math

uns = input()
dois = input()

x1, y1 = [float(i) for i in uns.split()]
x2, y2 = [float(i) for i in dois.split()]

print(f"{math.sqrt((x2 - x1)**2 + (y2-y1)**2):.4f}")


#1930 – Tomadas
lines = input()
print(sum([int(i) for i in lines.split()])-3)