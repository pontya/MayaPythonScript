import maya.cmds as cmds
import math

Node1 = cmds.ls(sl=True,)
Node2 = cmds.listHistory(Node1)

revolveNode = []
nurbsCurveNode = []

print Node2
for loop in Node2:
    SerchNode = cmds.nodeType(loop)
    if(SerchNode == 'revolve'):
        revolveNode = loop
        print revolveNode
    elif(SerchNode == 'nurbsCurve'):
        nurbsCurveNode = loop
        print nurbsCurveNode
    else:
        pass

getCvCurvePosition = cmds.pointOnCurve(nurbsCurveNode,position=True)

setPivotX = str(revolveNode) + '.pivotX'
setPivotY = str(revolveNode) + '.pivotY'
setPivotZ = str(revolveNode) + '.pivotZ'
cmds.setAttr(setPivot,getCvCurvePosition[0])
cmds.setAttr(setPivot,getCvCurvePosition[1])
cmds.setAttr(setPivot,getCvCurvePosition[2])