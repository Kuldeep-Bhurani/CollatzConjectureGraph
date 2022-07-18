import imp
import algorithm
import graph

if __name__ == "__main__":
    n = int(input("enter your no: "))
    result = algorithm.Algo(n)
    graph.Plot(result, n)
    # graph.Plot(result, algorithm.Algo(100), algorithm.Algo(4541))
