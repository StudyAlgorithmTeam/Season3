# NN

import sys


N, M = input().split()

for i in range(min(int(N)*len(N), int(M))):
    sys.stdout.write(N[i % len(N)])
