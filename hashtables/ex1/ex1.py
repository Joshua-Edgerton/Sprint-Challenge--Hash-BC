#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # For each item in the range of the input length
    # "i" will be used to loop through array
    for i in range(length):
        print("Step 1 - Each item within the length ->", i)
        # Use the insert function
        # Inserting into the hash table the input weights
        # Insert function takes paramaters of hashtable/key/value
        hash_table_insert(ht, weights[i], i)
        # Index gets its value from the retrieve function
        # Grabbing the weight limit minus the weight of each package for the key
        # Retrieve function takes hashtable/key
        index = hash_table_retrieve(ht, (limit - weights[i]))
        print("Step 2 - Index value after retrieve function ->", index)
        # 2nd Index gets its value
        second_index = weights.index(weights[i])
        print("Step 3 - Second_index value ->", second_index)
        # If index exists and it is not equal to the 2nd index
        if index is not None and index != second_index:
            # Then if that 2nd index is greater than the first index
            if second_index > index:
                # Return the 2nd index first
                return (second_index, index)
            else:
                # Otherwise returns the first index first
                return (index, second_index)


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

print(get_indices_of_item_weights([4, 4], 2, 8))