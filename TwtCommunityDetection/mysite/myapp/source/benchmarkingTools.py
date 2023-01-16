import mysite.myapp.source.graphUtils as gutils
from mysite.myapp.source.graphUtils import *
from mysite.myapp.source.parser import *


def actionStartTime():
    start_time = time.start()

def prepareFor(sizeLists):
    for item in sizeLists:
        createPartialDataset(item)

def timeGraphCommunityGN(sizeLists):
    times = []
    initializeWriter('BenchmarkGN', '../output/benchmarks/numbers/')
    for item in sizeLists:
        path = "../output/numbers/" + str(item) + "Test.csv"
        G = loadUndirectedGraph(path)
        #print("../output/numbers/" + str(item) + "Test.csv")
        time = benchmarkPlotGraphGN(G, item, "GN")
        times.append([item, time])

    writeList(times)

def timeGraphCommunityKLB(sizeLists):
    times = []
    initializeWriter('Benchmark', '../output/benchmarks/numbers/')
    for item in sizeLists:
        path = "../output/numbers/" + str(item) + "Test.csv"
        G = loadUndirectedGraph(path)
        #print("../output/numbers/" + str(item) + "Test.csv")
        time = benchmarkPlotGraphKLB(G, item, "KLB")
        times.append([item, time])

    writeList(times)

def timeGraphCommunityLC(sizeLists):
    times = []
    initializeWriter('BenchmarkLC', '../output/benchmarks/numbers/')
    for item in sizeLists:
        path = "../output/numbers/" + str(item) + "Test.csv"
        G = loadUndirectedGraph(path)
        #print("../output/numbers/" + str(item) + "Test.csv")
        time = benchmarkPlotGraphLC(G, item, "LC")
        times.append([item, time])

    writeList(times)


def timeGraphCommunityAF(sizeLists):
    times = []
    initializeWriter('BenchmarkAF', '../output/benchmarks/numbers/')
    for item in sizeLists:
        path = "../output/numbers/" + str(item) + "Test.csv"
        G = loadUndirectedGraph(path)
        #print("../output/numbers/" + str(item) + "Test.csv")
        time = benchmarkPlotGraphAF(G, 4, item, "AF")
        times.append([item, time])

    writeList(times)

def timeGraphCommunityGMC(sizeLists):
    times = []
    initializeWriter('BenchmarkGMC', '../output/benchmarks/numbers/')
    for item in sizeLists:
        path = "../output/numbers/" + str(item) + "Test.csv"
        G = loadUndirectedGraph(path)
        #print("../output/numbers/" + str(item) + "Test.csv")
        time = benchmarkPlotGraphGMC(G, item, "GMC")
        times.append([item, time])

    writeList(times)

def timeGraphCommunityNGMC(sizeLists):
    times = []
    initializeWriter('BenchmarkNGMC', '../output/benchmarks/numbers/')
    for item in sizeLists:
        path = "../output/numbers/" + str(item) + "Test.csv"
        G = loadUndirectedGraph(path)
        #print("../output/numbers/" + str(item) + "Test.csv")
        time = benchmarkPlotGraphNGMC(G, item, "NGMC")
        times.append([item, time])

    writeList(times)

def timeLoadingDataset(sizeLists):

    times = []
    for item in sizeLists:
        start_time = time.time()
        print("Starting dataset loading and parsing for ", item,  " rows...")

        initializeWriter('timeBenchmark' + str(item), '../output/benchmarks/numbers/')
        df = readDataset('data')
        df = parseQuates(df)
        df = cutDataset(df, item)
        rowsToWrite = getRowsFromDataset(df)
        namesToReplace = getNamesPerId(df)
        newnames = replaceNamesInCsv(rowsToWrite, namesToReplace)
        writeList(newnames)

        end_time = time.time() - start_time
        print("Dataset loaded in ", end_time, " seconds")
        times.append([item, end_time])

    print("Loading operation has finished")
    initializeWriter('LoadingTimes' + str(times[0][0]) + "-" + str(times[len(times) - 1][0]),
                     '../output/benchmarks/')
    writeList(times)

def graphCreationBenchmark(sizeLists, algorithmName):
    times = []

    for item in sizeLists:
        start_time = time.time()
        print("Starting Graph Creation for ", item, " rows...")
        if algorithmName == "GN":
            gutils.plotGraphGN("../output/numbers/" + str(item) + "Test.csv")

        end_time = time.time() - start_time
        print("Graph Creation ended in ", end_time, " seconds")
        times.append([item, end_time])

    print("Graphs creation has finished")
    initializeWriter('GraphGenerationTimes' + str(times[0][0]) + "-" + str(times[len(times) - 1][0]),
                     '../output/benchmarks/')
    writeList(times)

def benchmarkLoadDirectedGraph(filename):
    start_time = time.time()
    loadDirectedGraph(filename)
    end_time = time.time() - start_time
    return end_time

def benchmarkLoadUndirectedGraph(filename):
    start_time = time.time()
    loadUndirectedGraph(filename)
    end_time = time.time() - start_time
    return end_time

def benchmarkPlotGraphGN(G, item, algName):
    start_time = time.time()
    plotGraphGN(G, item, algName)
    end_time = time.time() - start_time
    return end_time

def benchmarkPlotGraphKLB(G, item, algName):
    start_time = time.time()
    plotGraphKLB(G, item, algName)
    end_time = time.time() - start_time
    return end_time

def benchmarkPlotGraphLC(G, item, algName):
    start_time = time.time()
    plotGraphLC(G, item, algName)
    end_time = time.time() - start_time
    return end_time

def benchmarkPlotGraphAF(G, k, item, algName):
    start_time = time.time()
    plotGraphAF(G, k, item, algName)
    end_time = time.time() - start_time
    return end_time

def benchmarkPlotGraphGMC(G, item, algName):
    start_time = time.time()
    plotGraphGMC(G, item, algName)
    end_time = time.time() - start_time
    return end_time

def benchmarkPlotGraphNGMC(G, item, algName):
    print("asd")
    start_time = time.time()
    plotGraphNGMC(G, item, algName)
    end_time = time.time() - start_time
    return end_time
