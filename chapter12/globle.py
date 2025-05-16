# globle and local variable
num=55 # globle var declaration
def fun():
    # global num #used fetch globle value of variable
    num=45 # local var declaration
    print(num)
fun() # call a local var
print(num) # call globle var