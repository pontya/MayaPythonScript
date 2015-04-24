import maya.cmds as cmds
import random

setObj = cmds.ls(sl=True)
for loop in setObj:
    randomSeed = random.randint(0,360)
    cmds.rotate(randomSeed,randomSeed,randomSeed,loop)