
# levenshtein_dist calculates the matrix
def levenshtein_dist(s1, s2):
    # init array
    s1, s2 = " " + s1, " " + s2
    h, w = len(s1), len(s2)
    m = [[0 for i in range(w)] for j in range(h)]
    for i in range(h): m[i][0] = i
    for j in range(w): m[0][j] = j

    # calculate distance
    for i in range(1, h):
        for j in range(1, w):
            repl = 0 if (s1[i] == s2[j]) else 1
            m[i][j] = min(
                # delete
                m[i - 1][j] + 1,
                # insert
                m[i][j - 1] + 1,
                # replace
                m[i - 1][j - 1] + repl
            )

    print(m)
    return m[w][h]


def weighted_levenshtein_dist(s1, s2, weights):
    print("not implemented yet")
    return 0


dist = levenshtein_dist("cats", "fast")
print(dist)
