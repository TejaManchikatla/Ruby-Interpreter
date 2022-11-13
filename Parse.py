from Variable_assignment import assignVariable
from Puts_ruby import puts
from Lexer import token 

def parse(object):

    tokens = token(object)
    i = 1
    if(tokens[i]=='PUTS'):
        i+=1
        return puts(tokens, i)
    elif(tokens[i]=='VARIABLE'):
        i+=1
        return assignVariable(tokens, i)



    return

teja=1
while(teja!='close'):
    teja = input('> ')
    parse(teja)
