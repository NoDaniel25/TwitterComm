import networkx as nx
from networkx import node_connected_component
from networkx.algorithms.community.centrality import girvan_newman
from networkx.algorithms.community.kernighan_lin import kernighan_lin_bisection
from networkx.algorithms.community.louvain import louvain_communities
from networkx.algorithms.community.asyn_fluid import asyn_fluidc
from networkx.algorithms.community.modularity_max import greedy_modularity_communities, naive_greedy_modularity_communities
from visualisationUtils import *
import matplotlib.pyplot as plt
import csv
from igraph import *


#def showGraph():
    #plt.show()

def printCommunities(comm):
    for com in comm:
        print(com)

def getNumberOfCommunities(size, algName):
    path = "../output/numbers/" + str(size) + "Test.csv"
    G = loadUndirectedGraph(path)
    #print("../output/numbers/" + str(item) + "Test.csv")
    return getCommunities(G, algName)

def loadDirectedGraph(filename):
    G = nx.DiGraph()
    # print(filename)
    graph = nx.Graph()
    edges = nx.read_edgelist
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        # print(csv_file)
        for row in csv_reader:
            # print(row[0], row[1])
            G.add_edge(row[0], row[1])
            line_count += 1
        print(f'Processed {line_count} lines.')
    return G

def loadUndirectedGraph(filename):
    G = nx.Graph()
    # print(filename)
    graph = nx.Graph()
    edges = nx.read_edgelist
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        # print(csv_file)
        for row in csv_reader:
            # print(row[0], row[1])
            G.add_edge(row[0], row[1])
            line_count += 1
        print(f'Processed {line_count} lines.')
    return G

#girvan_newman
def plotGraphGN(G, item, algName, min_size = 5):
    comm = girvan_newman(G)
    #print(comm)
    node_groups = []
    for com in next(comm):
        node_groups.append(list(com))
    #printCommunities(node_groups)
    print(node_groups)
    showCommunityGraph(node_groups, G, item, algName)

def getCommunities(G, algName):
    node_groups = []
    node_sizes = []
    if(algName == "GN"):
        comm = girvan_newman(G)

        for com in next(comm):
            node_groups.append(list(com))
    elif(algName == "LC"):
        comm = louvain_communities(G)
        node_groups = comm
    else:
        comm = greedy_modularity_communities(G)
        node_groups = comm



    for val in node_groups:
        node_sizes.append(len(val))

    node_sizes.sort(reverse=True)

    return node_sizes


# kernighan_lin_bisection
# needs undirected graph
def plotGraphKLB(G, item, algName, min_size = 5):
    comm = list(kernighan_lin_bisection(G, max_iter=100))
    node_groups = []
    for com in next(comm):
        node_groups.append(list(com))
    print(comm)
    showCommunityGraph(node_groups, G, item, algName)

# louvain_communities
def plotGraphLC(G, item, algName, min_size = 5):
    comm = louvain_communities(G)
    showCommunityGraph(comm, G, item, algName)

# asyn_fluidc
def plotGraphAF(G, k, item, algName, min_size = 5):
    comm = asyn_fluidc(G, k=1)
    node_groups = []
    for com in next(comm):
        node_groups.append(list(com))
        asd = node_connected_component(G, com[0])
        printCommunities(comm, asd, item, algName)

# greedy_modularity_communities
def plotGraphGMC(G, item, algName, min_size = 5):
    comm = greedy_modularity_communities(G)
    showCommunityGraph(comm, G, item, algName)

# naive_greedy_modularity_communities
def plotGraphNGMC(G, item, algName, min_size = 5):
    comm = naive_greedy_modularity_communities(G)
    print("asd2")
    showCommunityGraph(comm, G, item, algName)


