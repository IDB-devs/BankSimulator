from datetime import datetime
import pytz
from random import randint # numeros inteiros aleatorios


class ContaCorrente:
    """
    Cria um objeto ContaCorrente para gerenciar as contas dos clientes.

    Atributos:
        nome (str): nome do cliente
        cpf (str): cpf do cliente. deve ser inserido com pontos e traços.
        agencia (int): agencia responsável pela conta do cliente
        num_conta (int): número da conta corrente do cliente
        saldo (float): saldo disponível na conta do cliente
        limite (float): limite de cheque especial daquele cliente
        transacoes (list): histórico de transações do cliente
        cartoes (list): cartoes da conta
        
    """
    
    @staticmethod # metodo estatico auxiliar (não precisa de nada dentro da classe pra funcionar)
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East') # fuso horario de brasilia
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S') # formatacao datetime pra visual melhor
    
    def __init__(self, nome, cpf, agencia, num_conta): #funcao inicial ond vai todos os atributos da classe para facil acesso
        self.nome = nome
        self.cpf = cpf # um atributo q pode ser consultado mas n modificado fora da classe apenas pelos métodos da classe
        self._saldo = 0
        self._limite = None
        self.__agencia = agencia # torna o atributo inacessivel fora da classe
        self._num_conta = num_conta
        self._transacoes = []
        self.cartoes = []
    
    def consultar_saldo(self):
        """
        Exibe o saldo atual da conta do cliente.
        Não há parâmetros necessários.
        """
        print(f'seu saldo atual é de R${self._saldo:,.2f}')
        
    def depositar(self, valor):
       self._saldo += valor
       self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))
       
    def _limite_conta(self): # funcao privada (não é para usada fora da classe)
        self._limite = -1000
        return self._limite
    
    def sacar_dinheiro(self, valor):
        if self._saldo - valor < self._limite_conta():
            print('você não tem saldo suficiente para sacar esse valor')
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
            
    def consultar_limite_chequeespecial(self):
        print(f'Seu limite de cheque especial é de R${self._limite_conta():,.2f}')
        
    def consultar_historico_transacoes(self):
        print('Histórico de Transações: ')
        print('Valor, Saldo, Data e Hora')
        for transacao in self._transacoes:
            print(transacao)
            
    def transferir(self, valor, conta_destino):
        if self._saldo - valor < self._limite_conta():
            print('você não tem saldo suficiente para transferir esse valor')
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
            conta_destino._saldo += valor
            conta_destino._transacoes.append((valor, conta_destino._saldo, ContaCorrente._data_hora()))
                

class CartaoCredito:
    
    @staticmethod # metodo estatico auxiliar (não precisa de nada dentro da classe pra funcionar)
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East') # fuso horario de brasilia
        horario_BR = datetime.now(fuso_BR)
        return horario_BR
    
    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000000000000000, 9999999999999999) # nao colocar 0 no começo do min pq pod considerar como 0 sem contar os digitos
        self.titular = titular
        self.validade = f'{CartaoCredito._data_hora().month}/{CartaoCredito._data_hora().year + 4}'
        self.cod_seguranca = f'{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}' #macete para poder comecar com 0
        self.limite = 1000
        self._senha = '1234'
        self.conta_corrente = conta_corrente # vincular a uma conta corrente
        conta_corrente.cartoes.append(self) # para adc o cartão na conta corrente
        
    @property #definir um metodo get #utilizar qnd precisar de uma validação ou restrição
    def senha(self):
        #logica
        return self._senha
    
    @senha.setter #definir metodo set #utilizar qnd precisar de uma validação ou restrição
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
        else:
            print('nova senha inválida')
            
            