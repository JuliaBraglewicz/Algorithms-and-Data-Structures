class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

def Jarvis(points):
    n = len(points)
    if n < 3:
        return points
    left = min(points, key = lambda p: (p.x, p.y))
    p = points.index(left)
    hull = []
    while True:
        hull.append(points[p])
        q = (p + 1) % n
        for r in range(n):
            if r == p or r == q:
                continue
            val = (points[q].y - points[p].y) * (points[r].x - points[q].x) - (points[r].y - points[q].y) * (points[q].x - points[p].x)
            if val > 0:
                q = r
        p = q
        if points[p] == hull[0]:
            break
    return hull

def Jarvis_2(points):
    n = len(points)
    if n < 3:
        return points
    left = min(points, key = lambda p: (p.x, p.y))
    p = points.index(left)
    hull = []
    while True:
        hull.append(points[p])
        q = (p + 1) % n
        for r in range(n):
            if r == p or r == q:
                continue
            val = (points[q].y - points[p].y) * (points[r].x - points[q].x) - (points[r].y - points[q].y) * (points[q].x - points[p].x)
            if val > 0:
                q = r
            elif val == 0:
                length_pr = (points[p].x - points[r].x)**2 + (points[p].y - points[r].y)**2
                length_pq = (points[p].x - points[q].x)**2 + (points[p].y - points[q].y)**2
                if length_pr > length_pq:
                    q = r
        p = q
        if points[p] == hull[0]:
            break
    return hull

def main():
    set_1 = [(0, 3), (0, 0), (0, 1), (3, 0), (3, 3)]
    set_2 = [(0, 3), (0, 1), (0, 0), (3, 0), (3, 3)]
    set_3 = [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]

    for i in range(len(set_1)):
        set_1[i] = Point(set_1[i][0], set_1[i][1])
        set_2[i] = Point(set_2[i][0], set_2[i][1])

    for i in range(len(set_3)):
        set_3[i] = Point(set_3[i][0], set_3[i][1])

    print(Jarvis(set_1))
    print(Jarvis(set_2))

    print(Jarvis_2(set_1))
    print(Jarvis_2(set_2))

    print(Jarvis(set_3))
    print(Jarvis_2(set_3))

if __name__ == "__main__":
    main()