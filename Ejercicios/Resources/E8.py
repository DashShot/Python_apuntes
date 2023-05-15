def my_zip(*args):
    min_length = min(len(seq) for seq in args)
    zipped_list = []
    for i in range(min_length):
        tup = tuple(seq[i] for seq in args)
        zipped_list.append(tup)
    return zipped_list


print(my_zip([10, 20, 30], 'abc'))