class employee: #Format of class
    lang="Python" #this is a class attribute
    collage="janjyoti"
    sem=5
toya=employee() # "toya" object created  of above class which initiate the memory  allocation 
toya.name="Toya" # "name" is here object attribute
print(toya.name,toya.lang,toya.collage) 
ram=employee()
ram.lang="Java" # "lang" is here instant attribute for object which do not belongs to "lang " of class
print(ram.lang,ram.collage) 