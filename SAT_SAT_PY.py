def finish_him(formula):
    
    variables = []
    for letter in formula:
        if (letter!="+") and (letter!=".") and (((letter.upper(), letter.lower())) not in variables):
                variables.append((letter.upper(), letter.lower()))
            
    packing = {}
    formula=formula.split(".")
    contagemv = {}
    for x, y in variables:
        contagemv[x]=0
        contagemv[y]=0
    only = contagemv.copy()  
    check = contagemv.copy()  

    veracidade = {}        
    for k in formula:
        veracidade[k]=False

    for clause in formula: 
        for x, y in variables:
            if (x in clause and y in clause) and (x not in packing.keys() and y not in packing.keys()):  
                packing[x]=True   
                packing[y]=False
                continue


            elif (x in clause and y not in clause) and (x not in packing.keys() and y not in packing.keys()):
                packing[x]=True
                packing[y]=False
                only[x]+=1
                if (len(clause)==1) or (len([k for k in clause if k!=x and k!="+"])==0):
                    check[x]+=1
                continue

            elif (x in clause and y not in clause) and (x in packing.keys() and y in packing.keys()):           
                if (only[x]==0 and only[y]==0 and packing[x]==False) or (len(clause)==1) or (len([k for k in clause if k!=x and k!="+"])==0):
                    packing[x]=True
                    packing[y]=False

                elif ((only[x]>0 or only[y]>0) and packing[x]==False):
                    if check[x]==0 and check[y]==0:
                        packing[x]=True
                        packing[y]=False
                        for close in formula:
                            if veracidade[close]==True:                                
                                packing[x]=False
                                packing[y]=True
                continue


            elif (x not in clause and y in clause) and (x not in packing.keys() and y not in packing.keys()):   
                packing[y]=True
                packing[x]=False
                only[y]+=1
                if (len(clause)==1) or (len([k for k in clause if k!=y and k!="+"])==0):
                    check[y]+=1
                continue

            elif (x not in clause and y in clause) and (x in packing.keys() and y in packing.keys()):         
                if (only[x]==0 and only[y]==0 and packing[y]==False) or (len(clause)==1) or (len([k for k in clause if k!=y and k!="+"])==0):
                    packing[y]=True
                    packing[x]=False
                    
                elif ((only[x]>0 or only[y]>0) and packing[y]==False):                     
                    if check[x]==0 and check[y]==0:
                        packing[y]=True
                        packing[x]=False
                       
                        for close in formula:
                            if veracidade[close]==True:
                                packing[y]=False
                                packing[x]=True
                continue
        
        conjunto = packing.copy()

        for x, y in variables:              
            if x not in conjunto.keys():
                conjunto[x]=False
            if y not in conjunto.keys():
                conjunto[y]=False

        final = "("
        for test in clause:
            if test == "+":
                final+=" or "
            else:
                final+=str(conjunto[test])
        final+=")"

        if eval(final)==True:             
            veracidade[clause]=True

    conjunto = packing.copy()

    for see in formula:

        for x, y in variables:              
            if x not in conjunto.keys():
                conjunto[x]=False
            if y not in conjunto.keys():
                conjunto[y]=False

        final = "("
        for test in see:
            if test == "+":
                final+=" or "
            else:
                final+=str(conjunto[test])
        final+=")"

        veracidade[see]= eval(final)

    for clause in formula: 
        for x, y in variables:
            if (x in clause and y not in clause) and (veracidade[clause]==False) and check[y]==0:   
                packing[x]=True
                packing[y]=False
                if (len(clause)>1) and (len([k for k in clause if k!=x and k!="+"])>0):
                    for close in formula:
                        if (testef(close, variables, packing.copy())==False) and veracidade[close]==True:
                            packing[x]=False
                            packing[y]=True                           
                continue
     
            elif (x not in clause and y in clause) and (veracidade[clause]==False) and check[x]==0:   
                packing[y]=True
                packing[x]=False
                if (len(clause)>1) and (len([k for k in clause if k!=y and k!="+"])>0):
                    for close in formula:
                        if (testef(close, variables, packing.copy())==False) and veracidade[close]==True:
                            packing[y]=False
                            packing[x]=True
                continue


    conjunto = packing.copy()

    for x, y in variables:              
        if x not in conjunto.keys():
            conjunto[x]=False
        if y not in conjunto.keys():
            conjunto[y]=False
    
    conjunto = dict(sorted(conjunto.items()))

    formula= ".".join(formula)
    final = "("
    for test in formula:
        if test == "+":
            final+=" or "
        elif test == ".":
            final+=")"
            final+=" and "
            final+="("
        else:
            final+=str(conjunto[test])
    final+=")"

    tirar = []
    for limpar in conjunto.keys():      
        if limpar.islower():
            tirar.append(limpar)
    
    for remove in tirar:
        conjunto.pop(remove)

    if eval(final)==True:
        return f"+ Satisfiable -> {conjunto}"

    elif eval(final)==False:
        return "- Unsatisfiable"
    

def testef(close, variables, conjunto):

    for x, y in variables:              
        if x not in conjunto.keys():
            conjunto[x]=False
        if y not in conjunto.keys():
            conjunto[y]=False
    
    final = "("
    for test in close:
        if test == "+":
            final+=" or "
        else:
            final+=str(conjunto[test])
    final+=")"

    return eval(final)      
