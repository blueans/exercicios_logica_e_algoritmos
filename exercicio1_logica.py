print('Bem vindo a Loja da Ana Carolina Gomes')
valor_produto = float(input('Entre com o valor que produto: '))
qdt_produto = int(input("Entre com a quantidade desejada do produto: "))
desconto_produto = 0

if (qdt_produto <= 9):
  desconto_produto = 0.00 # produto não terá desconto entre 0 e 9 unidades
  desconto = '0%'

elif (qdt_produto >= 10) and (qdt_produto <= 99):
  desconto_produto = 0.05 # desconto de 5% no valor do produto entre 10 e 99 unidades
  desconto = '5%'

elif (qdt_produto >= 100) and (qdt_produto <= 999):
  desconto_produto = 0.10 # desconto de 10% no valor do produto entre 100 e 999 unidades
  desconto = '10%'

else:
    desconto_produto = 0.15 # desconto de 15% acima de 999 unidades do produto
    desconto = '15%'

total_sem_desconto = valor_produto * qdt_produto
print ('O valor total SEM desconto é de: R$ {:.2f}' . format(total_sem_desconto))
total_com_desconto = total_sem_desconto - total_sem_desconto * desconto_produto
print ('O valor total COM desconto é de: R$ {:.2f} (desconto de {})' . format(total_com_desconto, desconto))



