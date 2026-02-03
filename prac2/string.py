# 1
n = int(input())
f = {}
for i in range(1, n + 1):
    s = input().strip()
    if s not in f:
        f[s] = i

for s in sorted(f):
    print(s, f[s])

# 2
import sys
n = int(sys.stdin.readline())
doc = {}
for i in range(n):
    p = sys.stdin.readline().split()
    if p[0] == "set":
        doc[p[1]] = p[2]
    else: 
        key = p[1]
        if key in doc:
            print(doc[key])
        else:
            print("KE: no key " + key + " found in the document")