#program to print third, fifth and seventh item of list using enumerate
lst=[1,"ram",45,10, "shyam1", 79,"Toya"]
for i, item in enumerate(lst):
    if i==1 or i==4 or i==6:
        print(item)