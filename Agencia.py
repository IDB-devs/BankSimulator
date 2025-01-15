from random import randint


class Agencia:
    
    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []
        
    def verificar_caixa(self):
        if self.caixa < 1000000:
            print(f'Caixa abaixo do nível recomendado. Caixa atual: {self.caixa}')
        else:
            print(f'O valor do caixa está Ok. Caixa atual: {self.caixa}')
            
    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print('Empréstimos não é possível. Dinheiro não disponível em caixa.')    
            
    def adiconar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))


class AgenciaVirtual(Agencia):
    
    def __init__(self, site, telefone, cnpj):
        self.site = site #criando o atributo extra site
        super().__init__(telefone, cnpj, 1000) #puxando o init da superclasse acima
        self.caixa = 1000000
        self.caixa_paypal = 0
        
    def depositar_paypal(self, valor):
        self.caixa -= valor
        self.caixa_paypal += valor
    
    def sacar_paypal(self, valor):
        self.caixa_paypal -= valor
        self.caixa += valor


class AgenciaComum(Agencia):
    
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999)) #gerando numero aleatorio de agencia
        self.caixa = 1000000


class AgenciaPremium(Agencia):
    
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 10000000
        
    def adiconar_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            super().adiconar_cliente(nome, cpf, patrimonio) #roda o metodo igual ao da super classe
        else:
            print('O cliente não tem o patrimonio mínimo para entrar na agência premium')
    

if __name__ == "__main__": #não roda em outro arquivo caso seja importado
    
    agencia_premium = AgenciaPremium(22225555, 152000000)
    agencia_premium.caixa = 100000
    agencia_premium.verificar_caixa()
    agencia_premium.adiconar_cliente('lira', 1500000000, 50000000)
    print(agencia_premium.clientes)