import pandas as pd
import json

# Ler o arquivo JSON

def ler_arquivo_json ():
    df_json = pd.read_json('usuarios.json')

#Converter os dados para um DataFrame

def converterDataFrame():
    df_json = pd.json_normalize(df_json['usuarios'])
    print("DataFrame lido de JSON:")
    print(df_json)

#Filtrar os usuários com idade maior que 18 anos

def filtrar_idade_usuarios(df):
    return df[df['idade'] > 18]

#Ordena os usuários por idade.

def ordenar_usuarios(df):
    df_ordenado = df_json.sort_values(by='idade')
    print("DataFrame ordenado por 'idade':")
    print(df_ordenado)

# Retorna um relatório final como uma lista de dicionários com os dados processados. 

def gerar_relatorio(df):
    lista_registros = df.to_dict(orient='records')
    print("DataFrame convertido para lista de dicionários:")
    print(lista_registros)

if __name__ == "__main__":
    nome_arquivo = "usuarios.json"
    df = ler_arquivo_json(nome_arquivo)
    df = filtrar_idade_usuarios(df)
    df = ordenar_usuarios(df)
    relatorio = gerar_relatorio(df)
    salvar_resultado(df, "usuarios_filtrados.json")
    print("Processamento concluído. Arquivo 'usuarios_filtrados.json' salvo.")

