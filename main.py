from typing import List

m = ["a", "b", "b", "a", "z", "x"]


def double(m: List):
    counter = len(m) - 1
    # print(counter)
    for i in range(counter):
        if m[i] == m[i + 1]:
            deleting(i)
            break

            # double(m, counter)


def deleting(i):
    # for x in range(counter):
    # I = double(m, counter)
    # print(m[I],m[j])
    m.remove(m[i])
    m.remove(m[i])
    double(m)
    # print(m)


double(m)
print(m)


