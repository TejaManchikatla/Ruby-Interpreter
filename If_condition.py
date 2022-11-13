
from boolean import booleanExpression
from Lexer import token

def if_condition(tokens, i):

    boolean_expr = booleanExpression(tokens, i)
    boolean_result = boolean_expr.evaluate()
    return boolean_result

