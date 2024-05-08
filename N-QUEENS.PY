

#function for safe sequence
def is_safe(mat,r,c):
    #`column check`
    for i in range(r):
        if mat[i][c]=="Q":
            return False
    #upperleft and bottom-right diagonal check
    (i,j)=(r,c)
    while i>=0 and j>=0:
        if mat[i][j]=="Q":
            return False
        i-=1
        j-=1
    #upper-right and bottom left diagonal check
    (i,j)=(r,c)
    while i>=0 and j<len(mat):
        if mat[i][j]=="Q":
            return False
        i-=1
        j+=1
    return True
#function to print board
def print_board(mat):
    for r in mat:
        print("".join(r))
    print()

#function to solve nqueens problem
def nQueens(mat,r):
    if r==len(mat):
        print_board(mat)
        return
    for i in range(len(mat)):
        if is_safe(mat,r,i):
            mat[r][i]='Q'
            nQueens(mat,r+1)
            mat[r][i]='_' #backtrack function

if __name__=="__main__":
 n=int(input("enter number of queens:")) #N x N board
 mat=[['_'for x in range(n)]for y in range(n)]

nQueens(mat,0) 





        
        
