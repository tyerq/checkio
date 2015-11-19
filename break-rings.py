__author__ = 'tyerq'

def break_rings(rings):

    ring_conns = {}
    for conn in rings:
        if conn[0] in ring_conns:
            ring_conns[conn[0]].add(conn[1])
        else:
            ring_conns[conn[0]] = [conn[1]]
        if conn[1] in ring_conns:
            ring_conns[conn[1]].add(conn[0])
        else:
            ring_conns[conn[1]] = [conn[0]]



    return 1

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert break_rings(({1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {4, 6})) == 3, "example"
    assert break_rings(({1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4})) == 3, "All to all"
    assert break_rings(({5, 6}, {4, 5}, {3, 4}, {3, 2}, {2, 1}, {1, 6})) == 3, "Chain"
    assert break_rings(({8, 9}, {1, 9}, {1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}, {6, 7}, {8, 7})) == 5, "Long chain"

