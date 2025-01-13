import random

class Dataset:
    def generate(num_sequences, max_sequence_length, num_items):
        # Generate random sequences of items and itemsets
        sequences = []
        for i in range(num_sequences):
            seq = []
            sequence_length = 0
            while sequence_length < max_sequence_length:
                # Generate an itemset
                itemset_size = random.randint(1, min(num_items, max_sequence_length - sequence_length))
                itemset = set(random.sample(range(1, num_items + 1), itemset_size))
                seq.append(itemset)
                sequence_length += itemset_size
            sequences.append(seq)

        return sequences