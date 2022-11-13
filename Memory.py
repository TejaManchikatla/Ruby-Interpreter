
mem_var = []
mem_val = []
def store(var, val):

    if(var in mem_var):
        ind = mem_var.index(var)
        mem_val[ind] = val
    else: 
        mem_var.append(var)
        mem_val.append(val)

    print(mem_var)
    print(mem_val)


