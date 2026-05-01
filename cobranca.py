# •	Camiseta Manga Curta Simples (MCS), o valor unitário é de um real e oitenta centavos;
# •	Camiseta Manga Longa Simples (MLS), o valor unitário é de dois reais e dez centavos;
# •	Camiseta Manga Curta Com Estampa (MCE), o valor unitário é de dois reais e noventa centavos; 
# •	Camiseta Manga Longa Com Estampa (MLE), o valor unitário é de três reais e vinte centavos; 

# •	Se número de camisetas for menor que 20 não há desconto na venda;
# •	Se número de camisetas for igual ou maior que 20 e menor que 200, o desconto será de 5%;
# •	Se número de camisetas for igual ou maior que 200 e menor que 2000, o desconto será de 7%;
# •	Se número de camisetas for igual ou maior que 2000 e menor ou igual que 20000, o desconto será de 12%;
# •	Se número de camisetas for maior que 20000, não é aceito pedidos nessa quantidade de camisetas;

# ♦	Para o adicional de frete por transportadora (1) é cobrado um valor extra de 100 reais;
# ♦	Para o adicional de frete por Sedex (2) é cobrado um valor extra de 200 reais;
# ♦	Para o adicional de retirar o pedido na fábrica (0) é cobrado um valor extra de 0 reais;

# O valor final da conta é calculado da seguinte maneira:
# total = (modelo * num_camisetas) + frete

print('Seja Bem vindo a fábrica de camisas')

def escolha_modelo():
    """pergunta o modelo desejado"""
    while True:
        print('Qual modelo desejado\n'
            'Camiseta Manga Curta Simples (MCS), o valor unitário é de um real e oitenta centavos\n'
            'Camiseta Manga Longa Simples (MLS), o valor unitário é de dois reais e dez centavos\n' \
            'Camiseta Manga Curta Com Estampa (MCE), o valor unitário é de dois reais e noventa centavos\n' \
            'Camiseta Manga Longa Com Estampa (MLE), o valor unitário é de três reais e vinte centavos')
                
        model = str(input('>>>> ')).upper()
        if model not in ('MCS', 'MLS', 'MCE', 'MLE'):
            continue
        else:
            break
    if model == 'MCS':
        unitario = 1.80
    elif model == 'MLS':
        unitario = 2.10
    elif model == 'MCE':
        unitario = 2.90
    elif model == 'MLE':
        unitario = 3.20
    
    return unitario
        
def num_camisa():
    while True:
        try:
            print('Qual a quantidade de camisas')
            numero = int(input('>>>> '))           
            break
        except ValueError as e:
            print(f'valor invalido, são aceito apenas números {e}')
        finally:
            if numero > 20000:
                print('não é aceito pedidos nessa quantidade!')
                continue

    if numero <= 20:
        total = numero
    elif numero >= 20 and numero < 200:
        desconto = (numero * 5) // 100
        total = numero - desconto
    elif numero >= 200 and numero < 2000:
        desconto = (numero * 7) // 100
        total = numero - desconto
    elif numero >= 2000 and numero < 2000:
        desconto = (numero * 12) // 100
        total = numero - desconto 
    
    return total

def frete():
    while True:
        print('Qual será a forma de retirada\n\n' \
        '1 - frete por transportadora (1) é cobrado um valor extra de 100 reais\n' \
        '2 - frete por Sedex (2) é cobrado um valor extra de 200 reais\n' \
        '3 - retirar o pedido na fábrica (0) é cobrado um valor extra de 0 reais')

        frete = int(input('>>>> '))
        if frete not in (0, 1, 2):
            print('escolha uma opção valida!')
            continue
        else:
            break
    
    if frete == 0:
        adicional = 0
    elif frete == 1 :
        adicional = 100
    elif frete == 2:
        adicional = 200
    
    return adicional

#código principal(Main)
modelo = escolha_modelo()
camisa = num_camisa()
Frete = frete()
total = (modelo * camisa) + Frete
print(total)
print(f'Total: R$ {total} (Modelo: {modelo} * quantidade: {camisa}) + {Frete}')
