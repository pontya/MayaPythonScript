import maya.cmds as cmds

sp = cmds.ls(sl=True)
pos = cmds.filterExpand(sp, sm=31)

list_Vertex = []

#頂点の数だけ繰り返す
for loop in pos:
    #選択した頂点をリストで取得
    vList = cmds.pointPosition(loop,world=True)
    for i in range(len(vList)):
        #取得したリストを四捨五入していくい
        vList[i] = round(vList[i],3)
    print(str(loop) + str(vList))
    list_Vertex.append(vList)
    
print list_Vertex

#xVertex[i][0]→頂点xのみを抽出
#yVertex[i][1]→頂点yのみを抽出
#zVertex[i][2]→頂点zのみを抽出


#Y軸のみ抽出ac
yVertex = list_Vertex
yVertex_List = []

max_Vertex = []
print(min(yVertex))

for i in range(len(yVertex)):
    yVertex_List.append(yVertex[i][1]) 

max_yVertex = max(yVertex_List)
min_yVertex = min(yVertex_List)

print(max_yVertex)
print(min_yVertex)

max_Vertex_list = []
XY_max_Vertex = []
#Y軸の最大値のリストを取得
for i in range(len(yVertex)):
    if max_yVertex == yVertex[i][1]:
        max_Vertex = yVertex[i]
        max_Vertex_list.append(max_Vertex)
        print 'y軸の最大値が含まれる座標' + str(max_Vertex)
        """
        #max_Vertexの中から頂点xが最大のものを取得
        for k in range(len(max_Vertex)):
            max_Vertex_list.append(max_Vertex[k][0])
        
        XY_max_Vertex = max(max_Vertex_list)
        print XY_max_Vertex
    	"""
    else:
        pass
 
 print max_Vertex_list
 #最大値のリストの中からx座標の値が一番大きいものを取得
 for i in range(len(max_Vertex_list)):
 	print max_Vertex_list[i][0]

        
#Y軸の最小値のリストを取得
for i in range(len(yVertex)):
    if min_yVertex == yVertex[i][1]:
        min_Vertex = yVertex[i]
        print 'y軸の最小値が含まれる座標' + str(min_Vertex)
    else:
        pass
        
#最小値と最大値を通る直線のX座標を求める
    
