# import queue
# import itertools

import numpy as np


# Encontra caminho mínimo

class Dijkstra:
	def __init__(self, G, s):

        # Inicializa Dijkstra
		self.G = G
		self.dist = np.full(self.G.N, float("inf"))
		self.prev = np.full(self.G.N, -1)
		self.dist[s] = 0

        # Chama função auxiliar
		self.run()


	def run(self):
        
		Q = set([i for i in range(self.G.N)])

		while len(Q) > 0:

			min_dist = float("inf")
			min_node = None

			for q in Q:
				if self.dist[q] < min_dist:

					min_dist = self.dist[q]
					min_node = q				

			u = min_node
            
			if u is None:
				return

			Q.remove(u)

			for v in self.G.graph[u]:
				alt = self.dist[u] + 1

				if alt < self.dist[v]:
					self.dist[v] = alt
					self.prev[v] = u



class EccentricityD:
	

	def __init__(self, G):

		distances = list()

		for i in range(0, G.N):
			D = Dijkstra(G, i)
            
            # Excentricidade
			distances.append(np.nanmax(D.dist))

        # Seleciona raio e diametro
		self.radius = int(min(distances))
		self.diameter = int(max(distances))		

