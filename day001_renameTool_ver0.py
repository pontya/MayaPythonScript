import maya.cmds

def renameTool(rename_str):
    
    list_A = cmds.ls(sl=True)
    now_str_list = []
    #現在選択中のオブジェクトをリストに突っ込む
    for i in list_A:
        now_str_list.append(str(i))
    print(now_str_list)
    
    for i in list_A:
        cmds.rename(i,rename_str)
    
    list_A = cmds.ls(sl=True)
    now_str_list = []


    print('now_str_A')