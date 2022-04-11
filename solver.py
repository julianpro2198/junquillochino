def solve(lagod,junquillo):

    solutions = []

    for x in range(len(lagod)):
        partA = (0.25*(pow(lagod[x],2)))/(0.02*junquillo[x])
        partB = (0.0001*junquillo[x])/(0.02)
        
        solutions.append(round(partA-partB,1))
    
    return solutions
