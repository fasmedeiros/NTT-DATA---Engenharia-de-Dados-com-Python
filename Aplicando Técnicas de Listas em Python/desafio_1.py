def analise_vendas(vendas):
    # TODO: Calcule o total de vendas e realize a média mensal:
    total_vendas = sum(vendas)
    media_vendas = total_vendas / len(vendas)
    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()
    # TODO: Converta a entrada em uma lista de inteiros:
    vendas = list(map(int, [x.strip() for x in entrada.split(',')]))
    return vendas

def main():
    vendas = obter_entrada_vendas()
    resultado = analise_vendas(vendas)
    print(resultado)

if __name__ == "__main__":
    main()
