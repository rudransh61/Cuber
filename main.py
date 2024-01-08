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

# all turns 
def turnF(Uface, Dface, Lface, Rface, Fface, Bface):
    pass

def turnL(Uface, Dface , Lface ,Rface , Fface , Bface):
    #U[0][0] U[1][0] to D[1][0] D[0][0]
    Uface[0][0] , Dface[1][0] = swap(Uface[0][0],Dface[1][0])
    Uface[1][0] , Dface[0][0] = swap(Uface[1][0],Dface[0][0])

    Lface[0], Lface[1] = swap(Lface[0],Lface[1]) 
    Fface[0], Bface[0] = swap(Fface[0],Bface[0])

    return Uface,Dface,Lface,Rface,Fface,Bface


def turnB(Uface, Dface , Lface ,Rface , Fface , Bface):
    #U[0][0] U[1][0] to D[1][0] D[0][0]
    Uface[0][1] , Dface[1][1] = swap(Uface[0][1],Dface[1][1])
    Uface[1][1] , Dface[0][1] = swap(Uface[1][1],Dface[0][1])

    Lface[1], Lface[0] = swap(Lface[1],Lface[0]) 
    Fface[1], Bface[1] = swap(Fface[1],Bface[1])

    return Uface,Dface,Lface,Rface,Fface,Bface


 

     
    

def solve_2x2x1(Uface, Dface, Lface, Rface, Fface, Bface):
    U = Uface
    D = Dface
    L = Lface
    R = Rface
    F = Fface
    B = Bface
    with open("merged_output.txt", "r") as myfile:
        for mystring in myfile:
            digits = mystring.split()
            for char in digits:
                print(char, end=' ')
                for digit in char:
                    if digit == '1':
                        # print("1check", end=' ')
                        U,D,L,R,F,B = turnF(U, D, L, R, F, B)
                    elif digit == '2':
                        # print("2check", end=' ')
                        U,D,L,R,F,B = turnB(U, D, L, R, F, B)
                    elif digit == '3':
                        # print("3check", end=' ')
                        pass
                    elif digit == '4':
                        # print("4check", end=' ')
                        U,D,L,R,F,B = turnL(U,D,L,R,F,B)
                        #pass
                    else:
                        print("Invalid character found in file")
    print("")
    return None


# NOTE:
# 1 = F
# 2 = B
# 3 = R
# 4 = L

U = [[1, 1], 
     [1, 1]]
D = [[2, 2], 
     [2, 2]]
L = [3, 3]
R = [4, 4]
F = [5, 5]
B = [6, 6]
U,D,R,L,F,B = turnL(U,D,R,L,F,B)
print(U,D,R,L,F,B)

if is_solved(U, D, L, R, F, B):
    print("YES it is solved!")
else:
    print("No it is not solved!")
    # Solve
    solve_2x2x1(U, D, L, R, F, B)


