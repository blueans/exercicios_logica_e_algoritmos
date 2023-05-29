def dimensoesObjeto():
    print('---------------------------- DIMENSÕES DO OBJETO -----------------------------')
    while True:
        try:
            altura = float(input('Digite a altura do objeto em centimetros (cm): '))
            comprimento = float(input('Digite o comprimento do objeto em centimentros (cm): '))
            largura = float(input('Digite a largura do objeto em centimetros (cm): '))

            dimensoes = altura * comprimento * largura

            if dimensoes < 1000:
                tamanho = print('O valor dessa etapa é de R$10')
                return 10
            elif 1000 <= dimensoes < 10000:
                tamanho = print('O valor dessa etapa é de R$20')
                return 20
            elif 10000 <= dimensoes < 30000:
                tamanho = print('O valor dessa etapa é de R$30')
                return 30
            elif 30000 <= dimensoes < 100000:
                tamanho = print('O valor dessa etapa é de R$50')
                return 50
            else:
                print('Dimensões menores que 1000 ou maiores que 100000 não são aceitas.')

            print('O valor dessa etapa é de R${:.2f}' .format(tamanho))
            break

        except ValueError:  # caso o cliente não digite um valor númerico
            print('Você digitou um caractere não númerico. \n' +
                  'Digite novamente as dimensões do objeto')
            continue

            # return value


def pesoObjeto():
    print('---------------------------------- PESO DO OBJETO ----------------------------------')
    while True:
        try:
            pesoObj = float(input('Digite o peso do pacote que deseja enviar em quilogramas (kg): '))
            if pesoObj <= 0.1:
                return 1
            elif 0.1 <= pesoObj < 1:
                return 1.5
            elif 1 <= pesoObj < 10:
                return 2
            elif 10 <= pesoObj < 30:
                return 3
            else:
                print('Valor não aceito')
            continue  # pergunta novamente voltando para o inicio
            print('Peso do objeto: {:.2}'.format(pesoObj))

        except ValueError:
            print('Você digitou um valor não númerico ou incorreto para a somatória')
            continue

def rotaObjeto():
  print('---------------------------------- ROTA DO OBJETO ----------------------------------')
  while True:
      try:
          rota = input('Digite as inicias da rota desejada: \n' +
                             'RS - De Rio de Janeiro até São Paulo \n' +
                             'SR - De São Paulo até Rio de Janeiro\n' +
                             'BS - De Brasília até São Paulo\n' +
                             'SB - De São Paulo até Brasília\n').upper()
          if rota == 'RS':
              print ('A rota escolhida é Rio de Janeiro até São Paulo')
              valor_rota = 1
          elif rota == 'SR':
              print('A rota escolhida é São Paulo até Rio de Janeiro')
              valor_rota = 1
          elif rota == 'BS':
              print('A rota escolhida é Brasília até São Paulo')
              valor_rota = 1.2
          elif rota == 'SB':
              print('A rota escolhida é São Paulo até Brasília')
              valor_rota = 1.2
              return valor_rota

          else:
              print('Iniciais não aceitas. Digite as inicias da rota que deseja corretamente.')
            # continue  # pergunta novamente voltando para o inicio

      except ValueError:
          print('Você digitou um valor não númerico ou incorreto para a somatória')
      continue


# Inicio do Programa Principal
print('---------- Bem vindo(a) a Companhia de Logística: Ana Carolina Gomes LTDA ----------')
dimensoes = dimensoesObjeto()
print(dimensoes)
pesoObj = pesoObjeto()
print(pesoObj)
valor_rota = rotaObjeto()
print(valor_rota)
total = dimensoes * pesoObj * valor_rota
print('Total a pagar R$ {}. (dimensões: {} * peso: {} * rota {})'.format(total, dimensoes, pesoObj, valor_rota))