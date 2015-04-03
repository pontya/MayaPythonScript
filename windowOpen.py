import pymel.core as pm 
import maya.cmds as cmds
import maya.mel as mel 

window_list = []

window = cmds.lsUI(windows=True)
print(window)
#辞書型で種類ことにフィルターしてくれる機能をつける
for loop in window:
	if loop == "scriptEditorPanel1Window" or loop == "learningMoviesLaunchWnd" or loop == "ColorEditor" or loop == "MayaWindow" or loop == "Com orWindow" or loop == "gozwin" or loop == "nexFloatWindow":
		pass
	else:
		window_list.append(loop)

print(window_list)
pm.runtime.window_list[0]()
#mel.eval(window_list[0])

#def windowButton(buttunName,)
#with pm.window(title='windowList'):
 #   with pm.autoLayout():
  #  	for i in window_list
   #     pm.button(label=i, command=pm.Callback(mel.eval()))