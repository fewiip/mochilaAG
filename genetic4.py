import random
import numpy as np
import matplotlib.pyplot as plt


# Definição do problema da mochila
#valores = [60, 100, 120]
#pesos = [10, 20, 30]
# Dados do problema: valores e pesos dos itens e capacidade da mochila
valores = [60, 100, 120, 90, 50, 70, 30, 80, 110, 40, 95, 85, 55, 65, 75]  # Valores dos itens
pesos = [10, 20, 30, 15, 25, 35, 10, 20, 40, 15, 25, 18, 28, 22, 12]  
#capacidade = 50
capacidade = 100
num_itens = len(valores)
populacao_size = 1000
#num_geracoes = 50
num_geracoes = 1000
taxa_mutacao = 0.1


# Função de aptidão
def fitness(individuo):
    valor_total = 0
    peso_total = 0
    for i in range(num_itens):
        if individuo[i] == 1:
            valor_total += valores[i]
            peso_total += pesos[i]
    if peso_total > capacidade:
        return 0
    else:
        return valor_total

# Seleção por roleta
def selecao_roleta(populacao, fitnesses):
    soma_fitness = sum(fitnesses)
    ponto_roleta = random.uniform(0, soma_fitness)
    atual = 0
    for i, fitness in enumerate(fitnesses):
        atual += fitness
        if atual >= ponto_roleta:
            return populacao[i]

# Mutação uniforme
def mutacao(individuo):
    for i in range(num_itens):
        if random.random() < taxa_mutacao:
            individuo[i] = 1 - individuo[i]
    return individuo

# Algoritmo genético
populacao = [[random.randint(0, 1) for _ in range(num_itens)] for _ in range(populacao_size)]
historico_valores = []
melhores_valores = []
ultimos_valores = []

for geracao in range(num_geracoes):
    fitnesses = [fitness(individuo) for individuo in populacao]
    nova_populacao = []
    for _ in range(populacao_size):
        pai1 = selecao_roleta(populacao, fitnesses)
        pai2 = selecao_roleta(populacao, fitnesses)
        ponto_corte = random.randint(1, num_itens - 1)
        filho = pai1[:ponto_corte] + pai2[ponto_corte:]
        filho = mutacao(filho)
        nova_populacao.append(filho)
    populacao = nova_populacao
    melhor_valor = max(fitnesses)
    ultimos_valores.append(fitnesses[len(fitnesses) - 1])
    #print('tamanho vetor fitness: ' + str(len(fitnesses)))
    historico_valores.append(melhor_valor)
    if geracao == num_geracoes - 1:
        melhores_valores.extend(fitnesses)
    print(f'Geração {geracao+1}: Melhor valor = {melhor_valor}')

# Plot do histograma dos melhores valores
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
#plt.hist(melhores_valores, bins=10, alpha=0.75, edgecolor='black')
plt.hist(ultimos_valores, bins=10, alpha=0.75, edgecolor='black')
plt.xlabel('Valores')
plt.ylabel('Frequência')
plt.title('Histograma dos ultimos valores de cada geração')

# Plot do histograma dos últimos valores por geração
plt.subplot(1, 2, 2)
plt.hist(historico_valores, bins=10, alpha=0.75, edgecolor='black')
plt.xlabel('Valores')
plt.ylabel('Frequência')
plt.title('Histograma dos melhores valores por geração')

plt.tight_layout()
plt.show()

