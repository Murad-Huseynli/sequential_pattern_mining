from collections import defaultdict
import copy
from sortedcontainers import SortedSet

class PrefixSpan:
    minsup = 1
    patterns = list()

    def _calculate_frequent_items(data, pr_set):
        item_counts = defaultdict(int)
        for sequence in data:
            visited = SortedSet()
            for i, itemset in enumerate(sequence):
                if pr_set != 2 and i == 0:
                    continue
                for item in itemset:
                    if isinstance(item, int):
                        if item not in visited:
                            item_counts[item] += 1
                            visited.add(item)
                    else:
                        for s_item in item:
                            if s_item not in visited:
                                item_counts[s_item] += 1
                                visited.add(s_item)
        
        return {k: v for k, v in item_counts.items() if v >= PrefixSpan.minsup}

    def _calculate_frequent_items_set(data, prev_set):
        item_counts = defaultdict(int)
        for sequence in data:
            visited = SortedSet()
            if not sequence:
                continue
            for item in sequence[0]:
                item_counts[item] += 1
                visited.add(item)
                # continue
            for itemset in sequence:
                if prev_set.issubset(itemset):
                    for s_item in itemset:
                        if s_item not in prev_set and s_item not in visited:
                            item_counts[s_item] += 1
                            visited.add(s_item)
        
        return {k: v for k, v in item_counts.items() if v >= PrefixSpan.minsup}

    def _project(data, item, pr_set):
        projected_data = []
        for sequence in data:
            for idx, itemset in enumerate(sequence):
                if pr_set != 2 and idx == 0:
                    continue
                if item in itemset:
                    new_sequence = sequence[idx:]
                    new_sequence[0] = itemset.difference({item})
                    # if not new_sequence[0]:
                    #     new_sequence.pop(0)
                    projected_data.append(new_sequence)
                    break
        return projected_data

    def _project_set(data, item, prev_set):
        projected_data = []
        for sequence in data:
            idx = 0
            if not sequence:
                continue
            itemset = sequence[0]
            if item in itemset:
                new_sequence = sequence[idx:]
                new_sequence[0] = itemset.difference({item})
                # if not new_sequence[0]:
                #     new_sequence.pop(0)
                projected_data.append(new_sequence)
                continue
            for idx, itemset in enumerate(sequence):
                if item in itemset and prev_set.issubset(itemset):
                    new_sequence = sequence[idx:]
                    new_sequence[0] = itemset.difference({item})
                    # if not new_sequence[0]:
                    #     new_sequence.pop(0)
                    projected_data.append(new_sequence)
                    break
        return projected_data

    def _prefix_span(data, prefix, pr_set):
        # print(prefix)
        # print(data)
        # print()
        if prefix[0]:
            frequent_items = PrefixSpan._calculate_frequent_items(data, pr_set)
            for item, support in frequent_items.items():
                new_prefix = copy.deepcopy(prefix)
                new_prefix.append(SortedSet({item}))
                PrefixSpan.patterns[str(new_prefix)] = support
                projected_data = PrefixSpan._project(data, item, pr_set)
                PrefixSpan._prefix_span(projected_data, new_prefix, 0)
            
        if not prefix:
            return

        frequent_items = PrefixSpan._calculate_frequent_items_set(data, prefix[-1])
        for item, support in frequent_items.items():
            new_prefix = copy.deepcopy(prefix)
            new_prefix[-1].add(item)

            if str(new_prefix) in PrefixSpan.patterns:
                continue

            PrefixSpan.patterns[str(new_prefix)] = support
            projected_data = PrefixSpan._project_set(data, item, prefix[-1])
            PrefixSpan._prefix_span(projected_data, new_prefix, 1)

    def run(data, minsup):
        PrefixSpan.patterns = dict()
        PrefixSpan.minsup = minsup
        PrefixSpan._prefix_span(data, [SortedSet(), ], 2)
        print("Prefix Span: Number of frequent sequences: " + str(len(PrefixSpan.patterns)))
    
# PrefixSpan.run([
    
# ], )

# with open("prefix.txt", 'w') as file:
#     for pattern in PrefixSpan.patterns:
#         file.write(str(pattern) + "\n")
# print(len(PrefixSpan.patterns))