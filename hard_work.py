# condition: https://codeforces.com/problemset/problem/61/B?locale=ru
import re


def alpha(x):
    return ''.join([i for i in x if i.isalpha()])


w1, w2, w3 = alpha(input().lower()), alpha(input().lower()), alpha(input().lower())
r = r'(%s)|(%s)|(%s)' % (w1, w2, w3)
for i in range(int(input())):
    a = alpha(input()).lower()
    print('WA' if re.sub(r, '', a) else 'ACC')



