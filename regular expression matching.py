class Solution:
     def isMatch(self, s, p):
        T = [[True] + [False]*len(p)] + [[False]*(len(p)+1) for _ in range(len(s))]
        s, p = ' ' + s, ' ' + p
        for i in range(len(T)):
            for j in range(1, len(T[0])):
                if p[j] == '*':
                    if i == 0 or T[i][j-2]: 
                        T[i][j] = T[i][j-2]
                    elif i > 0 and (s[i] == p[j-1] or p[j-1] == '.'):
                        T[i][j] = T[i-1][j]
                elif i > 0 and (s[i] == p[j] or p[j] == '.'): 
                    T[i][j] = T[i-1][j-1]
        return T[-1][-1]
