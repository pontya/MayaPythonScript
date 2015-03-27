import maya.cmds
window = cmds.lsUI(windows=True)
print(window)
for loop in window:
	if loop != "scriptEditorPanel1Window" and loop != "learningMoviesLaunchWnd" and loop != "ColorEditor" and loop != "MayaWindow" and loop != "CommandWindow" and loop != "gozwin" and loop != "nexFloatWindow":
		cmds.deleteUI(loop)
