def get_lcs(string1, string2):
    lcs_list = []
    for i in range(len(string1)):
        flag = 0
        lcs = ''
        for j in range(i, len(string1)):
            for k in range(flag, len(string2)):
                if string1[j] == string2[k]:
                    lcs += string1[j]
                    flag = k + 1
                    break
        lcs_list.append((len(lcs), lcs))
    print(len(lcs_list))
    return sorted(lcs_list, reverse = True)

def longestCommonSubsequence(X: str, Y: str) -> int:
    m = len(X)
    n = len(Y)
    L = [[None] * (n + 1) for i in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    return L[m][n]

if __name__ == '__main__':
    lcs_list = get_lcs("abcdjio7890bhsdjknyewhbnvd", "djio78347bvfdjbnknyew")
    print(lcs_list)
    print(longestCommonSubsequence("abcdjio7890bhsdjknyewhbnvd", "djio78347bvfdjbnknyew"))