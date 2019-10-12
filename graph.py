#coding: utf8
import random
import numpy as np

class CRG:
							# Define parâmetros default
	def __init__(self, name, N=200, M=4, K=16, PIN=0.9, POUT=0):

		self.name = name
		self.N = N
		self.M = M
		self.K = K
		self.PIN = PIN
		self.POUT = POUT
		self.nodes_per_community = self.N//self.M # > 1

		# Inicializa dicionário (representação de lista ligada) contendo comunidades
		self.categorized_nodes = {
				i: [N for N in range((i * self.nodes_per_community), ((i+1) * self.nodes_per_community))] for i in range(self.M)
				}

		# No caso de N for ímpar, último node é adicionado na categoria M (índice M-1)
		for i in range(self.nodes_per_community * self.M, self.N):
			self.categorized_nodes[M-1].append(i)


		# Inicializa grafo e representação por matriz de adjacência
		self.graph = {i:[] for i in range(self.N)}
		self.adj = np.zeros((self.N, self.N), dtype=int)

		self.generate()
		self.cvt_linked_2_adj()
	


	# Cria uma aresta entre dois vértices
	# pre: grafo inicializado
	# pos: aresta é criada node1 -> [node2] e node2 -> [node1]
	def add_edge(self, node1, node2):
		if (not node2 in self.graph[node1]) and (not node1 in self.graph[node2]):
			self.graph[node1].append(node2)
			self.graph[node2].append(node1)

	# Remove uma aresta entre dois vértices
	# pre: grafo inicializado e existe aresta
	# pos: aresta é node2 é removida de node1 e aresta é node1 é removida de node2
	# node -> []
	def remove_edge(self, node1, node2):
		if node2 in self.graph[node1]:
			self.graph[node1].remove(node2)
		if node1 in self.graph[node2]:
			self.graph[node2].remove(node1)


	# Calcula grau médio do grafo
	# pre: grafo inicializado
	# pos: grau médio é retornado, desconsiderando decimais
	def get_degree(self):
		total = 0

		for i in self.graph:
			total += len(self.graph[i])

		total //= self.N
		return total

	# Converte representação do grafo de lista ligada para matriz de adjacência
	# pre: grafo inicializado
	# pos: self.adj é atualizado para corresponder à representação da lista ligada
	def cvt_linked_2_adj(self):
		for i in self.graph:
			for j in self.graph[i]:
				self.adj[i][j] = 1

	# Algoritmo para gerar grafo randomico clusterizado
	# pre: grafo e parametros inicializados
	# pos: gera grafo randomico clusterizado em lista ligada 
	def generate(self):

		# repete até que grau médio seja atingido
		while self.get_degree() <= self.K:

			

			# Comunidade é selecionada aleatoriamente, então,
			# dois de seus vértices são selecionados aleatoriamente
			if (random.random() < self.PIN):

				current_community = random.randint(0, self.M-1)
				
				newedges = random.sample(self.categorized_nodes[current_community], 2)

				self.add_edge(newedges[0], newedges[1])


			# Comunidades diferentes são selecionadas aleatoriamente, então,
			# dois de seus vértices são selecionados aleatoriamente, um de cada comunidade		
			if (random.random() < self.POUT):

				communities = [i for i in range(self.M)]
				select_communities = random.sample(communities, 2)

				newedge1 = random.sample(self.categorized_nodes[select_communities[0]], 1)
				newedge2 = random.sample(self.categorized_nodes[select_communities[1]], 1)
				
				newedges = newedge1 + newedge2

				self.add_edge(newedges[0], newedges[1])


	def __str__(self):
		return self.name