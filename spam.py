# import bitmap as bm
import copy
from sortedcontainers import SortedSet

class Spam:
    verticalDB = dict()
    last_bit_index = 0
    sequence_size = list()
    frequent_items = list()
    dataset = list()
    frequent_sups = list()

    def run(dataset, minsup):
        Spam.verticalDB = dict()
        Spam.last_bit_index = 0
        Spam.sequence_size = list()
        Spam.frequent_items = list()
        Spam.dataset = dataset
        Spam.frequent_sups = list()

        # Registering blocks of tids in cids
        for transaction in dataset:
            Spam.sequence_size.append(Spam.last_bit_index)
            Spam.last_bit_index += len(transaction)
        # Spam.last_bit_index -= 1

        # Creating Bitmap Representation of the dataset
        for cid in range(0, len(dataset)):
            for tid in range(0, len(dataset[cid])):
                if isinstance(dataset[cid][tid], int):
                    item = dataset[cid][tid]
                    if item not in Spam.verticalDB:
                        Spam.verticalDB[item] = 0 # bm.BitMap(Spam.last_bit_index)
                    Spam.verticalDB[item] |= 1 << Spam.sequence_size[cid] + tid
                else:
                    for item in dataset[cid][tid]:
                        if item not in Spam.verticalDB:
                            Spam.verticalDB[item] = 0 # bm.BitMap(Spam.last_bit_index)
                        Spam.verticalDB[item] |= 1 << Spam.sequence_size[cid] + tid

        # Spam.verticalDB = dict(sorted(Spam.verticalDB.items()))
        
        # Adding frequent items to the list
        frequent_items = list()
        for key, value in Spam.verticalDB.items():
            sup = 0
            for cid in range(0, len(Spam.dataset)):
                flag = False
                for tid in range(0, len(Spam.dataset[cid])):
                    if value & 1 << (Spam.sequence_size[cid] + tid) != 0:
                        flag = True
                
                if flag:
                    sup += 1
            
            if sup < minsup:
                continue
            frequent_items.append(key)
            Spam.frequent_items.append(str(key))
        
        for key, value in Spam.verticalDB.items():
            prefix = list()
            tmp = SortedSet()
            tmp.add(key)
            prefix.append(tmp)
            Spam.dfs_pruning(prefix, value, frequent_items, frequent_items, key, 2, minsup)
        
        print("SPAM: Number of frequent sequences: " + str(len(Spam.frequent_items)))

    def dfs_pruning(prefix, prefix_bitmap, s_n, i_n, i_step_check, size, minsup):
        s_temp, i_temp = list(), list()
        s_bitmaps, i_bitmaps = list(), list()

        # S-step
        for i in s_n:
            new_bitmap = prefix_bitmap # bm.BitMap.fromstring(prefix_bitmap.tostring())
            sup = 0
            for cid in range(0, len(Spam.dataset)):
                k = False
                flag = False
                for tid in range(0, len(Spam.dataset[cid])):
                    if not k:
                        if prefix_bitmap & 1 << (Spam.sequence_size[cid] + tid):
                            k = True
                        new_bitmap &= ~ (1 << (Spam.sequence_size[cid] + tid))
                        continue
                    if Spam.verticalDB[i] & 1 << (Spam.sequence_size[cid] + tid):
                        flag = True
                        new_bitmap |= 1 << (Spam.sequence_size[cid] + tid)
                    else:
                        new_bitmap &= ~ (1 << (Spam.sequence_size[cid] + tid))
                
                if flag:
                    sup += 1
            
            if sup >= minsup:
                s_temp.append(i)
                s_bitmaps.append(new_bitmap)

        for i in range(0, len(s_temp)):
            new_prefix = copy.deepcopy(prefix)
            tmp = SortedSet()
            tmp.add(s_temp[i])
            new_prefix.append(tmp)
            Spam.frequent_items.append(str(new_prefix))
            Spam.dfs_pruning(new_prefix, s_bitmaps[i], s_temp, s_temp, s_temp[i], size + 1, minsup)

        # I-step
        for i in i_n:
            if i <= i_step_check:
                continue
            new_bitmap = prefix_bitmap # bm.BitMap.fromstring(prefix_bitmap.tostring())
            sup = 0
            for cid in range(0, len(Spam.dataset)):
                flag = False
                for tid in range(0, len(Spam.dataset[cid])):
                    if not prefix_bitmap & 1 << (Spam.sequence_size[cid] + tid) != 0:
                        new_bitmap &= ~ (1 << (Spam.sequence_size[cid] + tid))
                        continue
                    if Spam.verticalDB[i] & 1 << (Spam.sequence_size[cid] + tid) != 0:
                        new_bitmap |= 1 << (Spam.sequence_size[cid] + tid)
                        flag = True
                    else:
                        new_bitmap &= ~ (1 << (Spam.sequence_size[cid] + tid))
                        continue
                
                if flag:
                    sup += 1
            
            if sup >= minsup:
                i_temp.append(i)
                i_bitmaps.append(new_bitmap)

        for i in range(0, len(i_temp)):
            new_prefix = copy.deepcopy(prefix)
            new_prefix[-1].add(i_temp[i])
            Spam.frequent_items.append(str(new_prefix))
            Spam.dfs_pruning(new_prefix, i_bitmaps[i], s_temp, i_temp, i_temp[i], size + 1, minsup)

# Spam.run([
    
# ], )

# with open("spam.txt", 'w') as file:
#     for pattern in Spam.frequent_items:
#         file.write(str(pattern) + "\n")
# print(len(Spam.frequent_items))