import copy
from sortedcontainers import SortedSet

class Spade:
    frequent_items = list()
    dataset = list()

    def run(dataset, minsup):
        elements = SortedSet()
        freq = dict()
        for i in range(0, len(dataset)):
            for j, item in enumerate(dataset[i]):
                if isinstance(item, int):
                    elements.add(item)
                    if item not in freq:
                        freq[item] = dict()
                    if i not in freq[item]:
                        freq[item][i] = list()
                    freq[item][i].append(j)
                else:
                    for s_item in item:
                        elements.add(s_item)
                        if s_item not in freq:
                            freq[s_item] = dict()
                        if i not in freq[s_item]:
                            freq[s_item][i] = list()
                        freq[s_item][i].append(j)

        elements = list(elements)

        sup = dict()

        Spade.frequent_items = list()
        def SPADE(minsup, P, k):
            newP = list()
            newP_used = SortedSet()
            for i, r_a in enumerate(P):
                if str(r_a[0]) not in newP_used:
                    newP_used.add(str(r_a[0]))
                    newP.append(r_a)
                for j, r_b in enumerate(P):
                    if j <= i:
                        continue
                    if r_a[0][:-1] != r_b[0][:-1]:
                        continue
                    r_ab = copy.deepcopy(r_a[0])
                    r_ab[-1] = r_ab[-1] | r_b[0][k]
                    if str(r_ab) in newP_used:
                        continue
                    L_r_ab = dict()
                    for transaction, occurences in r_a[1].items():
                        if transaction not in r_b[1]:
                            continue
                        l = 0                            
                        for occurence in r_b[1][transaction]:
                            while l < len(occurences) and occurence > occurences[l]:
                                l += 1
                            if l != len(occurences) and occurence == occurences[l]:
                                if transaction not in L_r_ab:
                                    L_r_ab[transaction] = list()
                                L_r_ab[transaction].append(occurence)
                    if len(L_r_ab) >= minsup:
                        newP.append((r_ab, L_r_ab))
                        newP_used.add(str(r_ab))
            if len(newP) != len(P):
                # newP.extend(P)
                SPADE(minsup, newP, k)
                return

            for r_a in P:
                Spade.frequent_items.append(r_a[0])
                sup[str(r_a[0])] = len(r_a[1])
                newP = list()
                for r_b in P:
                    if r_a[0][:-1] != r_b[0][:-1]:
                        continue
                    r_ab = copy.deepcopy(r_a[0])
                    r_ab.append(r_b[0][k])
                    L_r_ab = dict()
                    for transaction, occurences in r_a[1].items():
                        if transaction not in r_b[1]:
                            continue
                        for occurence in r_b[1][transaction]:
                            if occurence > occurences[0]:
                                if transaction not in L_r_ab:
                                    L_r_ab[transaction] = list()
                                L_r_ab[transaction].append(occurence)
                    if len(L_r_ab) >= minsup:
                        newP.append((r_ab, L_r_ab))
                if len(newP) != 0:
                    SPADE(minsup, newP, k + 1)
        
        P = list()
        for element in elements:
            if len(freq[element]) >= minsup:
                P.append((list([SortedSet([element])]), freq[element]))
        SPADE(minsup, P, 0)

        print("SPADE: Number of frequent sequences: " + str(len(Spade.frequent_items)))

# Spade.run([

# ], 80)

# with open("spade.txt", 'w') as file:
#     for pattern in Spade.frequent_items:
#         file.write(str(pattern) + "\n")
# print(len(Spade.frequent_items))