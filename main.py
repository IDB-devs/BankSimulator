from ContasBancos import ContaCorrente, CartaoCredito #importando a classe do arquivo coms classes
from Agencia import Agencia, AgenciaComum, AgenciaVirtual, AgenciaPremium #importar outro arquivo


# programa
conta_lira = ContaCorrente('Lira', '111.222.333-45', 1234, 34062)

cartao_lira = CartaoCredito('Lira', conta_lira)

print(cartao_lira.conta_corrente._num_conta)
print(conta_lira.cartoes)
print(cartao_lira.cod_seguranca)

cartao_lira.senha ='2345'
print(cartao_lira.senha)

# depositando dinheiro
#conta_lira.depositar(10000)
#conta_lira.consultar_saldo()

# sacar dinheiro
#conta_lira.sacar_dinheiro(10500)

#print('saldo final')
#conta_lira.consultar_saldo()
#conta_lira.consultar_limite_chequeespecial()

#conta_lira.consultar_historico_transacoes()

#print('-'*20)
#conta_maelira = ContaCorrente('Beth', '222.333.444-55', 5555, 656565)
#conta_lira.transferir(1000, conta_maelira)

#conta_lira.consultar_saldo()
#conta_maelira.consultar_saldo()

#conta_lira.consultar_historico_transacoes()
#conta_maelira.consultar_historico_transacoes()

agencia1 = Agencia(22223333, 200000000, 4568)

agencia_virtual = AgenciaVirtual('www.agenciavirtual.com.br', 22224444, 152000000)
agencia_virtual.verificar_caixa()
print(agencia_virtual.site)
agencia_virtual.depositar_paypal(20000)
print(agencia_virtual.caixa)
print(agencia_virtual.caixa_paypal)

agencia_premium = AgenciaPremium(22225555, 152000000)
agencia_premium.caixa = 100000
agencia_premium.verificar_caixa()
agencia_premium.adiconar_cliente('lira', 1500000000, 50000000)
print(agencia_premium.clientes)

agencia1.caixa = 1000000

agencia1.verificar_caixa()

agencia1.emprestar_dinheiro(1500, 12345678912, 0.02)

print(agencia1.emprestimos)

agencia1.adiconar_cliente('lira', 12345678912, 10000)
print(agencia1.clientes)

# help(ContaCorrente) para olhar o docstring de uma classe
# print(conta_lira.__dict__) para olhar os atributos de uma classe atraves de um dicionario