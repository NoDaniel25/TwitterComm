#from mysite.myapp.source.visualisationUtils import *
import csv

import networkx as nx
from pylab import *
from io import StringIO
import random
import mplcursors

min_size = 5

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

def showCommunityGraph(node_group, G, item, algName, min_size = 5):
    # plot the communities
    r = list(random.choices(range(256), k=125))
    g = list(random.choices(range(256), k=125))
    b = list(random.choices(range(256), k=125))
    color_map = []
    for val in zip(r, g, b):
        color_map.append(rgb_to_hex((val)))
    node_color = []
    new_node_group = []
    cluster_size = [0] * len(node_group)

    for val in node_group:
        print(len(val))
        print(min_size)
        if len(val) < min_size:
            for node in val:
                G.remove_node(node)
        else:
            new_node_group.append(val)

    for node in G:
        for i in range(0, len(new_node_group)):
            if node in new_node_group[i]:
                cluster_size[i] += 1
                node_color.append(color_map[i])

    plt.figure(figsize=(20, 14))
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, node_color=node_color, pos=pos)
    nx.draw_networkx_edges(G, pos=pos)

    plt.savefig("../output/images/" + str(item) + algName)

    plt.figure(figsize=(20, 14))
    nx.draw_networkx_nodes(G, node_color=node_color, pos=pos)
    nx.draw_networkx_edges(G, pos=pos)
    nx.draw_networkx_labels(G, pos=pos)

    plt.savefig("../output/images/" + str(item) + algName + "WNames")


def getCommunitiesSizes(node_group):
    clusters_sizes = []
    i = 0
    for node in node_group:
        clusters_sizes[i] = len(node)
        i+=1

    return clusters_sizes

def getPos(G, color_map, node_color):
    pos = nx.circular_layout(G)  # replaces your original pos=...
    # prep center points (along circle perimeter) for the clusters
    angs = np.linspace(0, 2 * np.pi, 1 + len(color_map))
    repos = []
    rad = 3.5  # radius of circle
    for ea in angs:
        if ea > 0:
            # print(rad*np.cos(ea), rad*np.sin(ea))  # location of each cluster
            repos.append(np.array([rad * np.cos(ea), rad * np.sin(ea)]))
    for ea in pos.keys():
        # color = 'black'
        posx = 0
        posInColors = 0
        for val in node_color:
            posInColors+=1
            if ea in val:
                posx = posInColors
        pos[ea] += repos[posx]
    return pos


def plotLoadingTimes(filename):
    list = []
    x = []
    y = []
    x1 = []
    y1 = []
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        # print(csv_file)
        for row in csv_reader:
            list.append([row[0], row[1]])
            x.append(row[1])
            y.append(int(row[0]))

            x1.append(float(row[1]))
            y1.append(int(row[0]))

    plt.figure(figsize=(20, 14))
    plt.plot(x, y)
    plt.xlabel("Time(seconds)")
    plt.ylabel("Sample size")
    plt.title("Loading Times")
    plt.savefig("../output/images/OriginalLoadingTimes")
    mplcursors.cursor(hover=True)
    #plt.show()

    plt.figure(figsize=(20, 14))
    plt.plot(x1, y1)
    plt.xlabel("Time(seconds)")
    plt.ylabel("Sample size")
    plt.title("Loading Times")
    mplcursors.cursor(hover=True)
    plt.savefig("../output/images/SmoothedLoadingTimes")

def plotTimes(filename):
    list = []
    x = []
    y = []
    x1 = []
    y1 = []
    path = "../output/benchmarks/numbers/" + filename + ".csv"
    print(path)
    with open(path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        # print(csv_file)
        for row in csv_reader:
            list.append([row[0], row[1]])
            print(row[1], row[0])
            x.append(row[0])
            y.append(row[1])

            x1.append(row[0])
            y1.append(float(row[1]))

    plt.figure(figsize=(20, 14))
    plt.plot(x, y)
    plt.ylabel("Time(seconds)")
    plt.xlabel("Sample size")
    plt.title("Loading Times")
    plt.savefig("../output/images/Benchmark" + filename)
    mplcursors.cursor(hover=True)
    #plt.show()

    plt.figure(figsize=(20, 14))
    plt.plot(x1, y1)
    plt.ylabel("Time(seconds)")
    plt.xlabel("Sample size")
    plt.title("Loading Times")
    mplcursors.cursor(hover=True)
    plt.savefig("../output/images/SmoothedBenchmark" + filename)

def plotTimeComparison():
    list = []
    x = []
    y = []
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    path = "../output/benchmarks/numbers/BenchmarkGN.csv"
    path1 = "../output/benchmarks/numbers/BenchmarkLC.csv"
    path2 = "../output/benchmarks/numbers/BenchmarkGMC.csv"
    with open(path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        # print(csv_file)
        for row in csv_reader:
            x.append(row[0])
            y.append(float(row[1]))

    print("before asd")
    with open(path1, 'r') as csv_file:
        print("asd")
        csv_reader = csv.reader(csv_file)
        line_count = 0
        # print(csv_file)
        for row in csv_reader:
            print("ceva")
            print(row[0], float(row[1]))
            x1.append(row[0])
            y1.append(float(row[1]))

    with open(path2, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        # print(csv_file)
        for row in csv_reader:
            x2.append(row[0])
            y2.append(float(row[1]))

    plt.figure(figsize=(20, 14))
    plt.plot(x, y, color = 'r')
    plt.plot(x1, y1, color = 'b')
    plt.plot(x2, y2, color = 'g')


    plt.ylabel("Time(seconds)")
    plt.xlabel("Sample size")
    plt.title("Loading Times")
    plt.savefig("../output/images/BenchmarkComparison")
    mplcursors.cursor(hover=True)
    #plt.show()

def plotTimeComparison2():
    list = []
    x = []
    y = []
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    path1 = "../output/benchmarks/numbers/BenchmarkLC.csv"
    path2 = "../output/benchmarks/numbers/BenchmarkGMC.csv"

    with open(path1, 'r') as csv_file1:
        csv_reader1 = csv.reader(csv_file1)
        line_count = 0
        # print(csv_file)
        for row in csv_reader1:
            x1.append(row[0])
            y1.append(float(row[1]))

    with open(path2, 'r') as csv_file2:
        csv_reader2 = csv.reader(csv_file2)
        line_count = 0
        # print(csv_file)
        for row in csv_reader2:
            x2.append(row[0])
            y2.append(float(row[1]))

    plt.figure(figsize=(20, 14))
    plt.plot(x2, y2, color = 'g')
    plt.plot(x1, y1, color = 'b')

    plt.ylabel("Time(seconds)")
    plt.xlabel("Sample size")
    plt.title("Loading Times")
    plt.savefig("../output/images/BenchmarkComparison2")
    mplcursors.cursor(hover=True)
    #plt.show()

def return_graph():

    x = np.arange(0,np.pi*3,.1)
    y = np.sin(x)

    fig = plt.figure()
    plt.plot(x,y)

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    data = imgdata.getvalue()
    return data