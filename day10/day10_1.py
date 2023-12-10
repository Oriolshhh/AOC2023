import sys

# Augmentem limit de recursivitat, es podria haver fer també amb bfs i evitarnos haver d'expandir el limit de recursivitat
sys.setrecursionlimit(1000000)

# DFS
def dfs(row, col):
    # Comprovem si la posició actual ja ha estat visitada
    if visited[row][col]:
        return
    # La marquem com a visitada
    visited[row][col] = True

    # Definim les direccions possibles
    directions = ["SLJ|", "SLF-", "S7F|", "S7J-"]
    dRow = [-1, 0, 1, 0]  # Canvis en la fila per a cada direcció
    dCol = [0, 1, 0, -1]  # Canvis en la columna per a cada direcció

    # Explorem les 4 direccions possibles
    for dir in range(4):
        if a[row][col] in directions[dir]: # Comprovem si la pipe permet aquesta direcció
            nRow, nCol = row + dRow[dir], col + dCol[dir]
            # Comprovem que la posició resultant sigui valida i que la pipe de la posició resultant permeti la direcció contraria
            if 0 <= nRow < rows and 0 <= nCol < cols and a[nRow][nCol] in directions[dir ^ 2]:
                # Si es valida fem dfs a partir d'aquesta posició
                dfs(nRow, nCol)

# Llegir la matriu del fitxer
with open('day10/input', 'r') as file:
    a = [line.strip() for line in file.readlines()]

rows = len(a)
cols = len(a[0])
visited = [[False for _ in range(cols)] for _ in range(rows)] # Inicialitzem la matriu de posicions visitades

for row in range(rows):
    for col in range(cols):
        if a[row][col] == 'S': # Si hm trobat la posició inicial començem el dfs a partir d'aquesta
            dfs(row, col)
            print(sum(sum(row) for row in visited) // 2) # Printem el numero de posicions visitades
            break  
