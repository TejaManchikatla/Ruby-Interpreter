
from RUBY import *
from Error import bad_shit
from Memory import *



def puts(tokens, i):

    if(tokens[i]=='('):
        if(tokens[i+2]=='"'):
            i+=4
            expr = ''
            while(tokens[i]!='"' and i<len(tokens)):
                expr+=tokens[i]
                i+=2
            if(tokens[i]=='"'and tokens[i+2]==')'):
                print(expr)
            else:
                print(bad_shit)
        else:
            expr = ''
            while(tokens[i+2]!=')'):
                
                if(tokens[i+3]=='VARIABLE'):
                    expr+=str(mem_val[mem_var.index(tokens[i+2])])
                else:
                    expr+=tokens[i+2]
                i+=2
            print(expr)
            lexer = Lexer(expr)
            interpreter = Interpreter(lexer)
            result = interpreter.expr()
            print(result)

                   
    else:
        print(bad_shit())
 

