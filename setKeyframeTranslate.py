"""
当スクリプトで問題が発生しても責任は取れません。
自己責任でお使いください。
"""

import maya.cmds as cmds
cmds.setKeyframe(attribute = 'translate')
#現在の時間を取得
i = cmds.currentTime(query　=　True)
cmds.currentTime(i　+　1)