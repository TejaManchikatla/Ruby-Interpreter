def token(a):
    keywords=["print","puts","new","require","break","begin","end","alias","gets","strip","if","else","unless","for","in","while","class","def","define","do","nil",
              "not","rescue","retry","return","self","super","then","do","true","unless","until","yield","case","class","def"]
    operators=["+","-","/","%","<",">","*"]
    
    tokens=[]
    if(a[0]==''):
        return "error"
    for j in a :
        if(j in keywords):
            tokens.append(j)
        elif j in operators:
            tokens.append(j)
        else:
            n=len(j)
            s=j
            i=0;
            while i<n :
                variable=''
                if s[i].isalpha() or s[i].isdigit() or s[i]=="_" or s[i]=="'" or s[i]=='"':
                    while s[i].isalpha() or s[i].isdigit() or s[i]=="_" or s[i]=="'" or s[i]=='"':
                        variable += s[i]
                        i=i+1
                        if(i==n):
                            break
                        
        