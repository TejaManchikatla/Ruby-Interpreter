# Ruby-Interpreter
Designing a basic interpreter for RUBY in PYTHON

## Breif Description
This Ruby interpreter takes one line at a time as input from the user and interpretes it and produes the output if required. And then waits for next line of input to be entered. Next line is the continuation of the first line and so on.
It has three main files Lexer, Parser, Interpreter.

[*Lexer*](#lexer) - It takes the given Line as String and returns the tokens present in it. It has predefined Token types, Reserved keywords. It has two classes 'Token' and 'Lexer'.

[*Parser*](#parser) - It gets the tokens of the given line from [Lexer](#lexer) and makes an Abstract syntax tree based on it.

[*Interpreter*](#interpreter) - It gets the abstract syntax tree from Parser and interprets the tree based on the semantics of the Ruby.

### Subset of the BNF used:
PROGRAM : COMPSTMT

T : ";" | "\n"

COMPSTMT : STMT {T EXPR} [T]
 
statement_list : statement| statement SEMI statement_list

statement : compound_statement
                | assignment_statement
                | empty

factor : INTEGER | LPAREN expr RPAREN | variable|string

term : factor ((MUL | DIV) factor)*

expr   : term ((PLUS | MINUS) term)*
 
boolean_expr : REL_OP expr expr

if stat : IF bool_expr THEN comp_stmt {ELSIF bool_expr THEN comp_stmt}ELSE comp_stmt END 
""comment - Here we are enforing that "Then" should be after 'bool_expr'"" 

puts stat : PUTS expr
