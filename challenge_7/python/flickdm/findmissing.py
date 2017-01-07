
def find_missing(pattern):
    if list is None:
        return -1

    pattern_total = 0
    pattern_len = len(pattern)

    for i in range(pattern_len):
        pattern_total += pattern[i]

    # Summation
    actual_total = pattern_len * (pattern_len + 1) / 2


    return (actual_total - pattern_total)
