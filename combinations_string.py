def combiner(charset, length, prefix=''):
    if length == 0:
        print(prefix)
        return
    for i in charset:
        newprefix = prefix + i
        combiner(charset, length-1, newprefix)

def no_rep_combiner(charset, length, prefix=''):
    if length == 0:
        print(prefix)
    for i in charset:
        if i not in prefix:
            newprefix = prefix + i
            no_rep_combiner(charset, length-1, newprefix)

def combinations_without_permutation(charset):
    for j in range(len(charset), 0, -1):
        no_rep_combiner(charset, j)
