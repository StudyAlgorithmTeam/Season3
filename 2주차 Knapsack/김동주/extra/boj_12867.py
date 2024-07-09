# N차원 여행


MAX_M = 50

N = int(input())
M = int(input())
indicies = list(map(int, input().split()))
steps = [(1 if c == '+' else -1) for c in input().strip()]

hash_index = {
    idx: i
    for i, idx in enumerate(set(indicies))
}

try:
    vector_history = [[0] * M]
    for i in range(M):
        vector = vector_history[-1].copy()
        idx = hash_index[indicies[i]]
        vector[idx] = vector_history[-1][idx] + steps[i]
        # 해당 vector를 이미 방문한 적 있는지 검사
        for j in range(i):
            if vector_history[j] == vector:
                raise ValueError
        vector_history.append(vector)
except ValueError:
    print(0)
else:
    print(1)
