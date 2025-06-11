def naive(S, W):
    m = 0
    len_S = len(S)
    len_W = len(W)
    match = 0
    while m < len_S - len_W:
        i = 0
        while i < len_W:
            if S[m + i] != W[i]:
                break
            else:
                i += 1
        m += 1
        if i == len_W:
            match += 1
    return match

def main():
    with open("lotr.txt", encoding='utf-8') as f:
        text = f.readlines()

    S = ' '.join(text).lower()

    W = 'time.'

    m = naive(S, W)
    print(m)

if __name__ == "__main__":
    main()