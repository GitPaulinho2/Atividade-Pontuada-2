import os 
os.system("clear") # Alunos: Diego Luis e Miguel Ferraz

print("""
    ================== MENU ===================
    1 - Picanha - R$25.00
    2 - Lasanha - R$20.00
    3 - Strogonoff - R$18.00
    4 - Bife Acebolado - R$15.00
    5 - Pão com ovo - R$5.00
    6 - Frango à milanesa - R$23.00
    7 - Macarrão com almôndegas - R$16.00
    0 - Finalizar pedido
    """)

precos = {1: ("Picanha", 25), 2: ("Lasanha", 20), 3: ("Strogonoff", 18),
         4: ("Bife Acebolado", 15), 5: ("Pão com Ovo", 5), 6: ("Frango à Milanesa", 23),  7: ("Macarrão com Almôndegas", 16)}
pratos_solicitados = []
total_pagar = 0

while True:
        try:
            opcao = int(input("Escolha um prato pelo número (0 para finalizar): "))
        except ValueError:
            print("Digite um número válido!")
            continue
        
        match opcao:
            case 1:
                pratos_solicitados.append(("Picanha", 25))
                total_pagar += 25
            case 2:
                pratos_solicitados.append(("Lasanha", 20))
                total_pagar += 20
            case 3:
                pratos_solicitados.append(("Strogonoff", 18))
                total_pagar += 18
            case 4:
                pratos_solicitados.append(("Bife Acebolado", 15))
                total_pagar += 15
            case 5:
                pratos_solicitados.append(("Pão com Ovo", 5))
                total_pagar += 5
            case 6:
                pratos_solicitados.append(("Frango à Milanesa", 23))
                total_pagar += 23
            case 7:
                pratos_solicitados.append(("Macarrão com Almôndegas", 16))
                total_pagar += 16
            case 0:
                break
            case _:
                print("Código inválido. Tente novamente.")
    
if not pratos_solicitados:
        print("Nenhum prato foi solicitado. Encerrando o sistema.")
        
    
print("\nFormas de Pagamento:\n1 - À vista (10% de desconto)\n2 - Cartão de crédito (10% de acréscimo)")
while True:
        try:
            pagamento = int(input("Escolha a forma de pagamento: "))
            match pagamento:
                case 1:
                    desconto = total_pagar * 0.10
                    total_pagar -= desconto
                    forma_pagamento = "À vista"
                    break
                case 2:
                    acrescimo = total_pagar * 0.10
                    total_pagar += acrescimo
                    forma_pagamento = "Cartão de Crédito"
                    break
                case _:
                    print("Opção inválida. Escolha 1 ou 2.")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
    
print("\n=== Nota Fiscal ===")
for prato, valor in pratos_solicitados:
    print(f"{prato}: R${valor:.2f}")
print(f"Total sem desconto/acréscimo: R${total_pagar:.2f}")
print(f"Forma de pagamento: {forma_pagamento}")
print(f"Total a pagar: R${total_pagar:.2f}")
