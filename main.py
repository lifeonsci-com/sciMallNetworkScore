
import numpy as np
import pandas as pd
from topoSortNetwork import Graph

PPIs = pd.read_table('./data/PPIs.txt', delim_whitespace=True)
ModuleGene = pd.read_table('./data/Module_Gene.txt', delim_whitespace=True)
Exp = pd.read_table('./data/DEG_EXP.txt', delim_whitespace=True, index_col=0)

ModuleTypeLen = len(set(ModuleGene['Module']))

CaseMemebers = Exp.iloc[:,range(94)]
NormalMembers = Exp.iloc[:,94:-1]

print (np.mean(NormalMembers, axis=1))

# for i in range(1, ModuleTypeLen, 1):
#
#     SubNetwork = ModuleGene[ModuleGene['Module'] == i]
#
#     MergeNetwork1 = pd.merge(PPIs, SubNetwork, left_on='Gene_1', right_on='Symbol')
#     MergeNetwork2 = pd.merge(PPIs, SubNetwork, left_on='Gene_2', right_on='Symbol')
#     MergeNetwork = MergeNetwork1.append(MergeNetwork2)
#
#     graph = Graph(MergeNetwork)
#     MergeNetwork.to_csv('./mergeNetwork.csv')
#     # print (MergeNetwork)
#     break


# Y
# CaseMemebers = Exp.iloc[:,range(51)]

# print (Exp.iloc[:,range(51)])
# N
# print
# print (np.mean(Exp, axis=1))

# print ()
# print (ModuleGene[])


# with open('./data/PPIs.txt', 'r') as fp:
#     PPIs = fp.readlines()
#     for ppi in PPIs:
#         T = ppi.split('\t')
#         print (len(T))
#         source = T[0]
#         target = T[1]
#         print (T)
        # value = int(T[2])
        # print (source, target, value)

