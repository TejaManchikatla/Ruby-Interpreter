
from RUBY import *
from Error import bad_shit
from Memory import *



def assignVariable(tokens, i):


    if(tokens[i]=='='):
        k = i
        if(tokens[i+2]=='"'):
            i+=4
            expr = ''
            while(tokens[i]!='"'):
                expr+=tokens[i]
                i+=2
            if(tokens[i]=='"'):
                store(tokens[k-2], expr)
                #print(expr)
            else:
                print(bad_shit)
        else:
            expr = ''
            while(i+2 < len(tokens)):
                if(tokens[i+3]=='VARIABLE'):
                    expr+=str(mem_val[mem_var.index(tokens[i+2])])
                else:
                    expr+=tokens[i+2]
                i+=2
            #print(expr)
            lexer = Lexer(expr)
            interpreter = Interpreter(lexer)
            result = interpreter.expr()
            #print(result)
            store(tokens[k-2], result)
    else:
        print(bad_shit)




