print('Bem vindo(a) a Lanchonete da Ana Carolina Gomes')
print('-------------------------------CARDÁPIO---------------------------------')

print('   CÓDIGO   |               DESCRIÇÃO             |        VALOR       |')
print('    100     |            Cachorro-quente          |       R$9,00       |')
print('    101     |         Cachorro-quente Duplo       |       R$11,00      |')
print('    102     |                X-Egg                |       R$12,00      |')
print('    103     |                X-Salada             |       R$13,00      |')
print('    104     |                X-Bacon              |       R$14,00      |')
print('    105     |                X-Tudo               |       R$17,00      |')
print('    200     |           Refrigerante Lata         |       R$5,00       |')
print('    201     |              Chá Gelado             |       R$4,00       |')

print('------------------------------------------------------------------------')

acumulador = 0
while True:
    codigo_produto = input('Entre com o código do produto desejado: ')
    if codigo_produto != '100' and codigo_produto != '101' and codigo_produto != '102' and codigo_produto != '103' and codigo_produto != '104' and codigo_produto != '105' and codigo_produto != '200' and codigo_produto != '201':
        print('Opção inválida. Escolha um dos códigos disponivéis no cardápio: ')
        continue  # se digitar algo invalido volta para o começo


    elif codigo_produto == '100':
        valor = 9.00
        print('Você escolheu um Cachorro-quente de {:.2f}'.format(valor))  # sair na tela o produto e o valor
        acumulador = acumulador + valor  # acumular o valor do produto

    elif codigo_produto == '101':
        valor = 11.00
        print('Você escolheu um Cachorro-quente Duplo de {:.2f}'.format(valor))
        acumulador = acumulador + valor

    elif codigo_produto == '102':
        valor = 12.00
        print('Você escolheu um X-Egg de {:.2f}'.format(valor))
        acumulador = acumulador + valor


    elif codigo_produto == '103':
        valor = 13.00
        print('Você escolheu um X-Salada de {:.2f}'.format(valor))
        acumulador = acumulador + valor

    elif codigo_produto == '104':
        valor = 14.00
        print('Você escolheu um X-Bacon de {:.2f}'.format(valor))
        acumulador = acumulador + valor

    elif codigo_produto == '105':
        valor = 17.00
        print('Você escolheu um X-Tudo de {:.2f}'.format(valor))
        acumulador = acumulador + valor

    elif codigo_produto == '200':
        valor = 5.00
        print('Você escolheu um Refrigerante Lata de {:.2f}'.format(valor))
        acumulador = acumulador + valor

    elif codigo_produto == '201':
        valor = 4.00
        print('Você escolheu um Chá Gelado de {:.2f}'.format(valor))
        acumulador = acumulador + valor

    pedir_mais = input('Você deseja pedir mais alguma coisa? (S ou aperte qualquer tecla)?:  ')
    pedir_mais = pedir_mais.upper()  # para dar certo sendo a letra maiscula ou minuscula
    if pedir_mais == 'S':
        print('O que mais você deseja?')
        continue  # caso a resposta seja não, o cliente encerra o programa recebendo o total da sua conta

    else:
        print('O valor total a ser pago é: R${:.2f}'.format(
            acumulador))  # sair na tela o valor total do ou dos produtos escolhidos
        break