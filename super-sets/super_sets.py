
def P(s):

    result = [""]
    # for i in range(len(s)):
    for elem in s:
        result_to_append = []
        for res_elem in result:
            # if elem not in result:
            result_to_append += [res_elem + elem]
        result += result_to_append

    return result


print(P(['a','b']))