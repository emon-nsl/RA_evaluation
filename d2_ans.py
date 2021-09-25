import os

def visit_directory(path):
    file_list = []
    folder_list = []
    try:
        folder_list = os.listdir(str(path))
    except:
        pass
    
    for i in folder_list:
        file_list.append(i)
        file = visit_directory(path+'/'+i)
        for j in file:
            file_list.append(j)
        

    return file_list
x = visit_directory('test_dir/')
print(x)
    

