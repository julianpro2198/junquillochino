from pickle import FALSE, TRUE
import solver


lagod = []
junquillo = []

flag = False

while flag==False:
    data=input()
    
    temparray = data.split(" ")

    if(temparray[0]=="0" and temparray[1]=="0"):
        flag = True
    else:
        lagod.append(float(temparray[0]))
        junquillo.append(float(temparray[1]))

solution = solver.solve(lagod,junquillo)

for i in range(len(solution)):
    print(solution[i])
