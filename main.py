import random
import time


def union(a, b):
    root_a = root(a)
    root_b = root(b)
    if not root_a == root_b:  # not already connected
        if tree_size[root_a] > tree_size[root_b]:
            tree_size[root_a] += tree_size[root_b]
            ids[root_b] = root_a
        else:
            tree_size[root_b] += tree_size[root_a]
            ids[root_a] = root_b


def connected(a, b):
    return root(a) == root(b)


def root(a):
    while a != ids[a]:
        ids[a] = ids[ids[a]]
        a = ids[a]
    return a


def rand_node(number_of_elements):
    return int(random.random() * number_of_elements)


total_nodes = 1000
ids = [i for i in range(total_nodes)]
tree_size = [1] * total_nodes
