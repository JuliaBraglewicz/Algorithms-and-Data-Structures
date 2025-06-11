import time

def naive(S, W):
    m = 0
    len_S = len(S)
    len_W = len(W)
    match = 0
    comparison = 0
    while m <= len_S - len_W:
        i = 0
        while i < len_W:
            comparison += 1
            if S[m + i] != W[i]:
                break
            else:
                i += 1
        m += 1
        if i == len_W:
            match += 1
    return match, comparison

def Rabin_Karp(S, W):
    pass

def main():
    with open("lotr.txt", encoding='utf-8') as f:
        text = f.readlines()

    S = ' '.join(text).lower()
    W = 'time.'

    t_start = time.perf_counter()
    match, comp = naive(S, W)
    t_stop = time.perf_counter()
    print(f"{match}; {comp}; {t_stop - t_start:.7f}")

if __name__ == "__main__":
    main()