
#Exercicio 1

A = float(input('Digite um numero que deverá ser somado com 2: '))
B = float(input('Digite um numero que deverá ser multiplicado por 3: '))

AB = (A + 2) * (3 * B)

print (f'o resultado da multiplicação das operações passadas é: {AB}')

#exercicio 2
print('Calculador de segundos\nOlá, este programa irá coletar os seus dias, horas, minutos e segundos\nlogo depois irá converte-los todos em segundos')

d = int(input('Digite a quantidade de dias: '))
h = int(input('Digite a quantidade de horas: '))
m = int(input('Digite a quantidade de minutos: '))
s = int(input('Digite a quantidade de segundos: '))

ss = s + (m * 60) + (h * 3600) + (d * 24 * 3600 )

print(f'O total de segundos existentes baseado nos dados fornecidos é igual a {ss} segundos')

#exercicio 3
print('Olá, vimos que o senhor está pedindo um emprestimo ao banco para realizar a compra de um apartamento\nAntes de aprovarmos o emprestimo, precisamos fazer algumas perguntas')
ap = float(input('Qual o valor do apartamento que Deseja comprar? '))
sa = float(input('Qual o valor do salário recebido? '))
an = int(input('em quantos anos pretende terminar de pagar o apartamento? '))

pr = ap/(an * 12)
s4 = sa * 0.40
if(pr > s4 ):
    print ('Infelizmente não podemos aprovar o seu emprestimo devido ao valor do imovel')

else:
    print('Parabéns o seu imprestimo foi aprovado, boa sorte com a compra do imovel')


#exercicio 4 

conv = int(input('Digite:\n 1 para converter para Celsius\n 2 para converter para Fahrenheit\n Você deseja converter uma temperatura de Celsius para Fahrenheit, ou de Fahrenheit para Celsius? '))

if (conv == 1):
    
    temp = float(input('Qual o valor da temperatura que deverá ser convertida para Celsius? '))
    cel = (temp - 32) * 5/9
    print (f'O resultado da sua conversão é {cel}°C')

elif(conv == 2):
    temp = float(input('Qual o valor da temperatura que deverá ser convertida para Fahrenheit? '))
    Fah = (temp * 9/5) + 32
    print (f'O resultado da sua conversão é {Fah}°F')

else:
    print ('numero não existente nas opções, por favor tente novamente')

#exercicio 5

dec = int(input('Qual operação deseja realizar?\n1 - Adição\n2 - subtração\n3 - multiplicação\n4 - divisão\n'))

if (dec == 1):
    n1 = float(input('Digite o primeiro numero: '))
    n2 = float(input('Digite o segundo numero: '))

    total = n1 + n2

    print(f'O resultado da soma é {total}')
    
elif(dec == 2):
    n1 = float(input('Digite o primeiro numero: '))
    n2 = float(input('Digite o segundo numero: '))

    total = n1 - n2

    print(f'O resultado da subtração é {total}')

elif(dec == 3):
    n1 = float(input('Digite o primeiro numero: '))
    n2 = float(input('Digite o segundo numero: '))

    total = n1 * n2

    print(f'O resultado da multiplicação é {total}')

elif(dec == 4):
    n1 = float(input('Digite o primeiro numero: '))
    n2 = float(input('Digite o segundo numero: '))

    total = n1 / n2

    print(f'O resultado da divisão é {total}')

else:
    print('O numero digitado não está incluso nas opções, porfavor tente novamente')

#exercicio 6
horas = int(input('Quantas horas o senhor trabalhou esté mês? '))
val = float(input('Qual o valor recebido por hora trabalhada? '))

valb = val * horas

FGTS = valb * 0.11

if(valb <= 900):
    INSS = valb *0.075
    totald = INSS 
    vall = valb - INSS
    print(f'Salário Bruto: R${valb}\nIR: Isento\nINSS R${INSS}\nFGTS R${FGTS}\nTotal de descontos  R${totald}\nSalário liquido R${vall}')

elif(valb > 900 and valb <= 1500):
    IR = valb * 0.05
    INSS = valb *0.075
    totald = INSS + IR
    vall = valb - totald

    print(f'Salário Bruto: R${valb}\nIR: R${IR}\nINSS: R${INSS}\nFGTS: R${FGTS}\nTotal de descontos: R${totald}\nSalário liquido: R${vall}')

elif(valb > 1500 and valb <= 2500):
    IR = valb * 0.10
    INSS = valb *0.09
    totald = INSS + IR
    vall = valb - totald

    print(f'Salário Bruto: R${valb}\nIR: R${IR}\nINSS: R${INSS}\nFGTS: R${FGTS}\nTotal de descontos: R${totald}\nSalário liquido: R${vall}')

else: 
    IR = valb * 0.20
    INSS = valb *0.12
    totald = INSS + IR 
    vall = valb - totald

    print(f'Salário Bruto: R${valb}\nIR: R${IR}\nINSS: R${INSS}\nFGTS: R${FGTS}\nTotal de descontos: R${totald}\nSalário liquido: R${vall}')

#DEIXO CLARO QUE NÃO TINHA EXERCICIO 7 NA FOLHA 
#exercicio 8

salm = 1412

sal = float(input('Digite o valor do seu salário: '))

qtd = sal / salm

print(f'Você recebe o equivalente a {qtd:.2f} salários minimos')