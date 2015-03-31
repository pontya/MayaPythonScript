import maya.cmds as cmds
cmds.setKeyframe(attribute = 'translate')
#現在の時間を取得
i = cmds.currentTime(query=True)
cmds.currentTime(i+1)