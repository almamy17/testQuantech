from os import listdir,rename
from os.path import isfile, join
files=listdir("folder")
for file in files:
    i=1
    if isfile(join("folder", file)):
        rename(file, 'super_fichier_'+str(i))
        i+=1