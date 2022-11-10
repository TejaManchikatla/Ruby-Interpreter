def token(a):
    #This is a token generator function.
    #Below are all the keyword in ruby language
    keywords=["print","puts","new","break","begin","end","gets","strip","if","else","unless","for","in","while","class","def","define","do","nil",
              "not","return","self","super","then","true","until","yield","case"]
    #these are the methods which may be used.
    methods=["sort","to_i","to_s","map"]
    #operator symbols
    operators=["+","-","/","%","<",">","*",".","!",":","&","(",")","{","}","[","]","-","?","#","="]
    #different types of brackets
    brackets=["(",")","{","}","[","]"]
    #different types of seperators
    seprator=[",","#",";"]
    #create token
    tokens=[]
    #if nothing is in the string return error
    if a[0]=='':
        return "errorrrr"
    for j in a:
        #a counter j which will iterate through the string and find the respective tokens
        if j in keywords:
            tokens.append(j)

        elif j in methods:
            tokens.append(j)

        elif j in operators:
            tokens.append(j)

        elif j in seprator:
            tokens.append(j)
        #if in not akeyword then it must be a number,alphabet,etc...
        else:
            n=len(j) #find length of string
            s=j 
            i=0

            while i<n:
                variable='' #temp variable

                if s[i].isalpha() or s[i].isdigit() or s[i]=="_" or s[i]=="'" or s[i]=='"':

                    while s[i].isalpha() or s[i].isdigit() or s[i]=="_" or s[i]=="'" or s[i]=='"':
                        variable+=s[i]
                        i+=1                      

                        if i==n:
                            break

                    if variable in keywords:         
                        #print(variable,"->keywords")
                        tokens.append(variable)
                        continue

                    elif variable in methods:
                        #print(variable,"->methods")
                        tokens.append(variable)
                        continue

                    else:
                        #print(variable,"->identifiers")
                        tokens.append(variable)
                        continue

                elif s[i] in operators:
                    oper=''

                    if s[i] in brackets:
                        #print(s[i],"->operator")
                        tokens.append(s[i])
                        i+=1
                        continue

                    while s[i] in operators:

                        if s[i] in brackets:
                            tokens.append(oper)
                            tokens.append(s[i])
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
                    continue

                elif s[i] in seprator:
                    #print(s[i],"->seprator")
                    tokens.append(s[i])
                    i+=1
                    continue

                else:
                    print("error")
                    return "error"
    return tokens
#test case
print(token("a+b")) 

    
    
