def maior(x,y):
    return max(x,y)

def maior3(x,y,z):
    return max(x,y,z)

def iniciais(nome):
    dividido = nome.split()
    inic = ''
    for i in dividido:
        inic += i[0] + ' '
    return inic

def aprovado(nota1, nota2):
    return (nota1 + nota2)/2 >= 60

def formatar_nome(nome):
    return " ".join([i.capitalize() for i in nome.split()])