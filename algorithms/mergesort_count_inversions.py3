def count_merge(lst1, lst2):
    n_inversions, result = 0, []
    while lst1 and lst2:
        a, b = lst1[0], lst2[0]
        if a <= b:
            res.append(lst1.pop(0))
        else:
            res.append(lst2.pop(0))
            n_inversions += len(lst1)
    result.extend(lst1 + lst2)
    return result, n_inversions


def count_inversions_merge_sort(lst):
    m = len(lst) // 2
    if not m:
        return(lst, 0)
    part_a, left_inversions = count_inversions_merge_sort(lst[:m])
    part_b, right_inversions = count_inversions_merge_sort(lst[m:])
    whole_thing, cross_inversions = count_merge(part_a, part_b)
    return whole_thing, left_inversions + right_inversions + cross_inversions