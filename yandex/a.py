def end(a):
    return a[0] + a[1] - 1


n = int(input())

inp2 = []
for i in range(n):
    inp2.append([int(x) for x in input().split(' ')])

inp = sorted(inp2, key=lambda x: x[0] + x[1])

d = [[0, inp[0][1]]]
ends0 = [end(inp[0])]
ends1 = [end(inp[0])]
history = [[[], [0]], ]
for i in range(1, len(inp)):
    d.append([])
    history.append([[], []])
    if d[i - 1][0] > d[i - 1][1]:
        d[i].append(d[i - 1][0])
        history[-1] = [[*history[-2][0]], []]
    else:
        d[i].append(d[i - 1][1])
        history[-1] = [[*history[-2][1]], []]
    if d[i][0] == d[i - 1][0]:
        ends0.append(ends0[i - 1])
    else:
        ends0.append(ends1[i - 1])
    start = inp[i][0]
    ind = -1
    # d[i][1] = ?
    new_ends1 = list(map(lambda x: x if x < start else -1000000000000, ends1))
    if len(list(filter(lambda x: x > 0, new_ends1))) == 0:
        mend_ind1 = -1
    else:
        mend_ind1 = new_ends1.index(max(new_ends1))
    new_ends0 = list(map(lambda x: x if x < start else -1000000000000, ends0))
    mend_ind0 = new_ends0.index(max(new_ends0))
    if mend_ind1 > -1:
        if d[mend_ind0][0] > d[mend_ind1][1]:
            d[i].append(d[mend_ind0][0] + inp[i][1])
            history[-1][1] = [*history[mend_ind0][0], i]
        else:
            d[i].append(d[mend_ind1][1] + inp[i][1])
            history[-1][1] = [*history[mend_ind1][1], i]

    else:
        d[i].append(inp[i][1])
        history[-1][1] = [i]
    ends1.append(end(inp[i]))

alla = []
alla_history = []
for i in d:
    for j in i:
        alla.append(j)

for i in history:
    for j in i:
        alla_history.append(j)
print(max(alla))
res_his = ""
for i in alla_history[alla.index(max(alla))]:
    real_index = inp2.index(inp[i])
    res_his += str(real_index) + " "

print(res_his)


