def angerams(array):
    h_table = {}
    for i in array:
        i_sorted = "".join(sorted(i))
        if i_sorted not in h_table:
            h_table[i_sorted] = [i]
        else:
            h_table[i_sorted].append(i)

    output = []
    for key in h_table:
        output.append(h_table[key])
    return output


array =  ["eat", "tea", "tan", "ate", "nat", "bat"]
print(angerams(array))
