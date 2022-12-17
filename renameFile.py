import os
import re
xlsbpath=r"D:\up\cmd_rename"

os.chdir(xlsbpath)

filelist = os.listdir(xlsbpath)
for f in filelist:
    #print(re.search("Bmp",f,re.IGNORECASE))
    if (re.search("Bmp",f,re.IGNORECASE)):
        os.rename(f,f.split("-")[0]+".bmp")
        
