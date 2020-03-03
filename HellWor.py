
from ortools.sat.python import cp_model

test1 = [
[1,1,1 ,1,1,1 ,1,1,1],
[2,2,2 ,2,2,2 ,2,2,2],
[3,3,3 ,3,3,3 ,3,3,3],

[1,2,3,4,5,6,7,8,9],
[1,2,3,4,5,6,7,8,9],
[1,2,3,4,5,6,7,8,9],

[1,4,7,1,4,7,1,4,7],
[2,5,8,2,5,8,2,5,8],
[3,6,9,3,6,9,3,6,9]
]



def CreeSudoku(taille,test1):
    model = cp_model.CpModel()
    for x in  range(0,taille):
        for y in range(0,taille):
            case =  model.NewIntVar(1,9 , 'coord_%s' % (str(str(x)+"-"+str(y))))
            test1[x][y]=case
    return  model,test1

def SepareSudoku(sudoku, tailleBlocs):
    listBlocs= []
    listLignes=[]
    listColonnes=[]
    for ligne in sudoku:
        listLignes.append(ligne)
    for numColonne in  range(0,len(sudoku[0])):
        colonne = []
        for numLigne in range(0,len(sudoku)):
            colonne.append(sudoku[numLigne][numColonne])
        listColonnes.append(colonne)

    nbBlockParLigne = len(sudoku)/tailleBlocs

    for i in range (0,int(nbBlockParLigne)):
        for j in range (0,int(nbBlockParLigne)):
            bloc = []
            for x in range (0,tailleBlocs):
                for y in range (0,tailleBlocs):
                    bloc.append(sudoku[i*tailleBlocs+x][j*tailleBlocs+y])
            listBlocs.append(bloc)

    return listBlocs,listColonnes,listLignes

def AppliqueConditions(sudoku,mod):
    blocs,colonnes,lignes = SepareSudoku(sudoku,3)
    for bloc in blocs :
        mod.AddAllDifferent(bloc)
    for colonne in colonnes :
        mod.AddAllDifferent(colonne)
    for ligne in lignes :
        mod.AddAllDifferent(ligne)
    return mod

def printList(l):
    for el in l:
        print(solver.Value(el))

def printMat(matrice,solver):
    print()
    for row in  range(0, len(matrice[0])):
        rowStr = ""
        for column in range(0, len(matrice[1])):
            rowStr = rowStr + str(solver.Value(matrice[row][column])) + " "
            if ((column + 1)% 3) == 0:
                rowStr = rowStr + " "
            
        print(rowStr)
        if ((row + 1 )% 3) == 0:
            print()


mod,t = CreeSudoku(9,test1)

# b,c,l =SepareSudoku(test1,3)

# printList(b)
# print()
# printList(c)
# print()
# printList(l)
# print()
# printMat(test1)

mod = AppliqueConditions(test1,mod)
solver = cp_model.CpSolver()
status = solver.Solve(mod)

printMat(test1,solver)


#model.addAllDifferent()