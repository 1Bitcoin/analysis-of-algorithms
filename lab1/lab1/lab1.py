def LevenshteinRecursion(string1, string2):
    if (string1 == "" or string2 == ""):
        return abs(len(string1) - len(string2))

    forfeit = 0 if (string1[-1] == string2[-1]) else 1

    return min(LevenshteinRecursion(string1, string2[:-1]) + 1,
               LevenshteinRecursion(string1[:-1], string2) + 1,
               LevenshteinRecursion(string1[:-1], string2[:-1]) + forfeit)

#print(LevenshteinRecursion("tac", "scat"))

def LevenshteinMatrix(string1, string2):
    len_i = len(string1) + 1
    len_j = len(string2) + 1

    table = [[i + j for j in range(len_j)] for i in range(len_i)]

    OutputTable(table, string1, string2)


    for i in range(1, len_i):
        for j in range(1, len_j):
            forfeit = 0 if (string1[i - 1] == string2[j - 1]) else 1

            table[i][j] = min(table[i - 1][j] + 1,
                              table[i][j - 1] + 1,
                              table[i - 1][j - 1] + forfeit)

    OutputTable(table, string1, string2)

    return (table[-1][-1])

def OutputTable(table, str1, str2):
    print("\n   ", end = " ")
    for i in str2:
        print(i, end = " ")

    for i in range(len(table)):
        if i:
            print("\n" + str1[i-1], end = " ")
        else:
            print("\n ", end = " ")
        for j in range(len(table[i])):
            print(table[i][j], end = " ")
    print("\n")

LevenshteinMatrix("cat", "scat")
