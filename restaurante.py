"""QUESTÃO 2 de 4 - Conteúdo até aula 04
Enunciado: Você e sua equipe de programadores foram contratados para desenvolver um app de vendas para uma loja que vende Marmitas
de Bife Acebolado ou Filé de Frango. Você ficou com a parte de desenvolver a interface do cliente para retirada do produto.
"""

print("Seja Bem Vindo á marmitaria!")
print("• Tamanho P de Bife Acebolado (BA) custa 16 reais e o Filé de Frango (FF) custa 15 reais;\n" \
    "• Tamanho M de Bife Acebolado (BA) custa 18 reais e o Filé de Frango (FF) custa 17 reais;\n" \
    "• Tamanho G de Bife Acebolado (BA) custa 22 reais e o Filé de Frango (FF) custa 21 reais;")

#variaveis do contador
total = 0
conter = 0

while True:
    #sabor da marmita
    flavor = str(input("Qual o sabor desejado (BA/FF): ")).upper()
    while True:
        # if flavor not in onion and flavor not in chiken: #se o sabor nao for uma opçao do cardapio retorna a pergunta
        if flavor not in ('BA', 'FF'): #se o sabor nao for uma opçao do cardapio retorna a pergunta
            flavor = str(input("Qual o sabor desejado (BA/FF): ")).upper()
        else:
            break

    #tamanho da marmita
    size = str(input("Qual será o tamanho da marmita (P/M/G): ")).upper()
    while True:
        if size not in ('P', 'M', 'G'): #se o tamanho nao for uma opçao do cardapio retorna a pergunta
            size = str(input("Qual será o tamanho da marmita (P/M/G): ")).upper()
        else:
            break

    #condição aninhada do valor dos sabores de acordo com o tamanho
    if size in ('P'):
        if flavor in 'BA':
            total = 16.00
        elif flavor in 'FF':
            total = 15.00
    elif size in ('M'):
        if flavor in 'BA':
            total = 18.00
        elif flavor in 'FF':
            total = 17.00
    elif size in ('G'):
        if flavor in 'BA':
            total = 22.00
        elif flavor in 'FF':
            total = 21.00
    
    #acumulador responsavel por calcular o valor total
    conter = conter + total

    #mensagem do pedido
    if flavor in 'ba':
        print(f'Você pediu um Beef Acebolado no tamanho {size.upper()}: R$ {total}')
    else:
        print(f'Você pediu um Filé de Frango no tamanho {size.upper()}: R$ {total}')

    #pergunta se vai pedir mais alguma coisa
    want = str(input("Deseja alguma coisa? "))
    if want in ('s', 'S'):
        continue
    if want in ('n', 'N'):
        break

print(f'O valor total a ser pago: {conter}')
