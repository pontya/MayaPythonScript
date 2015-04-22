import maya.cmds as cmds
import maya.mel as mel
import re

object = cmds.ls(sl=True)
print(object)

mel.eval('string $selecJoint = "%s";' % object)
mel.eval('artSkinInflListChanging $selecJoint 1;')
mel.eval('artSkinInflListChanged artAttrSkinPaintCtx;')

node = cmds.listHistory(object,f=True)
list_A = []

for searchWord in node:
	text = str(searchWord)
	pattern = re.compile(r'Shape')
	matchObj = pattern.search(text)
	if matchObj == None:
		print("目印たぬ")
	else:
		list_A.append(text)
if len(list_A) > 0:
    for list_loop in list_A:
        print(list_loop)
        cmds.select(list_loop,add=True)










