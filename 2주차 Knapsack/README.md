## 숙제

| 난이도 | 번호 | 제목 | 링크                  |
| ------ | ---- | ---- | --------------------- |
| ![S2]  | 1535 | 안녕 | <https://boj.kr/1535> |
| ![G4]  | 1106 | 호텔 | <https://boj.kr/1106> |

## 스터디 진행 중 풀이

| 난이도 | 번호 | 제목 | 링크                  |
| ------ | ---- | ---- | --------------------- |
| ![S2]  | 1535 | 안녕 | <https://boj.kr/1535> |

## 스터디 내용

### 동적 프로그래밍 (Dynamic Programming, DP)

-   점화식/함수를 설계하는 것이 포인트이다.
-   함수의 [멱등성](https://ko.wikipedia.org/wiki/멱등법칙)이 보장된다면 메모이제이션 기법으로 연산량을 비약적으로 줄일 수 있다.
    -   예) 피보나치 수
        -   일반적인 접근: $O(2^N)$
        -   메모이제이션을 이용한 DP 접근: $O(N)$

### DP를 이용한 [안녕](https://boj.kr/1535) 풀이.

#### 점화식을 세우는 경우

> 생명력이 $l$만큼 남았을 때, $i$번째 사람부터 $N$번째 사람까지 인사를 할지 말지 선택해가며 얻을 수 있는 최대 행복의 양

```math
\text{maxjoy}(i, l) = \begin{cases}
    -\infty, & \text{if } l \leq 0 \\
    0, & \text{if } l \gt 0 \text{ and } i = N \\
    \max \begin{cases}
        \text{maxjoy}(i+1, l) \\
        \text{maxjoy}(i+1, l-L_i)+J_i)
    \end{cases}, & \text{otherwise}
\end{cases}
```

문제의 조건:

-   $N \leq 20$
-   $i \leq N$
-   $1 \leq l \leq 100$

시간 복잡도:

-   $T(n) = 2T(n-1) + O(1)$
-   $O(2^N)$

#### 메모이제이션을 이용하는 경우

동일한 입력에 대한 반환을 캐시하여 사용한다.
이 때, 최악의 공간복잡도는 모든 입력 쌍의 개수와 비례하며,
시간 복잡도는 각 입력 쌍에 대해 1번 계산하고 이후로는 캐시된 값만 사용하므로 이 또한 입력 쌍의 개수와 비례한다.

입력 쌍의 개수($i$, $l$ 쌍의 경우의 수)

-   $\max i \times \max l = N \times 100$

공간 복잡도(메모이제이션에 필요한 것만):

-   $O(\max i \times \max l) = O(100N) = O(N)$

시간 복잡도:

-   $T(n) = (\max i \times \max l) \times O(1)$
-   $O(100N) = O(N)$

### DP를 이용한 [호텔](https://boj.kr/1106) 풀이.

$1$번 도시부터 $N$번 도시까지 총 $N$개의 도시가 있고,
$i$번 도시에서 홍보할 때 대는 비용이 $W_i$, 그 비용으로 얻을 수 있는 고객의 수가 $V_i$라고 하자.

적어도 $C$ 명 이상의 고객을 확보하기 위해 투자해야 하는 비용의 최솟값을 $f(C)$라고 하면, 다음의 점화식을 세울 수 있다:

$$
f(C) = \begin{cases}
    0, & \text{if } c \leq 0 \\
    \min_{1 \leq i \leq N}({ f(C - W_i) + V_i }), & \text{otherwise}
\end{cases}
$$

-   한 번 투자했던 도시에 다시 투자하는 것이 가능하다.
-   적어도 $C$명을 확보하는 것이므로, 그 이상의 숫자의 고객을 확보해도 된다.

#### 시간 복잡도

-   메모이제이션 없이 수행한다면, 최악의 경우 : $O(N^C)$
-   그럼 메모이제이션을 한다면 시간 복잡도는 어떻게 될까?

## 찾아온 문제들

#### 김동주

| 난이도 | 번호 | 제목        | 링크                  | 비고 |
| ------ | ---- | ----------- | --------------------- | ---- |
| ![S1]  | 1149 | RGB거리     | <https://boj.kr/1149> | #dp  |
| ![G4]  | 2133 | 타일 채우기 | <https://boj.kr/2133> | #dp  |

#### 정우현

| 난이도 | 번호  | 제목   | 링크                   | 비고                    |
| ------ | ----- | ------ | ---------------------- | ----------------------- |
| ![S1]  | 16113 | 시그널 | <https://boj.kr/16113> | #string #implementation |

#### 서동혁

| 난이도 | 번호 | 제목          | 링크                  | 비고                          |
| ------ | ---- | ------------- | --------------------- | ----------------------------- |
| ![G4]  | 1715 | 카드 정렬하기 | <https://boj.kr/1715> | #greedy #priority_queue(heap) |

#### 손영준

| 난이도 | 번호 | 제목 | 링크               |
| ------ | ---- | ---- | ------------------ |
| ![??]  | -    | -    | <https://boj.kr/-> |

#### 권동균

| 난이도 | 번호  | 제목      | 링크                   | 비고      |
| ------ | ----- | --------- | ---------------------- | --------- |
| ![S2]  | 1260  | DFS와 BFS | <https://boj.kr/1260>  | #bfs #dfs |
| ![G5]  | 10026 | 적록색약  | <https://boj.kr/10026> | #bfs      |

#### 박준석

| 난이도 | 번호 | 제목 | 링크                  | 비고                 |
| ------ | ---- | ---- | --------------------- | -------------------- |
| ![S1]  | 2002 | 추월 | <https://boj.kr/2002> | #queue #hashing #set |

#### 양효인

| 난이도 | 번호  | 제목       | 링크                   | 비고                             |
| ------ | ----- | ---------- | ---------------------- | -------------------------------- |
| ![S2]  | 12867 | n차원 여행 | <https://boj.kr/12867> | #hashing #coordinate_compression |

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
