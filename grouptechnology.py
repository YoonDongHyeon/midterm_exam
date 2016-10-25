# def sort(x,y):

machine_parts =[
 ['A','B''C','D','E'],
 ['1',1,0,1,0,0,0,0],
 ['2',1,1,1,1,0,0,0],
 ['3',1,1,0,0,0,0,0],
 ['4',0,0,0,1,0,0,0],
 ['5',0,0,0,0,1,1,1],
 ['6',0,0,0,0,1,1,0],
 ['7',0,0,0,0,0,1,1]]
machine_part =[
    [1,0,1,0,0,0,0],
 [1,1,1,1,0,0,0],
 [1,1,0,0,0,0,0],
 [0,0,0,1,0,0,0],
 [0,0,0,0,1,1,1],
 [0,0,0,0,1,1,0],
 [0,0,0,0,0,1,1]]

# while True:
blank = [[], [], [], [], [], [], []]
changematrix = [[], [], [], [], [], [], [], []]
sum_verticalline = []
totalmatrix = [[], [], [], [], [], [], [], []]
totalmatrixsub = [[], [], [], [], [], [], [], []]
for i in range(0,7):
    for k in range(0,7):
        blank[i].append(machine_part[k][i]*(2**(k+1)))
    sum_verticalline.append(sum(blank[i]))

for i in range(0,8):
    for j in range(0,7):
        if i == 0:
            totalmatrix[i].append(sum_verticalline[j])
            totalmatrixsub[i].append(sum_verticalline[j])
        else:
            totalmatrix[i].append(machine_part[i-1][j])
            totalmatrixsub[i].append(sum_verticalline[j])
print(totalmatrix)
print(sum_verticalline)

for k in range(0,8):
    for i in range(0,6):
        for j in range(i+1,7):
            if k == 0:
                if totalmatrix[0][i]> totalmatrix[0][j]:
                    t=totalmatrix[0][i]
                    totalmatrix[0][i]=totalmatrix[0][j]
                    totalmatrix[0][j]=t
            else:
                break
print(totalmatrix)
    # if totalmatrix[0]==totalmatrixsub[0]:
    #     break
    # else:
for k in range(1,8):
    for i in range(0,6):
        for j in range(1,7):
            if totalmatrix[0][i] == totalmatrixsub[0][j]:
                t = totalmatrix[k][i]
                totalmatrix[k][i]=totalmatrix[k][j]
                totalmatrix[k][j]=t
machine_part = [[],[],[],[],[],[],[]]

for i in range(0,7):
    for k in range(1,8):
        machine_part[i].append(totalmatrix[k][i])
        # continue

print(machine_part)
print(totalmatrix)



