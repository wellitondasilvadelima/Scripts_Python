from pessoa import Pessoa
from cliente import Cliente
from contabanco import ContaBanco
import os


def main():
 RUN = True
 print("\n")
 cliente_1_conta = ContaBanco(
                    'João K',
                    '10/10/2000', 
                    '10112365400', 
                    '9876540', 
                    'Maria Antonieta', 
                    'José Francisco', 
                    '88100100', 
                    'Rua Alemeda dos anjos', 
                    'Springfield', 
                    'Verde', 
                    'Kansas',
                    'Joao K',
                    'Conta Corrente',
                    '10101100',
                    '10',
                    '100.00',
                    '5000.00')
 while(RUN):
    print("ESCOLHA A TRANSAÇÃO")
    print("1. CONSULTAR SALDO")
    print("2. DEPOSITAR")
    print("3. SACAR")
    print("4. ENCERRAR")
    entrada = input()

    # Para Windows
    os.system("cls")

    # Para Linux e macOS
    #os.system("clear")

    if(entrada == "1"):
        cliente_1_conta.ConsultarSaldo()
    
    elif(entrada == '2'):
         print("Digite o valor: ")
         valor = input()
         cliente_1_conta.Depositar(valor)

    elif(entrada == '3'):
        print("Digite o valor: ")
        valor = input()
        cliente_1_conta.Sacar(valor)
        
    elif(entrada == '4'):
       RUN = False
       print("O PROGRAMA SERÁ FINALIZADO...")
    
    else:
        print("Opção Inválida")

    input("\nPressione Enter para continuar...\n\n")
    os.system("cls")

main()
print("ENCERRADO.")



'''
   cliente_1 = Cliente('João K', 
                    '10112365400', 
                    '9876540', 
                    'Maria Antonieta', 
                    'José Francisco', 
                    '88100100', 
                    'Rua Alemeda dos anjos', 
                    'Springfield', 
                    'Verde', 
                    'Kansas',
                    'Joao K',
                    'Conta Corrente',
                    '10101100',
                    '10',)
 '''






