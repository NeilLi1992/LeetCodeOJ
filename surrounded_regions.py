# Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
# For example,
# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:
#
# X X X X
# X X X X
# X X X X
# X O X X

def solve(board):
    if not board or not board[0]:
        return

    edge_position = [(0, j) for j in range(len(board[0]))] + [(len(board)-1, j) for j in range(len(board[0]))] + [(i,0) for i in range(1,len(board)-1)] + [(i, len(board[0])-1) for i in range(1,len(board)-1)]

    queue = filter(lambda (i,j):board[i][j]=='O',edge_position)
    for x,y in edge_position:
        if board[x][y] == 'O':
            queue.append((x,y))

    while queue:
        x,y = queue.pop()
        board[x][y] = 'A'

        # Search all unvisited neighbors
        neighbors = filter(lambda (i,j):0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == 'O', [(x+1,y), (x,y+1), (x-1,y), (x,y-1)])

        for pos in neighbors:
            queue.insert(0, pos)


    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'A':
                board[i][j] = 'O'
            elif board[i][j] == 'O':
                board[i][j] = 'X'

    print board


def sovle1(board):
    if not borard or not board[0]:
        return

    visited = [[False for i in range(len(board[0]))] for i in range(len(board))]
    region_index_list = []
    stack = [(0,0)]
    current_region = []

    last_symbol = ""
    while stack:
        x,y = stack.pop()
        current_symbol = board[x][y]
        visited[x][y] = True # mark as visited

        if current_symbol == 'O': # Add this into current region
            current_region.append((x,y))
        elif last_symbol == 'O':
            region_index_list.append(current_region)
            current_region = []

        # Search all unvisited neighbors
        neighbors = filter(lambda (i,j):0 <= i < len(board) and 0 <= j < len(board[0]) and not visited[i][j], [(x+1,y), (x,y+1), (x-1,y), (x,y-1)])

        for i,j in neighbors:
            neighbor_symbol = board[i][j]
            if neighbor_symbol == 'O':
                stack.append((i,j)) # Insert into stack at the end
            else:
                stack.insert(0, (i,j)) # Insert into stack from the beginning

        last_symbol = current_symbol

    print "Region number=", len(region_index_list)
    for region in region_index_list:
        if all([0<x<len(board)-1 and 0<y<len(board[0])-1 for x,y in region]):
            for x,y in region:
                board[x][y] = 'X'

board = [
['X','X','X','X'],
['X','O','O','X'],
['X','X','O','X'],
['X','O','X','X']]

solve(board)
