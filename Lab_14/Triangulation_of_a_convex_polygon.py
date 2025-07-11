import time
import math

def length(i, k, j):
    return math.sqrt((i[0] - k[0])**2 + (i[1] - k[1])**2) + math.sqrt((k[0] - j[0])**2 + (k[1] - j[1])**2) + math.sqrt((i[0] - j[0])**2 + (i[1] - j[1])**2)

def triangulation_recursive(points, i, j):
    if j - i < 2:
        return 0
    min_cost = float("inf")
    for k in range(i + 1, j):
        cost = length(points[i], points[k], points[j]) + triangulation_recursive(points, i, k) + triangulation_recursive(points, k, j)
        if cost < min_cost:
            min_cost = cost
    return min_cost

def triangulation_iterative(points):
    n = len(points)
    D = [[0 for _ in range(n)] for _ in range(n)]
    for l in range(2, n):
        for i in range(n - l):
            j = i + l
            D[i][j] = float("inf")
            for k in range(i + 1, j):
                cost = D[i][k] + D[k][j] + length(points[i], points[k], points[j])
                D[i][j] = min(D[i][j], cost)
    return D[0][-1]


def main():
    set_1 = [[0, 0], [1, 0], [2, 1], [1, 2], [0, 2]]
    set_2 = [[0, 0], [4, 0], [5, 4], [4, 5], [2, 5], [1, 4], [0, 3], [0, 2]]

    t_start = time.perf_counter()
    cost = triangulation_recursive(set_1, 0, len(set_1) - 1)
    t_stop = time.perf_counter()
    print(f"{cost:.4f}")
    print(f"{t_stop - t_start:.7f}")

    t_start = time.perf_counter()
    cost = triangulation_recursive(set_2, 0, len(set_2) - 1)
    t_stop = time.perf_counter()
    print(f"{cost:.4f}")
    print(f"{t_stop - t_start:.7f}")

    t_start = time.perf_counter()
    cost = triangulation_iterative(set_1)
    t_stop = time.perf_counter()
    print(f"{cost:.4f}")
    print(f"{t_stop - t_start:.7f}")

    t_start = time.perf_counter()
    cost = triangulation_iterative(set_2)
    t_stop = time.perf_counter()
    print(f"{cost:.4f}")
    print(f"{t_stop - t_start:.7f}")

if __name__ == "__main__":
    main()