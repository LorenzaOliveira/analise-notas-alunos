
import pandas as pd

#Ler a planilha do Excel
dados = pd.read_excel("notas.xlsx")

colunas_notas = ["Nota 1", "Nota 2", "Nota 3"]

#Verificar se as colunas existem
for coluna in ["Aluno"] + colunas_notas:
    if coluna not in dados.columns:
        raise ValueError(f"Coluna não encontrada: {coluna}")

#Verificar se todas as notas são números válidos
for coluna in colunas_notas:
    dados[coluna] = pd.to_numeric(dados[coluna], errors="coerce")

if dados[["Aluno"] + colunas_notas].isna().any().any():
    raise ValueError("Existem nomes ou notas vazios ou inválidos.")

if ((dados[colunas_notas] < 0) |
        (dados[colunas_notas] > 10)).any().any():
    raise ValueError("As notas devem estar entre 0 e 10.")

#Calcular a média de cada aluno
dados["Média"] = dados[colunas_notas].mean(axis=1)

#Encontrar os alunos com maior e menor média
maior_media = dados["Média"].max()
menor_media = dados["Média"].min()

print("\n--- MAIOR DESEMPENHO ---")
print(dados[dados["Média"] == maior_media][["Aluno", "Média"]])
print("Maior média:", round(maior_media, 2))

print("\n--- MENOR DESEMPENHO ---")
print(dados[dados["Média"] == menor_media][["Aluno", "Média"]])
print("Menor média:", round(menor_media, 2))

#Mostrar todos os alunos em ordem de desempenho
print("\n--- CLASSIFICAÇÃO DOS ALUNOS ---")
print(
    dados[["Aluno", "Nota 1", "Nota 2", "Nota 3", "Média"]]
    .sort_values("Média", ascending=False)
    .to_string(index=False)
)

#Analisar o resultado geral da turma
nota_minima = 6

aprovados = dados[dados["Média"] >= nota_minima]
reprovados = dados[dados["Média"] < nota_minima]

print("\n--- RESULTADO DA TURMA ---")
print("Média geral:", round(dados["Média"].mean(), 2))
print("Quantidade de alunos:", len(dados))
print("Aprovados:", len(aprovados))
print("Abaixo da média mínima:", len(reprovados))



