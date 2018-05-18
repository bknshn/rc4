from copy import deepcopy

def plus(a, b):
    return (a + b) % 256

def z1_count():
    # 253!
    def cases(length):
        ans = 1
        while (length > 253):
            ans *= length
            length -= 1
        return ans

    output = [0 for _ in range(256)]
    perm_list = list(range(256))
    S = [None for _ in range(256)]
    i = 1
    for j in perm_list:
        perm_list1 = deepcopy(perm_list)
        perm_list1.remove(j)
        S1 = deepcopy(S)
        S1[i] = j
        if S1[j] is None:
            for y in perm_list1:
                perm_list2 = deepcopy(perm_list1)
                perm_list2.remove(y)
                S2 = deepcopy(S1)
                S2[j] = y
                S2[i], S2[j] = S2[j], S2[i]
                if S2[plus(S2[i], S2[j])] is None:
                    for num in perm_list2:
                        output[num] += cases(len(perm_list2) - 1)
                else:
                    output[S2[plus(S2[i], S2[j])]] += cases(len(perm_list2))
        else:
            S1[i], S1[j] = S1[j], S1[i]
            if S1[plus(S1[i], S1[j])] is None:
                for num in perm_list1:
                    output[num] += cases(len(perm_list1) - 1)
            else:
                output[S1[plust(S1[i], S1[j])]] += cases(len(perm_list1))
    return output

output = [0 for _ in range(256)]
def count(depth, S, i, j, perm_list):
    def cases(length):
        MAX_LENGTH = 251
        # z1: 253 (256 - 3)
        # z2: 251 (256 - 5)
        assert length >= MAX_LENGTH, 'length not appropriate (length: {}, max length: {})'.format(length, MAX_LENGTH)
        ans = 1
        while (length > MAX_LENGTH):
            ans *= length
            length -= 1
        return ans

    if depth == 0:
        if S[plus(S[i], S[j])] is None:
            for num in perm_list:
                output[num] += cases(len(perm_list) - 1)  # 4
        else:
            output[S[plus(S[i], S[j])]] += cases(len(perm_list))  # 4
        return

    if depth == 1:
        print('hoge')

    i = plus(i, 1)  # 1
    if S[i] is None:
        for x in perm_list:
            perm_list1 = deepcopy(perm_list)
            perm_list1.remove(x)
            S1 = deepcopy(S)
            S1[i] = x
            j1 = plus(j, S1[i])  # 2
            if S1[j1] is None:
                for y in perm_list1:
                    perm_list2 = deepcopy(perm_list1)
                    perm_list2.remove(y)
                    S2 = deepcopy(S1)
                    S2[j1] = y
                    S2[i], S2[j1] = S2[j1], S2[i]  # 3
                    count(depth-1, deepcopy(S2), i, j1, deepcopy(perm_list2))
            else:
                S1[i], S1[j1] = S1[j1], S1[i]  # 3
                count(depth-1, deepcopy(S1), i, j1, deepcopy(perm_list1))
    else:
        j = plus(j, S[i])  # 2
        if S[j] is None:
            for y in perm_list:
                perm_list2 = deepcopy(perm_list)
                perm_list2.remove(y)
                S2 = deepcopy(S)
                S2[j] = y
                S2[i], S2[j] = S2[j], S2[i]  # 3
                count(depth-1, deepcopy(S2), i, j, deepcopy(perm_list2))
        else:
            S[i], S[j] = S[j], S[i]  # 3
            count(depth-1, deepcopy(S), i, j, deepcopy(perm_list))

if __name__ == '__main__':
    perm_list = list(range(256))
    S = [None for _ in range(256)]
    count(2, deepcopy(S), 0, 0, deepcopy(perm_list))

    for i, num in enumerate(output):
        print('{} {}'.format(i, num))
