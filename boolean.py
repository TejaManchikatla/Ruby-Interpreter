from RUBY import *
from Memory import *

class booleanExpression:
    
    def __init__(self,tokens,i):
        self.tokens=tokens
        self.i=i
    
    def evaluate(self):
        result=True
        left=''
        op=''
        i = self.i
        tokens = self.tokens
        while i<len(tokens):
            if self.tokens[i]=='>':
                op='>'
                i+=2
                break
            elif self.tokens[i]=='>=':
                op='>='
                i+=2
                break
            elif self.tokens[i]=='==':
                op='=='
                i+=2
                break
            elif self.tokens[i]=='!=':
                op='!='
                i+=2
                break
            elif self.tokens[i]=='<=':
                op='<='
                i+=2
                break
            elif self.tokens[i]=='<':
                op='<'
                i+=2
                break
            else:
                if(tokens[i+1]=='VARIABLE'):
                    left+=str(mem_val[mem_var.index(tokens[i])])
                else:
                    left+=tokens[i]
                i+=2
        right=''
        while i<len(tokens) and tokens[i+1]!='THEN':
            if(tokens[i+1]=='VARIABLE'):
                right+=str(mem_val[mem_var.index(tokens[i])])
            else:
                right+=tokens[i]

            i+=2
            
        lexer1=Lexer(left)
        lexer2=Lexer(right)
        interpreter1= Interpreter(lexer1)
        interpreter2= Interpreter(lexer2)
        leftresult = interpreter1.expr()
        rightresult = interpreter2.expr()
        if op=='>':
            return leftresult>rightresult
        elif op=='>=':
            return leftresult>=rightresult
        elif op=='==':
            return leftresult==rightresult
        elif op=='!=':
            return leftresult!=rightresult
        elif op=='<':
            return leftresult<rightresult
        elif op=='<=':
            return leftresult<=rightresult