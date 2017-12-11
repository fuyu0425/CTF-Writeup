import sys
plain_text = "POR4dnyTLHBfwbxAAZhe}}ocZR3Cxcftw9"
target = "SECCON{**************************}"
key = "**************"
ans = ''
print('plain_text length is ', len(plain_text))
print('target length is ', len(target))
print('key length is ', len(key))

def _l(idx, s):
    return s[idx:] + s[:idx]

s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz_{}"
t = [[_l((i+j) % len(s), s) for j in range(len(s))] for i in range(len(s))]


def main(p, k1, k2):
    i1 = 0
    i2 = 0
    c = ""
    for a in p:
        c += t[s.find(a)][s.find(k1[i1])][s.find(k2[i2])]
        i1 = (i1 + 1) % len(k1)
        i2 = (i2 + 1) % len(k2)
    return c
def printAns(ans):
    ans2=ans[::-1]
    i1=0
    i2=0
    raw =''
    for _ in plain_text:
        for i in s:
            if t[s.find(i)][ans[i1]][ans2[i2]]== _:
                raw+=i
        i1 =(i1+1)%14
        i2=(i2+1)%14
    print(raw)

def test():

    ans = [0]* 14
    for test0 in range(0, len(s)):
        for test13 in range(0, len(s)):
            if t[s.find('S')][test0][test13] != plain_text[0]:
                continue
            t[s.find('S')][test0][test13]
            ans[0] = test0
            ans[13] = test13
            for test1 in range(0, len(s)):
                for test12 in range(0, len(s)):
                    if t[s.find('E')][test1][test12] != plain_text[1]:
                        continue
                    ans[1] = test1
                    ans[12] = test12
                    for test2 in range(0, len(s)):
                        for test11 in range(0, len(s)):
                            if t[s.find('C')][test2][test11] != plain_text[2]:
                                        continue
                            ans[2] = test2
                            ans[11] = test11
                            for test3 in range(0, len(s)):
                                for test10 in range(0, len(s)):
                                    if t[s.find('C')][test3][test10] != plain_text[3]:
                                        continue
                                    ans[3] = test3
                                    ans[10] = test10
                                    for test4 in range(0, len(s)):
                                        for test9 in range(0, len(s)):
                                            if t[s.find('O')][test4][test9] != plain_text[4]:
                                                continue
                                            ans[4] = test4
                                            ans[9] = test9
                                            for test5 in range(0, len(s)):
                                                for test8 in range(0, len(s)):
                                                    if t[s.find('N')][test5][test8] != plain_text[5]:
                                                        continue
                                                    elif t[s.find('}')][test5][test8] != '9':
                                                        continue
                                                    ans[5] = test5
                                                    ans[8] = test8
                                                    for test6 in range(0, len(s)):
                                                        for test7 in range(0, len(s)):
                                                            if t[s.find('{')][test6][test7] != plain_text[6]:
                                                                continue
                                                            ans[6] = test6
                                                            ans[7] = test7
                                                            printAns(ans)


if __name__ == '__main__':
    test()
    pass
