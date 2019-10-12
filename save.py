import networkx as nx
import matplotlib.pylab as plt
import csv
import numpy as np
import os
from datetime import datetime

class Save:


	global cmaps
	cmaps = [
	            'Grey', 'Purple', 'Blue', 'Green', 'Orange', 'Red',
	            'Yellow','Grey', 'Purple', 'Blue', 'Green', 'Orange', 'Red','Grey', 'Purple', 'Blue', 'Green', 'Orange', 'Red',]


	def __init__(self, G):
		self.G = G

		self.path = "output/%s/" % self.G.__str__()
		self.subpath = datetime.now().strftime("%d.%m.%y-%H.%M.%S/")
		self.path += self.subpath

		if not os.path.exists(self.path):
		    os.makedirs(self.path)

		self.nodes = nx.from_numpy_matrix(self.G.adj)
		self.draw()
		self.data()
		


	def draw(self):

		plt.figure()

		color_map = []

		for i in range(0, self.G.M):
			for j in range(i * self.G.nodes_per_community,(i+1) * self.G.nodes_per_community):
				color_map.append(cmaps[i])


		plt.figure(figsize=(14,9))
		nx.draw(self.nodes,node_color = color_map,with_labels = False, node_size=15)
		plt.suptitle("Random Clustered Graph - %s" % self.G.name)
		plt.draw()
		plt.savefig(self.path + "%s.png" % self.G.name)
		plt.close()


	def data(self):

		# SAVE PLOT

		plt.figure(figsize=(11,10))
		plt.spy(self.G.adj,markersize=2)
		plt.suptitle("Random Clustered Graph - %s" % self.G.name)

		plt.text(-40, -5, "M: %d\nN: %d\nK: %d\nP(in): %.2f\nP(out): %.2f" % (self.G.M, self.G.N, self.G.K, self.G.PIN, self.G.POUT))

		plt.savefig(self.path + ("%s-rcg.png" % self.G.name))
		#plt.savefig(self.path + ("rcg-%d-%d-%.2f-%.2f.pdf" % (self.M, self.N, self.PIN, self.POUT)))
		plt.close()

		# SAVE GRAPH
		with open(self.path + ("%s-linked.csv" % self.G.name), 'w') as f:  # Just use 'w' mode in 3.x
		    w = csv.DictWriter(f, self.G.graph.keys())
		    w.writeheader()
		    w.writerow(self.G.graph)

	    # SAVE GRAPH
		np.savetxt(self.path + ("%s-adj.csv" % self.G.name), self.G.adj, delimiter=",", fmt="%d")