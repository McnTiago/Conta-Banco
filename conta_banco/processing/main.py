from cliente import Cliente
from conta import Conta

cliente1 = Cliente('teste', '123.456.789-10', 27)


conta_teste = Conta(cliente1, 10.50, 1000)

print(conta_teste.cliente.nome, conta_teste.consulta_saldo())

conta_teste.depositar(1000.40)

print(conta_teste.consulta_saldo())

conta_teste.sacar(500)

print(conta_teste.consulta_saldo())

conta_teste.sacar(1000)

print(conta_teste.consulta_saldo())