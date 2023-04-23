def finish_him(formula):

    variables = []
    for letter in formula:
        if (letter!="+") and (letter!=".") and (((letter.upper(), letter.lower())) not in variables):
                variables.append((letter.upper(), letter.lower()))
            
    check = {}
    for x, y in variables:
        check[x]=0
        check[y]=0

    veracidade = {} 
    formula=formula.split(".")       
    for k in formula:
        veracidade[k]=False

    packing = {}
    for clause in formula: 
        for x, y in variables:
            if (x in clause and y in clause) and (x not in packing.keys() and y not in packing.keys()): 
                packing[x]=True   
                packing[y]=False
                continue

            elif (x in clause and y not in clause) and (x not in packing.keys() and y not in packing.keys()):  
                packing[x]=True
                packing[y]=False

                if (len(clause)==1) or (len([k for k in clause if k!=x and k!="+"])==0):
                    check[x]+=1
                continue

            elif (x not in clause and y in clause) and (x not in packing.keys() and y not in packing.keys()):   
                packing[y]=True
                packing[x]=False

                if (len(clause)==1) or (len([k for k in clause if k!=y and k!="+"])==0):
                    check[y]+=1
                continue

    for see in formula:
        final = "("
        for test in see:
            if test == "+":
                final+=" or "
            else:
                final+=str(packing[test])
        final+=")"

        veracidade[see] = eval(final)

    for clause in formula: 
        for x, y in variables:
            if (x in clause and y not in clause) and (veracidade[clause]==False) and check[y]==0:
                packing[x]=True
                packing[y]=False
                conjunto = packing.copy()
                for close in formula:
                    if veracidade[close]==True:                    
                        final = "("
                        for test in close:
                            if test == "+":
                                final+=" or "
                            else:
                                final+=str(conjunto[test])
                        final+=")"

                        if (eval(final)==False):
                            packing[x]=False
                            packing[y]=True                           
                continue

            elif (x not in clause and y in clause) and (veracidade[clause]==False) and check[x]==0:   
                packing[y]=True
                packing[x]=False
                conjunto = packing.copy()
                for close in formula:
                    if veracidade[close]==True: 
                        final = "("
                        for test in close:
                            if test == "+":
                                final+=" or "
                            else:
                                final+=str(conjunto[test])
                        final+=")" 

                        if (eval(final)==False) and veracidade[close]==True:
                            packing[y]=False
                            packing[x]=True
            continue

    packing = dict(sorted(packing.items()))

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
            final+=str(packing[test])
    final+=")"

    tirar = []
    for limpar in packing.keys():      
        if limpar.islower():
            tirar.append(limpar)
    
    for remove in tirar:
        packing.pop(remove)

    if eval(final)==True:
        return f"+ Satisfiable -> {packing}"

    else:
        return "- Unsatisfiable"  
