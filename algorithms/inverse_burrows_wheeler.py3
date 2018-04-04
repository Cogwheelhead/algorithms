from itertools import count


def unzip(zipped):
    return zip(*zipped)


def inverse_bwt(bwt_string):
    first_col, mapping = unzip(sorted(zip(bwt_string, count())))

    result, curr_symbol_num = [], 0
    while curr_symbol_num or not result:
        curr_symbol_num = mapping[curr_symbol_num]
        result.append(first_col[curr_symbol_num])

    return ''.join(result)