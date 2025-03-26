
"""Carregar Dados: Crie uma função que leia o arquivo vendas.csv e retorne um DataFrame.
    Calcular Valor Total: Crie uma função que adicione uma nova coluna valor_total ao DataFrame, calculada como quantidade * preco_unitario.
    Filtrar Vendas: Crie uma função que filtre os registros onde o valor_total seja superior a R$500.
    Salvar Resultado: Crie uma função que salve o DataFrame filtrado em um novo arquivo CSV."""

import pandas as pd

def ler_csv_de_vendas():
    df_csv = pd.read_csv('vendas.csv')
    print("DataFrame lido de CSV:")
    print(df_csv)

def calcular_valor_total():
    df_vendas['valor_total'] = df_vendas['quantidade'] * df_vendas['preco_unitario']
    print("DataFrame com coluna 'valor_total':")
    print(df_vendas)

def filtrar_vendas():
    df_filtrado = df_vendas[df_vendas['valor_total'] > 500]
    print("Vendas com valor_total > 500:")
    print(df_filtrado)

def salvar_resultado(): 
    df_filtrado.to_csv('vendas_filtradas.csv', index=False)
    print("Arquivo 'vendas_filtradas.csv' salvo.")

if __name__ == "__main__":
    nome_arquivo = "vendas.csv"
    df = ler_csv_de_vendas(df_csv)
    df = calcular_valor_total(df_vendas)
    df_filtrado = filtrar_vendas(df_filtrado)
    salvar_resultado(df_filtrado, "vendas_filtradas.csv")
    print("Processamento concluído. Arquivo 'vendas_filtradas.csv' salvo.")