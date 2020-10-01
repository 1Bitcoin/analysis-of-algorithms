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

def RecursionLevenshteinMatrix(string1, string2, matrix):
    if (string1 == "" or string2 == ""):
        return abs(len(string1) - len(string2))

    forfeit = 0 if (string1[-1] == string2[-1]) else 1

    value = min(RecursionLevenshteinMatrix(string1, string2[:-1], matrix) + 1,
               RecursionLevenshteinMatrix(string1[:-1], string2, matrix) + 1,
               RecursionLevenshteinMatrix(string1[:-1], string2[:-1], matrix) + forfeit)

    matrix[len(string1)][len(string2)] = value;

    return value;


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

def DamerauLevenshteinMatrix(string1, string2):
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

            if ((i > 1 and j > 1) and string1[i - 1] == string2[j - 2] and string1[i - 2] == string2[j - 1]):
                table[i][j] = min(table[i][j], table[i - 2][j - 2] + 1)

    OutputTable(table, string1, string2)

    return print(table[-1][-1])


string1 = "cat"
string2 = "act"

len_i = len(string1) + 1 if len(string1) > len(string2) else len(string2) + 1
len_j = len(string2) + 1 if len(string2) > len(string1) else len(string1) + 1

matrix = [[0 for j in range(len_j)] for i in range(len_i)]

#print(RecursionLevenshteinMatrix(string1, string2, matrix))
#LevenshteinMatrix(string1, string2)

DamerauLevenshteinMatrix(string1, string2)