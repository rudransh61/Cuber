def swap(var1, var2):
    return var2, var1

def is_solved(Uface, Dface, Lface, Rface, Fface, Bface):
    # Check for Uface
    if any(Uface[i][j] != Uface[0][0] for i in range(2) for j in range(2)):
        return False

    # Check for Dface
    if any(Dface[i][j] != Dface[0][0] for i in range(2) for j in range(2)):
        return False

    # Check for Lface
    if Lface[0] != Lface[1]:
        return False

    # Check for Rface
    if Rface[0] != Rface[1]:
        return False

    # Check for Fface
    if Fface[0] != Fface[1]:
        return False

    # Check for Bface
    if Bface[0] != Bface[1]:
        return False

    return True

def turnL2(Uface, Dface , Lface ,Rface , Fface , Bface):
    Uface[0][0] , Dface[1][0] = swap(Uface[0][0],Dface[1][0])
    Uface[1][0] , Dface[0][0] = swap(Uface[1][0],Dface[0][0])

    Lface[0], Lface[1] = swap(Lface[0],Lface[1]) 
    Fface[0], Bface[0] = swap(Fface[0],Bface[0])

    return Uface, Dface, Lface, Rface, Fface, Bface

def turnR2(Uface, Dface , Lface ,Rface , Fface , Bface):
    Uface[0][1] , Dface[1][1] = swap(Uface[0][1],Dface[1][1])
    Uface[1][1] , Dface[0][1] = swap(Uface[1][1],Dface[0][1])

    Rface[0], Rface[1] = swap(Rface[0],Rface[1]) 
    Fface[1], Bface[1] = swap(Fface[1],Bface[1])

    return Uface, Dface, Lface, Rface, Fface, Bface

def turnF2(Uface, Dface, Lface, Rface, Fface, Bface):
    Uface[0][0], Rface[0] = swap(Rface[0], Uface[0][0])
    Uface[0][1], Rface[1] = swap(Rface[1], Uface[0][1])
    Dface[0][0], Lface[0] = swap(Lface[0], Dface[0][0])
    Dface[0][1], Lface[1] = swap(Lface[1], Dface[0][1])

    Fface[0], Fface[1] = swap(Fface[1], Fface[0])

    return Uface, Dface, Lface, Rface, Fface, Bface

def turnB2(Uface, Dface, Lface, Rface, Fface, Bface):
    Uface[0][1], Rface[0] = swap(Rface[0], Uface[0][1])
    Uface[1][1], Rface[1] = swap(Rface[1], Uface[1][1])
    Dface[0][1], Lface[0] = swap(Lface[0], Dface[0][1])
    Dface[1][1], Lface[1] = swap(Lface[1], Dface[1][1])

    Bface[0], Bface[1] = swap(Bface[1], Bface[0])

    return Uface, Dface, Lface, Rface, Fface, Bface

def generate_moves(cube_state, depth, move_sequence):
    if depth == 0:
        if is_solved(*cube_state):
            print("Solution found:", move_sequence)
            return True
        return False

    for move in ['L2', 'R2', 'F2', 'B2']:
        new_state = cube_state
        if move == 'L2':
            new_state = turnL2(*new_state)
        elif move == 'R2':
            new_state = turnR2(*new_state)
        elif move == 'F2':
            new_state = turnF2(*new_state)
        elif move == 'B2':
            new_state = turnB2(*new_state)

        if generate_moves(new_state, depth - 1, move_sequence + [move]):
            return True

    return False

def solve_2x2x1(cube_state):
    depth = 1
    while not generate_moves(cube_state, depth, []):
        depth += 1

# Initial state
U = [[1, 1],
     [1, 1]]
D = [[2, 2],
     [2, 2]]
L = [3, 3]
R = [4, 4]
F = [5, 5]
B = [6, 6]

# Solve the cube
solve_2x2x1((U, D, L, R, F, B))
