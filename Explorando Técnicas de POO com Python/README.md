# Desafio de código
## Explorando Técnicas de POO com Python

Este projeto demonstra técnicas de Programação Orientada a Objetos (POO) em Python, focando na criação de classes que representam dados de vendas e na capacidade de agrupar essas vendas por categoria.

## 1 - Criando Classes para Dados de Vendas

### Descrição

Nesta seção, implementamos a classe `Venda`, que representa uma venda individual. Cada venda possui atributos como `produto`, `quantidade` e `valor`.

### Classe Venda

```python
class Venda:
    def __init__(self, produto, quantidade, valor):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor
```

### Atributos

- **produto**: O nome do produto vendido.
- **quantidade**: O número de unidades vendidas.
- **valor**: O valor total da venda.

### Uso

Exemplo de como criar uma instância da classe `Venda`:

```python
venda1 = Venda("Celular", 5, 1000)
print(venda1.produto)  # Saída: Celular
```

## 2 - Agrupamento de Vendas por Categoria

### Descrição

Aqui, implementamos a classe `Categoria`, que agrupa várias vendas. A classe permite adicionar vendas e calcular o total de vendas para cada categoria.

### Classe Categoria

```python
class Categoria:
    def __init__(self, nome):
        self.nome = nome
        self.vendas = []
    
    def adicionar_venda(self, venda):
        if isinstance(venda, Venda):
            self.vendas.append(venda)

    def total_vendas(self):
        return sum(venda.valor for venda in self.vendas)
```

### Atributos

- **nome**: O nome da categoria.
- **vendas**: Uma lista de objetos `Venda` associados a esta categoria.

### Métodos

- **adicionar_venda(venda)**: Adiciona uma venda à lista de vendas se o objeto passado for uma instância da classe `Venda`.
- **total_vendas()**: Retorna o total de vendas somando o valor de cada venda na lista.

### Uso

Exemplo de como criar uma instância da classe `Categoria` e adicionar vendas:

```python
categoria_eletronicos = Categoria("Eletrônicos")
venda1 = Venda("Celular", 5, 1000)
categoria_eletronicos.adicionar_venda(venda1)
print(f'Total de vendas em {categoria_eletronicos.nome}: {categoria_eletronicos.total_vendas()}')
```

## Conclusão

Este projeto ilustra a criação e o uso de classes em Python para gerenciar dados de vendas e agrupá-los de forma organizada. As técnicas de POO facilitam a manutenção e a escalabilidade do código, permitindo um gerenciamento mais eficiente de informações relacionadas a vendas.
