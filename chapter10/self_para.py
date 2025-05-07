class employee: 
    lang="Python" 
    sal=120000
    def getInfo(self):
        print(f"the {self.lang} has {self.sal} salary. ")
    @staticmethod # This states that given method dont need any object reference like "self"
    def greet(): 
        print("Good morning!")

toya=employee() # "toya" object created  of above class which initiate the memory  allocation 
toya.getInfo()
toya.greet()