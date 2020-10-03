import time

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

    #OutputTable(table, string1, string2)

    for i in range(1, len_i):
        for j in range(1, len_j):
            forfeit = 0 if (string1[i - 1] == string2[j - 1]) else 1

            table[i][j] = min(table[i - 1][j] + 1,
                              table[i][j - 1] + 1,
                              table[i - 1][j - 1] + forfeit)

    #OutputTable(table, string1, string2)

    return (table[-1][-1])

def GetRecursionLevenshteinMatrix(string1, string2):
    len_i = len(string1)
    len_j = len(string2)
    
    matrix = [[-1 for j in range(len_j + 1)] for i in range(len_i + 1)]

    return RecursionLevenshteinMatrix(string1, len_i, string2, len_j, matrix)


def RecursionLevenshteinMatrix(string1, i, string2, j, matrix):
    if (i == 0):
        matrix[i][j] = j
    elif (j == 0):
        matrix[i][j] = i
    else:
        if (matrix[i][j - 1] == -1):
           matrix[i][j - 1] = RecursionLevenshteinMatrix(string1, i, string2, j - 1, matrix)

        if (matrix[i - 1][j] == -1):
            matrix[i - 1][j] = RecursionLevenshteinMatrix(string1, i - 1, string2, j, matrix)

        if (matrix[i - 1][j - 1] == -1):
           matrix[i - 1][j - 1] = RecursionLevenshteinMatrix(string1, i - 1, string2, j - 1, matrix)

        forfeit = 0 if (string1[i - 1] == string2[j - 1]) else 1
        matrix[i][j] = min(min(matrix[i][j - 1], matrix[i - 1][j]) + 1, matrix[i - 1][j - 1] + forfeit)

    return matrix[i][j];


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

    #OutputTable(table, string1, string2)

    for i in range(1, len_i):
        for j in range(1, len_j):
            forfeit = 0 if (string1[i - 1] == string2[j - 1]) else 1

            table[i][j] = min(table[i - 1][j] + 1,
                              table[i][j - 1] + 1,
                              table[i - 1][j - 1] + forfeit)

            if ((i > 1 and j > 1) and string1[i - 1] == string2[j - 2] and string1[i - 2] == string2[j - 1]):
                table[i][j] = min(table[i][j], table[i - 2][j - 2] + 1)

    #OutputTable(table, string1, string2)

    return print(table[-1][-1])


string1 = "n"
string2 = "j"

t = time.time_ns()
print(LevenshteinMatrix(string1, string2))
end = time.time_ns()
print(end - t)

#print(GetRecursionLevenshteinMatrix(string1, string2))
#print(LevenshteinMatrix(string1, string2))
#print(DamerauLevenshteinMatrix(string1, string2))
