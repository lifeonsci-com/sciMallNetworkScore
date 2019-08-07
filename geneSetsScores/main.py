from gensim.models import Word2Vec
import gensim.models.keyedvectors as word2vec
from util import parse_args, read_graph
import numpy as np
import pandas as pd
from itertools import combinations, permutations


def getEnrichStatisc(R, pathWay, geneSet, p):
    s1 = 0
    s2 = 0
    s3 = 0
    Es = 0
    for l in range(p):
        for i in range(l):
            s1 += R[i] * (1 if i in pathWay else 0)

        for i in range(p):
            s2 += R[i] * (1 if i in pathWay else 0)

        for i in range(l):
            s3 += (1 if str(i) in pathWay else 0)

        s4 = p - len(pathWay)
        if Es == 0 or (s1 / s2) - (s3/s4) > Es:
            Es = (s1 / s2) - (s3/s4)
    return Es




# p is the number of gene; n is the number of sample
def generateKSScore(embPath, nodes, p, n, pathWays, geneSets):
    print(embPath)
    # model = Word2Vec()
    # wv = Word2Vec.load(embPath, binary=True)
    model = word2vec.KeyedVectors.load_word2vec_format(embPath)    # print (len(list(permutations(nodes, 2))))

    idx2node = {idx:node for idx, node in enumerate(nodes)}
    nodeLen = len(nodes)
    R = np.zeros(shape=(nodeLen, nodeLen))

    for idx, Source in enumerate(nodes):
        for TargetIdx in range(idx+1, nodeLen, 1):
            geneScore = model.similarity(str(Source), str(nodes[TargetIdx]))
            # print (geneScore)
            R[idx][TargetIdx] = geneScore
            R[TargetIdx][idx] = geneScore
            # print (Source, Target)

    R = pd.DataFrame(R)
    # print (geneScores)
    R = R.sum(axis=1)
    # print (geneScores)
    R = R.sort_values(ascending=False)

    print (R)

    for idx, value in enumerate(R):
        R[idx] = abs(p/2 - idx + 1)

    return R


# export PYTHONPATH="/Users/csx/GitProject/sciMallNetworkScore:$PYTHONPATH"
if __name__ == "__main__":
    embPath = '/Users/csx/GitProject/sciMallNetworkScore/data/emb/test.emb'
    args = parse_args()
    G = read_graph(args)
    nodes = G.nodes
    pathWays = [set([32, 34, 3])]
    R = generateKSScore(embPath, list(nodes), p = len(nodes), n = 10, pathWays = pathWays, geneSets=set(nodes))
    for pathway in pathWays:
        Es = getEnrichStatisc(R, pathway, set(nodes), p = len(nodes))
        print ('pathway: 32 34 3 scores: ', Es)
    # print (G.nodes)
    # print (G.nodes)
	# geneSetsScore()







