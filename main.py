

import pandas as pd


PPIs = pd.read_table('./data/PPIs.txt', delim_whitespace=True)
ModuleGene = pd.read_table('./data/Module_Gene.txt', delim_whitespace=True)
Exp = pd.read_table('./data/DEG_EXP.txt', delim_whitespace=True)

ModuleTypeLen = len(set(ModuleGene['Module']))



for i in range(1, ModuleTypeLen, 1):
    SubNetwork = ModuleGene[ModuleGene['Module'] == i]

    MergeNetwork1 = pd.merge(PPIs, SubNetwork, left_on='Gene_1', right_on='Symbol')
    MergeNetwork2 = pd.merge(PPIs, SubNetwork, left_on='Gene_2', right_on='Symbol')
    MergeNetwork = MergeNetwork1.append(MergeNetwork2)
    print (MergeNetwork)
    break



print (Exp.iloc[:,range(51)])

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

