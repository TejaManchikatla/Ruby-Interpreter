
from boolean import booleanExpression
from Lexer import token

def while_condition(tokens, i):

    boolean_expr = booleanExpression(tokens, i)
    boolean_result = boolean_expr.evaluate()

    array_of_tokens = []
    if(boolean_result):
        teja=1
        teja = input('> ')
        tokens = token(teja)
        while('END' not in tokens):
            array_of_tokens.append(tokens)
            teja = input('> ')
            tokens = token(teja)
            


    return array_of_tokens
