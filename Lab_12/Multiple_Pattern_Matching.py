import time

def hash(word, d, q, N):
    hw = 0
    for i in range(N):
        hw = (hw*d + ord(word[i])) % q
    return hw

def RabinKarp(S, W):
    match = {}
    for pattern in W:
        match[pattern] = 0

    correct = 0
    false = 0
    d = 256
    q = 101
    M = len(S)
    N = len(W[0])

    h = 1
    for i in range(N - 1):
        h = (h*d) % q 

    hW = set()
    for w in W:
        hW.add(hash(w, d, q, N))

    hS = hash(S[0:N], d, q, N)
    for m in range(M - N + 1):
        if hS in hW:
            if S[m:m + N] in W:
                match[S[m:m + N]] += 1
                correct += 1
            else:
                false += 1
        if m < M - N:
            hS = (d * (hS - ord(S[m]) * h) + ord(S[m + N])) % q
            if hS < 0:
                hS += q
    return match, correct, false

def main():
    with open("lotr.txt", encoding='utf-8') as f:
        text = f.readlines()

    S = ' '.join(text).lower()
    W = ['gandalf', 'looking', 'blocked', 'comment', 'pouring', 'finally', 'hundred', 'hobbits', 'however', 'popular', 'nothing', 'enjoyed', 'stuffed', 'relaxed', 'himself', 'present', 'deliver', 'welcome', 'baggins', 'further']
    test = int(input())
    
    if test == 1:
        t_start = time.perf_counter()
        match, correct, false = RabinKarp(S, W[0])
        t_stop = time.perf_counter()
        print(f"{t_stop - t_start:.7f}")

        t_start = time.perf_counter()
        match, correct, false = RabinKarp(S, W)
        t_stop = time.perf_counter()
        print(f"{t_stop - t_start:.7f}")

    elif test == 2:
        match, correct, false = RabinKarp(S, W)
        for pattern in match.keys():
            print(f"{pattern} {match[pattern]}")
        print(f"{correct}")
        print(f"{false}")

if __name__ == "__main__":
    main()