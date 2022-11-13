from Variable_assignment import assignVariable
from Puts_ruby import puts
from Lexer import token 
from If_condition import if_condition
from While_condition import while_condition
from boolean import booleanExpression

def parse(tokens, i):


    if(tokens[i]=='PUTS'):
        i+=1
        return puts(tokens, i)
    
    elif(tokens[i]=='VARIABLE'):
        i+=1
        return assignVariable(tokens, i)
    
    elif(tokens[i]=='IF'):
        i+=1
        true_or_false = if_condition(tokens, i)
        if true_or_false:
            teja = input('> ')
            tokens = token(teja)
            while('END' not in tokens):
                parse(tokens, 1)
                teja = input('> ')
                tokens = token(teja)
                if('ELSE' in tokens):
                    while('END' not in tokens):
                        teja = input('> ')
                        tokens = token(teja)
        else:
            teja = input('> ')
            tokens = token(teja)

            while('END' not in tokens):
                teja = input('> ')
                tokens = token(teja)
                if('ELSE' in tokens):
                    while('END' not in tokens):
                        parse(tokens, 1)
                        teja = input('> ')
                        tokens = token(teja)
    
    elif(tokens[i]=='WHILE'):
        i+=1

        boolean_tokens = tokens
        boolean_expr = booleanExpression(boolean_tokens, i)
        boolean_result = boolean_expr.evaluate()

        array_of_tokens = [tokens]
        if(boolean_result):
            teja=1
            teja = input('> ')
            tokens1 = token(teja)
            while('END' not in tokens1):
                array_of_tokens.append(tokens1)
                teja = input('> ')
                tokens1 = token(teja)
            while(boolean_result):
                for j in range(1, len(array_of_tokens)):
                    parse(array_of_tokens[j], 1)
                boolean_expr = booleanExpression(array_of_tokens[0], i)
                boolean_result = boolean_expr.evaluate()
        else:
            while('END' not in tokens):
                teja = input('> ')
                tokens = token(teja)

    elif(tokens[i]=='')

        



    




teja=1
while(teja!='close'):
    teja = input('> ')
    tokens = token(teja)
    parse(tokens, 1)
