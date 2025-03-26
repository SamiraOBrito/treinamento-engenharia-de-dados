# Dados fictícios
dados = [
    {"regiao": "Norte", "vendas": 100},
    {"regiao": "Sul", "vendas": 200},
    {"regiao": "Norte", "vendas": 150},
    {"regiao": "Sul", "vendas": 250},
]

# Dicionário para armazenar as médias
medias = {}

# Cálculo das médias
for linha in dados:
    regiao = linha["regiao"]
    vendas = linha["vendas"]
    
    if regiao not in medias:
        medias[regiao] = {"total": 0, "qtd": 0}
    
    medias[regiao]["total"] += vendas
    medias[regiao]["qtd"] += 1

for regiao, valores in medias.items():
    media = valores["total"] / valores["qtd"]
    print(f"Média de vendas na região {regiao}: {media}")