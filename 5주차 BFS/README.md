## 숙제

| 난이도 | 번호  | 제목                             | 링크                   |
| ------ | ----- | -------------------------------- | ---------------------- |
| ![S2]  | 24447 | 알고리즘 수업 - 너비 우선 탐색 4 | <https://boj.kr/24447> |
| ![G5]  | 10026 | 적록색약                         | <https://boj.kr/10026> |

## 스터디 진행 중 풀

| 난이도 | 번호  | 제목                             | 링크                   |
| ------ | ----- | -------------------------------- | ---------------------- |
| ![S2]  | 24447 | 알고리즘 수업 - 너비 우선 탐색 4 | <https://boj.kr/24447> |

## 스터디 내용

-   스터디 진행 방식 변경
    -   차주부터는 7문제 중 각자 하나 씩 골라서 풀이하는 것으로 변경
    -   매 주 4명씩 풀어온 코드와 알고리즘 및 시간복잡도 분석을 발표함
-   BFS의 시간 복잡도 및 BFS 예제 코드 설명

시간복잡도: $O(V+E)$

```python
from collections import deque, defaultdict


V = 10 # 정점의 개수 (0 ~ V-1 번 정점이 있음)
R = 1 # 시작 노드

E = defaultdict(list)
q = deque()
visited = [False] * V

for i in range(M):
    # cin >> u >> v;
    u,v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)

visited[R] = True
q.append(R)

depth = 0
n_visited = 1
while q:
    width = len(q)
    for _ in range(width):
        u = q.popleft()
        print(width, depth)  # 지금 보고있는 큐의 너비와 깊이
        # 방문한다.
        for v in E[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
                n_visited += 1
    depth += 1
```

## 찾아온 문제들

### 김동주

| 난이도 | 번호 | 제목   | 링크                  | 선정 이유                             |
| ------ | ---- | ------ | --------------------- | ------------------------------------- |
| ![S2]  | 2512 | 예산   | <https://boj.kr/2512> | #parametric_search #hamilton_distance |
| ![G4]  | 8983 | 사냥꾼 | <https://boj.kr/8983> | #bisection #sorting #mathematics      |

### 정우현

| 난이도 | 번호     | 제목 | 링크                      | 선정 이유 |
| ------ | -------- | ---- | ------------------------- | --------- |
| ![??]  | 문제번호 | -    | <https://boj.kr/문제번호> |           |

### 서동혁

| 난이도 | 번호     | 제목 | 링크                      | 선정 이유 |
| ------ | -------- | ---- | ------------------------- | --------- |
| ![??]  | 문제번호 | -    | <https://boj.kr/문제번호> |           |

### 손영준

| 난이도 | 번호     | 제목 | 링크                      | 선정 이유 |
| ------ | -------- | ---- | ------------------------- | --------- |
| ![??]  | 문제번호 | -    | <https://boj.kr/문제번호> |           |

### 권동균

| 난이도 | 번호     | 제목 | 링크                      | 선정 이유 |
| ------ | -------- | ---- | ------------------------- | --------- |
| ![??]  | 문제번호 | -    | <https://boj.kr/문제번호> |           |

### 박준석

| 난이도 | 번호     | 제목 | 링크                      | 선정 이유 |
| ------ | -------- | ---- | ------------------------- | --------- |
| ![G5]  | 1052 | 물병 | <https://boj.kr/1052> |  해결 방안 찾기 위해 꽤 오래 고민해야했고 개인적으로 참신한 느낌이었음 비트마스킹?신기함  |
| ![S2]  | 10654 | 랜선자르기 | <https://boj.kr/1654> |  이진 탐색 연습에 좋아보임 옛날부터 계속 시도했다가 실패했는데 드디어 해결해서 행복함  |

### 양효인

| 난이도 | 번호     | 제목 | 링크                      | 선정 이유 |
| ------ | -------- | ---- | ------------------------- | --------- |
| ![??]  | 문제번호 | -    | <https://boj.kr/문제번호> |           |

<!-- solved.ac 문제 난이도 별 태그 이미지 -->

[P1]: https://d2gd6pc034wcta.cloudfront.net/tier/20.svg
[P2]: https://d2gd6pc034wcta.cloudfront.net/tier/19.svg
[P3]: https://d2gd6pc034wcta.cloudfront.net/tier/18.svg
[P4]: https://d2gd6pc034wcta.cloudfront.net/tier/17.svg
[P5]: https://d2gd6pc034wcta.cloudfront.net/tier/16.svg
[G1]: https://d2gd6pc034wcta.cloudfront.net/tier/15.svg
[G2]: https://d2gd6pc034wcta.cloudfront.net/tier/14.svg
[G3]: https://d2gd6pc034wcta.cloudfront.net/tier/13.svg
[G4]: https://d2gd6pc034wcta.cloudfront.net/tier/12.svg
[G5]: https://d2gd6pc034wcta.cloudfront.net/tier/11.svg
[S1]: https://d2gd6pc034wcta.cloudfront.net/tier/10.svg
[S2]: https://d2gd6pc034wcta.cloudfront.net/tier/9.svg
[S3]: https://d2gd6pc034wcta.cloudfront.net/tier/8.svg
[S4]: https://d2gd6pc034wcta.cloudfront.net/tier/7.svg
[S5]: https://d2gd6pc034wcta.cloudfront.net/tier/6.svg
[??]: https://d2gd6pc034wcta.cloudfront.net/tier/0.svg
