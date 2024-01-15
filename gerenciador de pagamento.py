print('{:=^40}'.format(' LOJAS AMERICANAS '))
valor = float(input('VALOR TOTAL: R$ '))
print('''FORMAS DE PAGAMENTO
 [ 1 ] À vista Dinheiro/Debito
 [ 2 ] À vista Cartão
 [ 3 ] 2x no Cartão
 [ 4 ] 3x ou mais no cartão/com juros''')
opc = int(input('Qual opção deseja?. '))
if opc == 1:
    total = valor - valor * 10 / 100
elif opc == 2:
    total = valor - (valor * 5 /100)
elif opc == 3:
    total = valor
    parcela = total / 2
    print(f' sua compra vai custar 2x de  R${parcela:.2f} no final')
elif opc == 4:
    total = valor + (valor * 20 / 100)
    tatalp = int(input('quantas parcelas?: '))
    parcela = total / tatalp
    print(F'sua compra será parcelada em {tatalp}x de R${parcela:.2f} COM JUROS')
else:
    total = valor
    print('OPÇÃO INVALIDA, TENTE NOVAMENTE!')
print(f'sua compra de R${valor:.2f} vai custar R${total:.2f} no final')