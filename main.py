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
def turnU(Uface, Dface, Lface, Rface, Fface, Bface):
    pass

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
                        turnU(U, D, L, R, F, B)
                        pass
                    elif digit == '2':
                        # print("2check", end=' ')
                        pass
                    elif digit == '3':
                        # print("3check", end=' ')
                        pass
                    elif digit == '4':
                        # print("4check", end=' ')
                        pass
                    else:
                        print("Invalid character found in file")
    print()


# NOTE:
# 1 = U
# 2 = D
# 3 = R
# 4 = L

def main():
    U = [[1, 2], [1, 1]]
    D = [[2, 2], [2, 2]]
    L = [3, 3]
    R = [4, 4]
    F = [5, 5]
    B = [6, 6]

    if is_solved(U, D, L, R, F, B):
        print("YES it is solved!")
    else:
        print("No it is not solved!")

        # Solve
        solve_2x2x1(U, D, L, R, F, B)


if __name__ == "__main__":
    main()
