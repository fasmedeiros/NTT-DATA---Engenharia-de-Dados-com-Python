# Desafio de Código
## Dominando Filtragem e Extração de Dados com Python

## 1. Filtragem de Visuais

### Função `filtrar_visuais(lista_visuais)`
Remove duplicatas e normaliza os nomes de visuais em uma lista.

- **Parâmetro:** 
  `lista_visuais` (str): Uma string contendo tipos de visuais separados por vírgulas.
  
- **Retorna:** 
  Uma string com visuais únicos e normalizados, formatados em "Título Capitalizado".

### Exemplo de Uso
```python
def filtrar_visuais(lista_visuais):
    # Converter a string de entrada em uma lista
    visuais = lista_visuais.split(", ")
    
    # Normalizar e remover duplicatas usando um conjunto
    visuais_normalizados = {visual.title() for visual in visuais}
    
    # Converter o conjunto de volta para uma lista ordenada
    lista_final = sorted(visuais_normalizados)

    # Unir a lista em uma string, separada por vírgulas
    return ", ".join(lista_final)

# Capturar a entrada do usuário
entrada_usuario = "Gráfico de Barras, Gráfico de Barras, Tabela, Gráfico de Pizza, gráfico de barras"

# Processar a entrada e obter a saída
saida = filtrar_visuais(entrada_usuario)
print(saida)  # Saída: "Gráfico De Barras, Gráfico De Pizza, Tabela"
```

---

## 2. Extração de Anos

### Função `extrair_anos(datas)`
Extrai os anos de uma lista de datas no formato "YYYY-MM-DD".

- **Parâmetro:** 
  `datas` (str): Uma string contendo datas separadas por vírgula e espaço.
  
- **Retorna:** 
  Uma string com os anos extraídos, separados por vírgulas.

### Exemplo de Uso
```python
def extrair_anos(datas):
    # Divide a string de datas em uma lista
    lista_datas = datas.split(", ")
    # Extraí o ano de cada data e cria uma nova lista com os anos
    anos = [data.split("-")[0] for data in lista_datas]
    
    # Junta os anos em uma string separada por vírgula e retorna
    return ", ".join(anos)

# Capturar a entrada do usuário
entrada = "2024-01-15, 2023-11-22, 2024-05-10"

# Chame a função para imprimir o resultado
saida = extrair_anos(entrada)
print(saida)  # Saída: "2024, 2023, 2024"
```

---

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou um pull request.
