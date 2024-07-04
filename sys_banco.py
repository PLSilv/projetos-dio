valor_atual = 0.0
contagem_saques = 0  
limite_saques = 3  
movimentos = []

def deposito(valor_atual, movimentos):
    valor = float(input("Digite o valor para depósito: "))
    valor_atual += valor
    movimentos.append(f"Depósito: R${valor:.2f}")
    return valor_atual

# Função para saque
def realizar_saque(valor_atual, contagem_saques, limite_saques, movimentos):
    if contagem_saques >= limite_saques:
        print("Você atingiu o limite de 3 saques.")
        return valor_atual, contagem_saques

    valor = float(input("Digite o valor para saque: "))
    if valor <= valor_atual:
        valor_atual -= valor
        contagem_saques += 1
        movimentos.append(f"Saque: R${valor:.2f}")
    else:
        print("Saldo insuficiente!")
    return valor_atual, contagem_saques

def extrato(valor_atual, movimentos):
    print("\n--- Extrato ---")
    if movimentos:
        for transacao in movimentos:
            print(transacao)
    else:
        print("Nenhuma transação realizada.")
    print(f"\nSeu saldo atual é: R${valor_atual:.2f}")
    print("----------------")

while True:
    
    print("""
          
                  Bem-vindo!
          
          Selecione a operação desejada:
          
           """)

    print("""
        (1) Depósito
        (2) Saque
        (3) Extrato
        (4) Sair
           """)

    opcao = int(input("Digite a opção desejada (1/2/3/4): "))

    if opcao == 1:
        valor_atual = deposito(valor_atual, movimentos)
        
    elif opcao == 2:
        valor_atual, contagem_saques = realizar_saque(valor_atual, contagem_saques, limite_saques, movimentos)
        
    elif opcao == 3:
        extrato(valor_atual, movimentos)
        
    elif opcao == 4:
        print("Sistema encerrado")    
        break
    
    else:
        print("Opção inválida!")
