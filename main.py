from typing import List

m = ["a", "b", "b", "a", "z", "x"]


def double(m: List):
    counter = len(m) - 1

    for i in range(counter):
        if m[i] == m[i + 1]:
            deleting(i)
            break


def deleting(i):
    m.remove(m[i])
    m.remove(m[i])
    double(m)


double(m)
print(m)
