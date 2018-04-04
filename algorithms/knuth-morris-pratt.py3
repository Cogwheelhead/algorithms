def prefix_function(text):
    pf = [0]
    for i, curr_symbol in enumerate(text[1:], start=1):
        curr_border_len = pf[i - 1]
        while curr_border_len and text[curr_border_len] != curr_symbol:
            curr_border_len = pf[curr_border_len - 1]
        pf.append(curr_border_len + (text[curr_border_len] == curr_symbol))
    return pf


def find(needle, haystack):
    text = f'{needle}${haystack}'
    pf = prefix_function(text)

    return [i - 2*len(needle) for i in range(len(needle) + 1, len(text))
            if pf[i] == len(needle)]