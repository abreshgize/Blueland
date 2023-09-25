import os
from os import listdir, name, path
from os.path import isfile, join
from re import L
if __name__ == '__main__':
    path = "D://Download//Images//Product"
    path2 = "D://Download//Product"
    i = 0

    
    for f in os.listdir(path):
        f1 = os.path.join(path2, f)
        if  os.path.isfile(f1):
            i+=1
    print(i)
        # if os.path.exists (os.path.join(path2, "UNI_Collar.jpg")):
        #     print(f.)
        #     i+=1
        
    # print(i)