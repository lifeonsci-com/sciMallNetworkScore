# coding=utf-8
import codecs
from collections import defaultdict

graphSets = set()
Graph = defaultdict(list)
OperateMap = {'->': 1, '-|': -1}

with open('./data/network/networks.txt') as fp:
    rawNetworks = fp.read()
    # print (rawNetworks)

    for pathway in rawNetworks.split('\n'):
        print (pathway)
        items = pathway.split(' ')
        # while Source < Len-1:
        for Source in range(0,len(items)-1,2):
            op = Source+1
            Target = Source+2
            path = ' '.join([items[Source], items[op], items[Target]])
            if path in graphSets:
                continue

            graphSets.add(path)


            print (items[Source], items[op], items[Target])
            Graph[items[Source]].append((items[Target], items[op]))


            # Graph[items[Source]].append((items[Target], items[op]))
        # break

# ->表示促进作用，-|表示抑制作用，//表示没有意义，边去掉
wf = codecs.open('./data/GeneNetwork.csv', 'w', encoding='utf-8')
wf.write('Source Target Label\n')
for key in Graph.keys():
    values = Graph[key]
    for value in values:
        if value[1] == '//': continue
        wf.write('{} {} {}\n'.format(key,value[0], OperateMap[value[1]]))
wf.close()

# 节点图

wf = codecs.open('./data/GeneNetworkLabel.csv', 'w', encoding='utf-8')
wf.write('Id Label\n')

for key in Graph.keys():
    wf.write('{} {}\n'.format(key, key))

wf.close()

