#constructor 
class employee: 
    lang="Python" 
    sal=120000
    def __init__(self,name,sal,lang):#"__init__" is called dandor method which print and execute without calling
        self.name=name
        self.sal=sal
        self.lang=lang
        print(name, sal, lang)
        print("called itself")
    def getInfo(self):
        print(f"the {self.lang} has {self.sal} salary. ")
    @staticmethod 
    def greet(): 
        print("Good morning!")

toya=employee("Toya", 1450000, "Javascript") #argument of object can be accessed by "__init__"method in class directly
toya.getInfo()
toya.greet()