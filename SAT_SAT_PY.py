import time
inicio = time.time()
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
    
print(finish_him("a+b+A.A"))                                                                                   
print(finish_him("A+a"))                                                                                       
print(finish_him("A+d.e+a.F.A"))                                                                               
print(finish_him("A+A+A.d+a+E"))                                                                               
print(finish_him("c+E+a.A+f"))                                                                                 
print(finish_him("A+b+a.A+a.A+d.e+a.F.A+A+A.d+a+E"))                                                           
print(finish_him("A.d+e+a.D"))                                                                                  
print(finish_him("A+b+C.A.a+B.C"))                                                                                
print(finish_him("A+B.A+b.a+B"))                                                                               
print(finish_him("A+B+C.A+b+C.A+B+c.A+b+c.a+B+C.a+b+c"))                                                        
print(finish_him("b+C+d.a+C+E.b+C+e.b+D+E.a+D+e.b+D+E.B+C+d.a+c+D.a+C+E.a+b+D.a+C+e.A+b+C"))                      
print(finish_him("A+a+b.C+B+D.a+c+d"))                                                                         
print(finish_him("A+B+C.B+c+f.b+E"))                                                                           
print(finish_him("A+b+c.a+c+D.a+b+D"))                                                                         
print(finish_him("A+b.a+c.a"))                                                                                 
print(finish_him("A+B+C.a+b.A+c.C+b.a+b+c"))                                                                     
print(finish_him("d.e+D.E+A"))                                                                                   
print(finish_him("A+B.a+c.b"))                                                                                 
print(finish_him("A+B.a+c.b+b"))                                                                               
print(finish_him("A+B.a+c.D+E.d+f.e.b"))                                                                       
print(finish_him("d.A+B.e+D.b.a+c"))                                                                             
print(finish_him("D+A+c.f+D+a.c.d"))                                                                           
print(finish_him("a+B+C.A+b+C.A+B+C.a+b+c"))                                                                   
print(finish_him("A+a+b.C+B+D.a+c+D"))                                                                         
print(finish_him("c.B+C+A.a+c.b.A"))                                                                           
print(finish_him("B+c+d.B+C+d.a+B+D.a+b+C.A+b+d"))                                                             
print(finish_him("A+B.b+C+d.a+D"))                                                                             
print(finish_him("A+b.A+C.a+B"))                                                                               
print(finish_him("a+B+C.A+b+C.A+B+D.a+c+d"))                                                                   
print(finish_him("A+A+B.a+b+b.a+B+B"))                                                                         
print(finish_him("A+b.a+B+C.a"))                                                                               
print(finish_him("A+b+c.a+B+C.a"))                                                                             
print(finish_him("a+b+B+D.d+A+B+c.c+D+b+A"))                                                                    
print(finish_him("a+b+B+D.d+A+B+c.c+D+b+A"))                                                                

print("---------------------------------------------------------------------------------------------------")

print(finish_him("A.a"))                                                                                       
print(finish_him("A+B.a+c.a.b"))                                                                               
print(finish_him("A+b+a.a.A"))                                                                                 
print(finish_him("A+b+a.A+a.A+d.e+a.F.a.A+A+A.d+a+E"))                                                         
print(finish_him("A+B.A+b.a+C.a+c"))                                                                           
print(finish_him("A+B+C.A+B+c.A+b+C.A+b+c.a+B+C.a+B+c.a+b+C.a+b+c"))                                           
print(finish_him("b+C+d.a+C+E.b+C+e.b+D+E.a+D+e.b+D+E.B+C+d.a+c+D.a+C+E.a+b+D.a+C+e.A+b+C.A.a"))   
print(finish_him("A+B+C+D+E+F+G+H.a.b.c.d.e.f.g.h"))             
 

fim = time.time()
print(fim-inicio)