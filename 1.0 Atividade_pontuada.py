import os
os.system("clear")

preco = 0
pratos_solicitados = 0
total_pagar = 0
preco_total = 0
desconto = 0
acrescimo = 0
while True:
    print("""
================== MENU ===================

Código    \tPrato   \t\tValor
1 \t\tPicanha     \t\t R$25.00
2 \t\tLasanha     \t\t R$20.00
3 \t\tStrogonoff     \t\t R$18.00
4 \t\tBife Acebolado\t\t R$15.00
5 \t\tPão com ovo   \t\t R$5.00
6 \t\tFrango a milanesa \t R$23.00
7 \t\tMacarrão com almôndegas  R$16.00
""")

    opcao = int(input("Informe o prato desejado: "))

    match opcao:

     case 1: 
      prato = "Picanha"
      valor = 25
     case 2:
      prato = "Lasanha"
      valor = 20
     case 3:
      prato = "Strogonoff"
      valor = 18
     case 4:
      prato = "Bife Acebolado"
      valor = 15
     case 5:
      prato = "Pão Com Ovo"
      valor = 5
     case 6:
      prato = "Frango a milanesa"
      valor = 23
     case 7:
      prato = "Macarrão com almôndegas"
      valor = 16
     case _:
      prato = "Opção invalida"
      valor = 0

    mais_pedidos = input("Deseja pedir mais pratos?\n'S' para sim e 'N' para não:")
        
    if mais_pedidos == 's':
     pratos_solicitados += 1
    else:
      mais_pedidos == 'n'
      break

while True:
    print("""
=== Pagamento ===    
1\tA vista
2\tCartão de crédito    
   """)
  
    pagamento = int(input("Informe a forma de pagamento:"))

    match pagamento:
      case 1:
        if preco_total > 0:
            desconto = preco_total * 0.10
        
      case 2:
        if preco_total > 0:
            acrescimo = preco_total * 10

    preco_total = total_pagar + desconto
    
    print("\n ===Nota Fiscal===")
    print(f"Pratos Solicitados: {pratos_solicitados}")
    print(f"Valor sem desconto: {preco_total}")
    print(f"Desconto aplicado: {desconto}")
    print(f"Total da compra: R${total_pagar:.2f}")
    break

