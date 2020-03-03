
from ortools.sat.python import cp_model


def CreeSudoku(taille):
    model = cp_model.CpModel()
    mat=[]
    for x in  range(0,taille):
        ligne =[]
        for y in range(0,taille):
            case =  model.NewIntVar(1,taille , 'coord_%s' % (str(str(x)+"-"+str(y))))
            ligne.append(case)
        mat.append(ligne)
    return  model, mat

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
    blocs,colonnes,lignes = SepareSudoku(sudoku,int(len(sudoku)**0.5))
    for bloc in blocs :
        mod.AddAllDifferent(bloc)
    for colonne in colonnes :
        mod.AddAllDifferent(colonne)
    for ligne in lignes :
        mod.AddAllDifferent(ligne)
    return mod

def printMat(matrice,solver):
    tailleBloc = int(len(matrice)**0.5)
    print()
    for row in  range(0, len(matrice[0])):
        rowStr = ""
        for column in range(0, len(matrice[1])):
            valCase = solver.Value(matrice[row][column])
            rowStr = rowStr + str(valCase) + " "
            if len(matrice) >9 and valCase<10:
                rowStr=rowStr+" "
            if ((column + 1)% tailleBloc) == 0:
                rowStr = rowStr + " "
            
        print(rowStr)
        if ((row + 1 )% tailleBloc) == 0:
            print()


mod,sudoku = CreeSudoku(25)   # marche pour des valeur carree   (4, 9, 16 ,25, ...)

mod = AppliqueConditions(sudoku,mod)
solver = cp_model.CpSolver()
status = solver.Solve(mod)

printMat(sudoku,solver)