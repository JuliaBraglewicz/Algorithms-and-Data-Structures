import time

def naive(S, W):
    m = 0
    M = len(S)
    N = len(W)
    match = 0
    comparison = 0
    while m <= M - N:
        i = 0
        while i < N:
            comparison += 1
            if S[m + i] != W[i]:
                break
            else:
                i += 1
        m += 1
        if i == N:
            match += 1
    return match, comparison

def hash(word, d, q, N):
    hw = 0
    for i in range(N):  # N - to długość wzorca
        hw = (hw*d + ord(word[i])) % q  # dla d będącego potęgą 2 można mnożenie zastąpić shiftem uzyskując pewne przyspieszenie obliczeń
    return hw

def RabinKarp(S, W):
    match = 0
    comparison = 0
    collision = 0
    d = 256
    q = 101
    M = len(S)
    N = len(W)
    hW = hash(W, d, q, N)
    for m in range(M - N + 1):
        hS = hash(S[m:m + N], d, q, N)
        comparison += 1
        if hS == hW:
            if S[m:m + N] == W:
                match += 1
            else:
                collision += 1
    return match, comparison, collision
                

def main():
    with open("lotr.txt", encoding='utf-8') as f:
        text = f.readlines()

    S = ' '.join(text).lower()
    W = 'time.'

    t_start = time.perf_counter()
    match, comp = naive(S, W)
    t_stop = time.perf_counter()
    print(f"{match}; {comp}; {t_stop - t_start:.7f}")

    t_start = time.perf_counter()
    match, comp, col = RabinKarp(S, W)
    t_stop = time.perf_counter()
    print(f"{match}; {comp}; {col}; {t_stop - t_start:.7f}")

if __name__ == "__main__":
    main()