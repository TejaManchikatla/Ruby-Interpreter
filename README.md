# Ruby-Interpreter
Designing a basic interpreter for RUBY in PYTHON

## Breif Description
This Ruby interpreter takes one line at a time as input from the user and interpretes it and produes the output if required. And then waits for next line of input to be entered. Next line is the continuation of the first line and so on.
It has three main files Lexer, Parser, Interpreter.

[*Lexer*](#lexer) - It takes the given Line as String and returns the tokens present in it. It has predefined Token types, Reserved keywords. It has two classes 'Token' and 'Lexer'.

[*Parser*](#parser) - It gets the tokens of the given line from [Lexer](#lexer) and makes an Abstract syntax tree based on it.

[*Interpreter*](#interpreter) - It gets the abstract syntax tree from [Parser](#parser) and interprets the tree based on the semantics of the Ruby.

### Subset of the BNF used:

PROGRAM : COMPSTMT

T : ";" | "\n"

COMPSTMT : STMT {T EXPR} \[T]
 
statement_list : statement| statement SEMI statement_list

statement : compound_statement
                | assignment_statement
                | empty

factor : INTEGER | LPAREN expr RPAREN | variable|string

term : factor ((MUL | DIV) factor)*

expr   : term ((PLUS | MINUS) term)*
 
boolean_expr : REL_OP expr expr

"" comment - Here in the below BNF we are enforing that "Then" and "DO" should be present.""

if stat : IF bool_expr THEN comp_stmt {ELSIF bool_expr THEN comp_stmt}ELSE comp_stmt END  

puts stat : PUTS expr

unless stat : UNLESS bool_expr THEN comp_stmt END

while stat : WHILE bool_expr DO comp_stmt END

until stat : UNTIL bool_expr DO comp_stmt END

assignment_statement : variable ASSIGN_OP expr

# Lexer
The predefined token types present in Lexer file are INTEGER, PLUS, MINUS, MUL, DIV, LPAREN, RPAREN, EOF,ID, ASSIGN_OP, SEMI,STRING, EQUALS, LESSTHAN, GREATERTHAN, NOTEQUALS, LESSTHANEQUALS, GREATERTHANEQUALS. The Reseved Keywords present are  'end', 'if', 'else', 'elsif', 'then', 'while', 'unless', 'do', 'puts', 'until'.

It has a 'Token' class to define the tokens used. And a 'Lexer' class to check and return the token types present in the given string. It has the following functions defined in it.

### *error*  
It raises an exception called "Invalid Character" whenever the function is called.

### *peek*  
It returns what character is present next to the pointer but doesn't change the pointers location.

### *_id*  
It checks if the word given is in Reserved keywords and returns it. If it is not present then it is returned as 'ID' Token. 

### *advance* 
It forwards the pointer. If it reaches the end of the input then current character is 'None', else it is the character at the pointer.

### *skip_whitespace*  
It skips the whitespace character if the pointer points at whitespaces.

### *integer* 
It returns the integer value if the pointer points at any multidigit integer.

### *string*  
It returns all the characters until ' " ' is encountered and skips the character ' " '.

### *get_next_token*  
It is Lexical analyser. If the pointer is at whitespace, it skips that character by calling [*skip_whitespace*](#skip_whitespace) and continues to run rest of the code. If the pointer is at alphabet, it calls [*_id*](#_id) functions and returns the corresponding token. If the pointer is at interger, it calls [*integer*](#integer) and returns corresponding integer. If the pointer is at one of the predefined tokentypes then it returns those corresponding token objects. If the pointer is not present in any one of the above then it calls [*error*](#error) and the program stops. When end of the input, that is, 'None' is encountered then it returns 'EOF' Token.
