test1 = [
[1,1,1,1,1,1,1,1,1],
[2,2,2,2,2,2,2,2,2],
[3,3,3,3,3,3,3,3,3],

[1,2,3,4,5,6,7,8,9],
[1,2,3,4,5,6,7,8,9],
[1,2,3,4,5,6,7,8,9],

[1,4,7,1,4,7,1,4,7],
[2,5,8,2,5,8,2,5,8],
[3,6,9,3,6,9,3,6,9]
]





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

def printList(l):
    for el in l:
        print(el)

b,c,l =SepareSudoku(test1,3)

printList(b)
print()
printList(c)
print()
printList(l)

#model.addAllDifferent()