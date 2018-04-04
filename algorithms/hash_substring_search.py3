x, p = 31, 2**31 - 1


def hashcode(string):
    result = 0
    for s in string:
        result = (result * x + ord(s)) % p
    return result


def find(needle, haystack):
    needle_hash = hashcode(needle)
    exp = pow(x, len(needle), p)
    hashes = [hashcode(haystack[:len(needle)])]
    
    for left_char, right_char in zip(haystack, haystack[len(needle):]):
        hashes.append((hashes[-1]*x + ord(right_char) - ord(left_char)*exp) % p)
        
    return (i for i, curr_hash in enumerate(hashes) 
            if curr_hash == needle_hash and haystack.startswith(needle, i))