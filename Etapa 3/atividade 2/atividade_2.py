""""
    Calcular Média: Crie uma função que calcule a média das notas para cada aluno.
    Identificar Aprovados: Crie uma função que identifique os alunos com média maior ou igual a 7.
    Gerar Relatório: Crie uma função que retorne um relatório com o nome do aluno, a média calculada e o status (Aprovado quando a nota for maior que 6, senão Reprovado)."""

import pandas as pd

#Carrega o arquivo alunos_csv

def carregar_csv_alunos():
    df_csv = pd.read_csv('alunos.csv')
    print("DataFrame lido de CSV:")
    print(df_csv)

#Calcula a media das notas de cada aluno

def calcular_media(df):
    df['media'] = df[['nota1', 'nota2', 'nota3']] /3
    return df

#Identifica os alunos com média maior ou igual a 7.

def identificar_aprovados(df):
    return df[df['media'] >= 7]

#Gera um relatório com nome, média e status de aprovação dos alunos

def gerar_relatorio(df):
    df['status'] = df['media'].apply(lambda x: 'Aprovado' if x >= 6 else 'Reprovado')
    return df[['aluno', 'media', 'status']]

# Salva o resultado do relatorio
def salvar_resultado(df, relatorio): 
    df.to_csv(relatorio, index=False)
    print("Arquivo 'relatorio.csv' salvo.")

if __name__ == "__main__":
    nome_arquivo = "alunos.csv"
    df = carregar_csv_alunos(nome_arquivo)
    df = calcular_media(df)
    df_relatorio = gerar_relatorio(df)
    salvar_resultado(df_relatorio, "relatorio_alunos.csv")
    print("Processamento concluído. Arquivo 'relatorio_alunos.csv' salvo.")

