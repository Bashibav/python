#program to write multiplication table  of 2 to 20 in diffrent file in folder
def gen_table(n):
    table=""
    for i in range (1,11):
        table +=f"{n} x {i} = {n*i}\n"
    with open(f"tables/table_{n}.txt","w") as f:
        f.write(table)
for i in range(2,21):
    gen_table(i)