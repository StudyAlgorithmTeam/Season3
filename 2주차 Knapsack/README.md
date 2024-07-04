> [마크다운 사용법 - 참고 링크](https://gist.github.com/ihoneymon/652be052a0727ad59601)

<!-- 문제 템플릿

| 난이도 | 번호 | 제목 | 링크               |
| ------ | ---- | ---- | ------------------ |
| ![??]  | -    | -    | <https://boj.kr/-> |

-->

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

## 찾아온 문제들

#### 김동주

| 난이도 | 번호 | 제목 | 링크               |
| ------ | ---- | ---- | ------------------ |
| ![??]  | -    | -    | <https://boj.kr/-> |

#### 정우현

| 난이도 | 번호 | 제목 | 링크               |
| ------ | ---- | ---- | ------------------ |
| ![??]  | -    | -    | <https://boj.kr/-> |

#### 서동혁

| 난이도 | 번호 | 제목 | 링크               |
| ------ | ---- | ---- | ------------------ |
| ![??]  | -    | -    | <https://boj.kr/-> |

#### 손영준

| 난이도 | 번호 | 제목 | 링크               |
| ------ | ---- | ---- | ------------------ |
| ![??]  | -    | -    | <https://boj.kr/-> |

#### 권동균

| 난이도 | 번호 | 제목 | 링크               |
| ------ | ---- | ---- | ------------------ |
| ![??]  | -    | -    | <https://boj.kr/-> |

#### 박준석

| 난이도 | 번호 | 제목 | 링크               |
| ------ | ---- | ---- | ------------------ |
| ![??]  | -    | -    | <https://boj.kr/-> |

#### 양효인

| 난이도 | 번호 | 제목 | 링크               |
| ------ | ---- | ---- | ------------------ |
| ![??]  | -    | -    | <https://boj.kr/-> |

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
