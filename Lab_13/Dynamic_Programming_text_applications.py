def cost_recursive(P, T, i, j):
    if  i == 0:
        return j
    if j == 0:
        return i
    
    insert = cost_recursive(P, T, i, j -1) + 1
    delete = cost_recursive(P, T, i - 1, j) + 1
    substitute = cost_recursive(P, T, i - 1, j - 1) + (P[i] != T[j])

    return min(insert, delete, substitute)

def cost_PD(P, T):
    p, t = len(P), len(T)
    D = [[0 for _ in range(t)] for _ in range(p)]

    for i in range(t):
        D[0][i] = i
    for j in range(p):
        D[j][0] = j

    R = [['X' for _ in range(t)] for _ in range(p)]

    for i in range(1, t):
        R[0][i] = 'I'
    for j in range(1, p):
        R[j][0] = 'D'
    
    for i in range(1, p):
        for j in range(1, t):
            insert = D[i][j - 1] + 1
            delete = D[i - 1][j] + 1
            substitute = D[i - 1][j - 1] + (P[i] != T[j])

            D[i][j] = min(insert, delete, substitute)

            
            if D[i][j] == substitute:
                if P[i] == T[j]:
                    R[i][j] = 'M'
                else:
                    R[i][j] = 'S'
            elif D[i][j] == insert:
                R[i][j] = 'I'
            else:
                R[i][j] = 'D'
                    
    return D[i][j], R

def path_reconstruction(R):
    path = []
    i = len(R) - 1
    j = len(R[0]) - 1

    while R[i][j] != 'X':
        path.append(R[i][j])
        if R[i][j] == 'I':
            j -= 1
        elif R[i][j] == 'D':
            i -= 1
        else:
            i -= 1
            j -= 1

    return ''.join(reversed(path))

def pattern_matching(P, T):
    p, t = len(P), len(T)
    D = [[0 for _ in range(t)] for _ in range(p)]

    for j in range(p):
        D[j][0] = j

    R = [['X' for _ in range(t)] for _ in range(p)]

    for j in range(1, p):
        R[j][0] = 'D'
    
    for i in range(1, p):
        for j in range(1, t):
            insert = D[i][j - 1] + 1
            delete = D[i - 1][j] + 1
            substitute = D[i - 1][j - 1] + (P[i] != T[j])

            D[i][j] = min(insert, delete, substitute)

            
            if D[i][j] == substitute:
                if P[i] == T[j]:
                    R[i][j] = 'M'
                else:
                    R[i][j] = 'S'
            elif D[i][j] == insert:
                R[i][j] = 'I'
            else:
                R[i][j] = 'D'
                    
        last = D[-1]
        minimum = min(last)

    return minimum, last.index(minimum)
    
def longest_common_sequence(P, T):
    p, t = len(P), len(T)
    D = [[0 for _ in range(t)] for _ in range(p)]

    for i in range(t):
        D[0][i] = i
    for j in range(p):
        D[j][0] = j

    R = [['X' for _ in range(t)] for _ in range(p)]

    for i in range(1, t):
        R[0][i] = 'I'
    for j in range(1, p):
        R[j][0] = 'D'
    
    for i in range(1, p):
        for j in range(1, t):
            insert = D[i][j - 1] + 1
            delete = D[i - 1][j] + 1
            substitute = D[i - 1][j - 1] + (P[i] != T[j]) * 1000

            D[i][j] = min(insert, delete, substitute)

            
            if D[i][j] == substitute:
                if P[i] == T[j]:
                    R[i][j] = 'M'
                else:
                    R[i][j] = 'S'
            elif D[i][j] == insert:
                R[i][j] = 'I'
            else:
                R[i][j] = 'D'
                    
    return D[i][j], R

def common_sequence_reconstruction(P, T, R):
    path = []
    i = len(R) - 1
    j = len(R[0]) - 1

    while R[i][j] != 'X':
        if R[i][j] == 'M':
            path.append(P[i])
        if R[i][j] == 'I':
            j -= 1
        elif R[i][j] == 'D':
            i -= 1
        else:
            i -= 1
            j -= 1  

    return ''.join(reversed(path))

def main():
    P = ' kot'
    T = ' pies'
    print(cost_recursive(P, T, 3, 4))

    P = ' biały autobus'
    T = ' czarny autokar'
    cost, _ = cost_PD(P, T)
    print(cost)

    P = ' thou shalt not'
    T = ' you should not'
    _, R = cost_PD(P, T)
    print(path_reconstruction(R))

    P = ' ban'
    T = ' mokeyssbanana'
    _, index = pattern_matching(P, T)
    print(index - len(P) + 2)

    P = ' bin'
    _, index = pattern_matching(P, T)
    print(index - len(P) + 2)

    P = ' democrat'
    T = ' republican'
    _, R = longest_common_sequence(P, T)
    print(common_sequence_reconstruction(P, T, R))

    T = ' 243517698'
    P = "".join(sorted(T))
    _, R = longest_common_sequence(P, T)
    print(common_sequence_reconstruction(P, T, R))

if __name__ == "__main__":
    main()