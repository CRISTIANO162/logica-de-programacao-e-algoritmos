"""QUESTÃO 1 de 4 - Conteúdo até Aula 03
Enunciado: Imagina-se que você é um dos programadores responsáveis pela construção de app de vendas para uma determinada empresa X que aceita
cartões de crédito. Uma das estratégias de vendas dessa empresa X é cobrar um Juros maior conforme a quantidade de parcelas que o cliente desejar,
conforme a listagem abaixo:

•	Se a quantidade de parcelas for menor que 4, o Juros será de 0% (0 / 100);
•	Se a quantidade de parcelas for igual ou maior que 4 e menor que 6, o Juros será de 4% (4 / 100);
•	Se a quantidade de parcelas for igual ou maior que 6 e menor que 9, o Juros será de 8% (8 / 100);
•	Se a quantidade de parcelas for igual ou maior que 9 e menor que 13, o Juros será de 16% (16 / 100);
•	Se a quantidade de parcelas for igual ou maior que 13, o Juros será de 32% (32 / 100);
"""


print("Olá, seja bem vindo a loja do Cris!")

RequestedValue = int(input("Qual o valor do pedido: "))
installments = int(input("Qual a quantidade de parcelas: "))

if  installments < 4: #parcelas menor que 4 juros de 0%
    fees = 0
elif  installments >= 4 and  installments < 6: #quantidade de parcelas for igual ou maior que 4 e menor que 6, o Juros será de 4%
    fees = .04 
elif  installments >= 6 and  installments < 9: #quantidade de parcelas for igual ou maior que 6 e menor que 9, o Juros será de 8%
    fees = .08
elif  installments >= 9 and  installments < 13: #quantidade de parcelas for igual ou maior que 9 e menor que 13, o Juros será de 16%
    fees = .16
else:
    installments >= 13 #quantidade de parcelas for igual ou maior que 13, o Juros será de 32%
    fees = .13

# O valor da parcela é calculado da seguinte maneira:
# valorDaParcela=  (valorDoPedido*(1+juros))/quantidadeParcelas
# O valor total parcelado é calculado da seguinte maneira:
# valorTotalParcelado=valorDaParcela*quantidadeParcelas

InstallmentValue = (RequestedValue * (1 + fees)) //  installments
total = InstallmentValue *  installments

print(f"valor das parcelas é: R$ {InstallmentValue}")
print(f"Valor total parcelado é: R$ {total}")