#1036 – Fórmula de Bhaskara
nums = input()
a, b, c = [float(i) for i in nums.split()]

delta = b**2-4*a*c

if a == 0 or delta < 0:
    print("Impossivel calcular")
else:
    print(f"R1 = {(-b+delta**0.5)/(2*a):.5f}")
    print(f"R2 = {(-b-delta**0.5)/(2*a):.5f}")


#1044 – Múltiplos
nums = input()
a, b = int(nums.split()[0]), int(nums.split()[1])
if a % b == 0 or b % a == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")

#1049 – Animal
a = input()
b = input()
c = input()

arv = {
    'vertebrado': {'ave': {'carnivoro': 'aguia', 'onivoro': 'pomba'},
                   'mamifero': {'onivoro': 'homem', 'herbivoro': 'vaca'}},
    
    'invertebrado': {'inseto': {'hematofago': 'pulga', 'herbivoro': 'lagarta'},
                   'anelideo': {'hematofago': 'sanguessuga', 'onivoro': 'minhoca'}}
    }
    
print(arv[a][b][c])

#1050 – DDD
a = int(input())
d = {
    61: 'Brasilia',
    71: 'Salvador',
    11: 'Sao Paulo',
    21: 'Rio de Janeiro',
    32: 'Juiz de Fora',
    19: 'Campinas',
    27: 'Vitoria',
    31: 'Belo Horizonte'} 
    
if a in d:
    print(d[a])
else:
    print("DDD nao cadastrado")

#2424 – Tira-teima
coords = input().split()
x, y = [int(i) for i in coords]

if (x >= 0 and x <= 432) and (y >= 0 and y <= 468):
    print("dentro")
else:
    print("fora")

#2670 – Máquina de Café
A1 = int(input())
A2 = int(input())
A3 = int(input())

tempo1 = 0*A1 + 2*A2 + 4*A3
tempo2 = 2*A1 + 0*A2 + 2*A3
tempo3 = 4*A1 + 2*A2 + 0*A3

print(min(tempo1, tempo2, tempo3))

#1059 – Números Pares
for i in range(1, 101, 2):
    print(i)

#1080 – Maior e Posição
lista = []
for i in range(100):
    num = int(input())
    lista.append(num)

print(max(lista))
print(lista.index(max(lista)) + 1)

#1094 – Experiências
n = int(input())

dic = {
    "C": 0,
    "R": 0,
    "S": 0}

for i in range(n):
    entry = input().split()
    dic[entry[1]] += int(entry[0])

total = sum(dic.values())
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {dic['C']}")
print(f"Total de ratos: {dic['R']}")
print(f"Total de sapos: {dic['S']}")

print(f"Percentual de coelhos: {dic['C'] / total * 100:.2f} %")
print(f"Percentual de ratos: {dic['R'] / total * 100:.2f} %")
print(f"Percentual de sapos: {dic['S'] / total * 100:.2f} %")

#1114 – Senha Fixa
a = False
while not a:
    b = int(input())
    if b == 2002:
        print("Acesso Permitido")
        a = not a
    else:
        print("Senha Invalida")

#1116 – Dividindo X por Y
n = int(input())

for i in range(n):
    ent = input().split()
    x, y = [int(i) for i in ent]
    try:
        print(float(x/y))
    except:
        print("divisao impossivel")

#1151 – Fibonacci Fácil
N = int(input())

a, b = 0, 1
fibonacci = []

for i in range(N):
    fibonacci.append(a)
    a, b = b, a + b

print(" ".join(map(str, fibonacci)))