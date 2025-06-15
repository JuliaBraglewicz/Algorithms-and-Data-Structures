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
    for i in range(N):
        hw = (hw*d + ord(word[i])) % q
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

def RabinKarp_with_rolling_hash(S, W):
    match = 0
    comparison = 0
    collision = 0
    d = 256
    q = 101
    M = len(S)
    N = len(W)
    h = 1
    for i in range(N - 1):
        h = (h*d) % q 
    hW = hash(W, d, q, N)
    hS = hash(S[0:N], d, q, N)
    for m in range(M - N + 1):
        comparison += 1
        if hS == hW:
            if S[m:m + N] == W:
                match += 1
            else:
                collision += 1
        if m < M - N:
            hS = (d * (hS - ord(S[m]) * h) + ord(S[m + N])) % q
            if hS < 0:
                hS += q
    return match, comparison, collision

def kmp_search(S, W):
    comparison = 0
    m = 0
    i = 0
    T = kmp_table(W)
    M = len(S)
    N = len(W)
    P = []
    nP = 0
    while m < M:
        comparison += 1
        if W[i] == S[m]:
            m += 1
            i += 1
            if i == N:
                P.append(m - i)
                nP += 1
                i = T[i]
        else:
            i = T[i]
            if i < 0:
                m += 1
                i += 1
    return nP, comparison, T

def kmp_table(W):
    N = len(W)
    T = [None for _ in range(N + 1)]
    pos = 1
    cnd = 0
    T[0] = -1
    while pos < N:
        if W[pos] == W[cnd]:
            T[pos] = T[cnd]
        else:
            T[pos] = cnd
            while cnd >= 0 and W[pos] != W[cnd]:
                cnd = T[cnd]
        pos += 1
        cnd += 1
    T[pos] = cnd
    return T

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

    t_start = time.perf_counter()
    match, comp, col = RabinKarp_with_rolling_hash(S, W)
    t_stop = time.perf_counter()
    print(f"{match}; {comp}; {col}; {t_stop - t_start:.7f}")

    t_start = time.perf_counter()
    nP, comp, T = kmp_search(S, W)
    t_stop = time.perf_counter()
    print(f"{nP}; {comp}; {T}; {t_stop - t_start:.7f}")

if __name__ == "__main__":
    main()