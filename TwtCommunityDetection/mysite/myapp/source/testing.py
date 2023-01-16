from mysite.myapp.source.benchmarkingTools import *

#################
#sizeLists = [1000, 2000]
#timeLoadingDataset(sizeLists)
#################
#size = 1233
#createPartialDataset(size)
#G = loadDirectedGraph("../output/numbers/1000Test.csv") # + str(size) + "Test.csv")
#time = plotGraphGN(G)
#sizes = getCommunitiesSizes(G)
#print(sizes)
#plotLoadingTimes("../output/benchmarks/LoadingTimes1000-40000.csv")
#################
#sizeLists = [1000, 2000, 4000, 6000, 8000, 10000, 20000, 40000]


'''#### Newton for 1000-8000
### Create
sizeL = [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000]
sizeLL = [10000]
#prepareFor(sizeLL)
### Get times
timeGraphCommunityGN(sizeLL)
### Sizes
'''


'''###
sizeL = [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000]
sizeLL = [5000, 10000, 20000]
sizeLLL = [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 10000, 20000]
#prepareFor(sizeLL)
### Get times
timeGraphCommunityLC(sizeL)'''


###
'''sizeL = [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000]
sizeLL = [40000]
prepareFor(sizeLL)
### Get times
timeGraphCommunityGMC(sizeLL)
'''
'''sizeL = [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000]
sizeLL = [1000, 1500]
#prepareFor(sizeL)
### Get times
timeGraphCommunityNGMC(sizeLL)'''




#####
#plotTimes("BenchmarkLC")
#
#plotTimes("BenchmarkGN")
#
#plotTimes("BenchmarkGMC")
#
#plotTimes("BenchmarkGN")
#
#plotTimeComparison()
#plotTimeComparison2()

gn = getNumberOfCommunities(6000, "GN")
print(gn)
print(len(gn))

gn = getNumberOfCommunities(6000, "LC")
print(gn)
print(len(gn))

gn = getNumberOfCommunities(6000, "GMC")
print(gn)
print(len(gn))