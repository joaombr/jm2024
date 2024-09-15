class Empregado:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base

    def __str__(self):
        return f'Nome: {self.nome}, Salário Base: R${self.salario_base:.2f}'

class Gerente(Empregado):
    def __init__(self, nome, salario_base, bonus):
        super().__init__(nome, salario_base)
        self.bonus = bonus

    def calcular_salario(self):
        return self.salario_base + self.bonus

    def __str__(self):
        return f'Nome: {self.nome}, Salário Base: R${self.salario_base:.2f}, Bônus: R${self.bonus:.2f}'

class Vendedor(Empregado):
    def __init__(self, nome, salario_base, comissao_por_venda, numero_vendas):
        super().__init__(nome, salario_base)
        self.comissao_por_venda = comissao_por_venda
        self.numero_vendas = numero_vendas

    def calcular_salario(self):
        return self.salario_base + (self.comissao_por_venda * self.numero_vendas)

    def __str__(self):
        return f'Nome: {self.nome}, Salário Base: R${self.salario_base:.2f}, Comissão por Venda: R${self.comissao_por_venda:.2f}, Número de Vendas: {self.numero_vendas}'
    
class Entregador(Empregado):
    def __init__(self, nome, salario_base, comissao_por_entrega, numero_entrega):
        super().__init__(nome, salario_base)
        self.comissao_por_entrega = comissao_por_entrega
        self.numero_entrega = numero_entrega

    def calcular_salario(self):
        return self.salario_base + (self.comissao_por_entrega * self.numero_entrega)

    def __str__(self):
        return f'Nome: {self.nome}, Salário Base: R${self.salario_base:.2f}, Comissão por Entrega: R${self.comissao_por_entrega:.2f}, Número de Entregas: {self.numero_entrega}'

def main():
    # Criar um gerente
    gerente = Gerente(nome="Braga", salario_base=5000.00, bonus=2000.00)
    print(gerente)
    print(f'Salário Total do Gerente: R${gerente.calcular_salario():.2f}\n')

    # Criar um vendedor
    vendedor = Vendedor(nome="Pedro", salario_base=1700.00, comissao_por_venda=15.00, numero_vendas=60)
    print(vendedor)
    print(f'Salário Total do Vendedor: R${vendedor.calcular_salario():.2f}\n')

    # Criar um entregador
    entregador = Entregador(nome="Kelven", salario_base=1800.00, comissao_por_entrega=10.00, numero_entrega=60)
    print(entregador)
    print(f'Salário Total do Entregador: R${entregador.calcular_salario():.2f}\n')

if __name__ == "__main__":
    main()
