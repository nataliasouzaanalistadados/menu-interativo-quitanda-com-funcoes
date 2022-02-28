cesta=[]

def esta_vazia():
    return len(cesta) == 0

def item_cesta():
  if not esta_vazia():
        print('Cesta de compras')
        for items in cesta:
          print(items)
          print('-'*15)
  else:
    print('Cesta de compras está vazia')
    print('-'*15)

def adicionar_fruta():
  print(f'Escolha a fruta desejada:\n' \
                      f'1 - Banana\n' \
                      f'2 - Melancia\n' \
                      f'3 - Morango\n' \
                      f'Digite a opção desejada: ')
  fruta = input('')
  frutas = {
    '1':'Banana',
    '2':'Melancia',
    '3':"Morango"}

  if fruta in frutas:
    cesta.append(frutas[fruta])
    print(f'{frutas[fruta]} foi adicionado com sucesso')
    print('-'*15)
  else:
    print('Opção inválida')
    print('-'*15)

def checkout():
  precos = {
    'Banana':3.50,
    'Melancia':7.50,
    'Morango':5.00}
  if len(cesta) > 0:
        total = 0
        for item in cesta:
            total += precos[item]

        print(f'Total de compras: {total}')
        print(f'Cesta de compras: {cesta}')
  else:
        print('Cesta de compras vazia.')

def sair(*args):
  print("Encerrando atendimento")
  exit()

opcoes={
    '1':item_cesta,
    '2':adicionar_fruta,
    '3':checkout,
    '4':sair
}


def main():


  while True:

    print(f'Quitanda: \n1:Ver cesta\n2:Adicionar frutas\n'\
          f'3:Checkout\n4:Sair\nDigite a opção desejada:')
    op = input('')
    if op in opcoes.keys():
      print(opcoes[op]())
    else:
      print('Opção inválida')
   

if __name__ == '__main__':
  main()