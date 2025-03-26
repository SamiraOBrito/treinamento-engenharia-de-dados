import pandas as pd

# Ler o arquivo CSV

def ler_arquivo_csv ():
    df_csv = pd.read_csv('dados_agregacao.csv')

#Converter os dados para um DataFrame

def converterDataFrame(dados_agregacao):
    df_csv = pd.read_csv(dados_agregacao)
    print("DataFrame lido de CSV:")
    print(df_csv)

# Agrupa os dados pela categoria e calcula a soma e a média dos valores

def agregar_dados (df):
    agregados = df_agregacao.groupby('categoria')['valor'].agg(soma_valor='sum', media_valor='mean').reset_index()
    print("Dados agregados por categoria:")
    print(agregados)


# Salva o DataFrame das agregações em um arquivo Parquet

def salvar_em_parquet():
    agregados.to_parquet('dados_agregados.parquet', index=False)
    print("Arquivo 'dados_agregados.parquet' salvo.")

# Lê o arquivo Parquet e retorna um DataFrame para validação

def carregar_validar_parquet(dados_agregacao):
    return pd.read_parquet(dados_agregacao)

if __name__ == "__main__":
    nome_arquivo = "dados_agregacao.csv"
    df = ler_arquivo_csv(nome_arquivo)
    df_agregado = agregar_dados(df)
    salvar_em_parquet(df_agregado, "dados_agregados.parquet")
    df_validado = carregar_validar_parquet("dados_agregados.parquet")
    print("Processamento concluído. Arquivo 'dados_agregados.parquet' salvo e validado.")