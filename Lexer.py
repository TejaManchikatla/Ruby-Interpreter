#This is a token generator function aka lexer, scanner, tokenizer...


def token(a):
    #Below are all the keyword in ruby language
    keywords=["print","puts","new","require","break","begin","end","alias","gets","strip","if","else","unless","for","in","while","class","def","define","do","nil",
              "not","rescue","retry","return","self","super","then","do","true","unless","until","yield","case","class","def"]
    #these are the methods which may be used.
    methods=["sort","to_i","to_s","map"]
    #operator symbols
    operators=["+","-","/","%","<",">","*",".","!",":","&","(",")","{","}","[","]","-","?","#","="]
    #different types of brackets
    op=["(",")","{","}","[","]"]
    #different types of seperators
    seprator=[",","#",";"]
    #split the line by whitespaces
    a = a.split(" ")
    #list of tokens
    tokens=[]
    if a[0]=='':
        return "errorrrr"
    for j in a:
        if j in keywords:
            #print(j,"->keyword")
            tokens.append(j)
            tokens.append("keywords")

        elif j in methods:
            #print(j,"->methods")
            tokens.append(j)
            tokens.append("methods")

        elif j in operators:
            #print(j,"->operators")
            tokens.append(j)
            tokens.append("operator")

        elif j in seprator:
            #print(j,"seprator")
            tokens.append(j)
            tokens.append("seperator")

        else:
            n=len(j)
            s=j
            i=0

            while i<n:
                variable=''

                if s[i].isalpha() or s[i].isdigit() or s[i]=="_" or s[i]=="'" or s[i]=='"':

                    while s[i].isalpha() or s[i].isdigit() or s[i]=="_" or s[i]=="'" or s[i]=='"':
                        variable+=s[i]
                        i=i+1
                        

                        if i==n:
                            break

                    if variable in keywords:         
                        #print(variable,"->keywords")
                        tokens.append(variable)
                        tokens.append("Identifier")
                        continue

                    elif variable in methods:
                        #print(variable,"->methods")
                        tokens.append(variable)
                        tokens.append("Identifier")
                        continue

                    else:
                        #print(variable,"->identifiers")
                        tokens.append(variable)
                        tokens.append("Identifier")
                        continue

                elif s[i] in operators:
                    oper=''

                    if s[i] in op:
                        #print(s[i],"->operator")
                        tokens.append(s[i])
                        tokens.append("operator")
                        i+=1
                        continue

                    while s[i] in operators:

                        if s[i] in op:
                            tokens.append(oper)
                            tokens.append(s[i])
                            tokens.append("operator")
                            oper=''
                            i+=1
                            continue
                        oper+=s[i]
                        i+=1

                        if i==n:
                            break
                    #print(oper,"->operator")
                    if len(oper)>0:
                        tokens.append(oper)
                        tokens.append("operator")
                    continue

                elif s[i] in seprator:
                    #print(s[i],"->seprator")
                    tokens.append(s[i])
                    tokens.append("seprator")
                    i+=1
                    continue

                else:
                    print("error")
                    return "error"
                    break
    return tokens
#testing
print(token("puts ab+c/d+v"))
