from cliente import Cliente

class ContaBanco(Cliente):
    
    def __init__(self, nome, dataNascimento, cpf, rg, 
                 nome_mae, nome_pai, cep, endereco, 
                 cidade, bairro, estado, titular, tipo_conta, 
                 numero_conta, numero_agencia, saldo, credito):

        super().__init__(nome, dataNascimento, cpf, rg, nome_mae, nome_pai, cep, endereco, 
                         cidade, bairro, estado,titular, tipo_conta, 
                 numero_conta, numero_agencia,)
        
        self.saldo               = saldo
        self.credito             = credito

    def Sacar(self, saque):
        try:
            if float(saque) > 0:
                if (float(self.saldo) - float(saque)) < 0 :
                    print("Saldo insuficiente")
                #elif(self.saldo - saque) >=0:
                    #self.saldo = self.saldo - saque
                else:
                    self.saldo = float(self.saldo) - float(saque)
                    print("Operação realizada com sucesso. Transação concluída!")
            else:
                print("Valor inválido. Transação encerrada!")
        except ValueError:
           print("\nDigite um valor válido")      

    def ConsultarSaldo(self):
        print("Tipo de Conta: ", self.tipo_conta)
        print("Saldo: ", self.saldo)
        print("Credito Liberado: ", self.credito)
    
    def Depositar(self, deposito):
        #deposito = float
        try:

            if float(deposito) > 0:
                self.saldo = float(self.saldo) + float(deposito)
                print("\nDeposito efetuado com sucesso!: ")

            else:
                print("\nImpossível depositar este valor. Deposito não realizado.")
        
        except ValueError:
           print("\nDigite um valor válido")