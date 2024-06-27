> [마크다운 사용법 - 참고 링크](https://gist.github.com/ihoneymon/652be052a0727ad59601)

<!-- 문제 템플릿

| 난이도 | 번호 | 제목 | 링크             |
| ------ | ---- | ---- | ---------------- |
| ![??]  | -    | -    | https://boj.kr/- |

-->

## 숙제

| 난이도 | 번호  | 제목          | 링크                 |
| ------ | ----- | ------------- | -------------------- |
| ![G2]  | 11444 | 피보나치 수 6 | https://boj.kr/11444 |

## 스터디 내용

### CCW 복습

> [![ccw](https://github.com/StudyAlgorithmTeam/Season2/assets/19310326/8f10f750-3480-456d-9c0e-83c0fe6eecf3)](https://ohgym.tistory.com/11)
>
> <https://github.com/StudyAlgorithmTeam/Season2/tree/main/14주차%20CCW>

### 나머지 연산의 분배 법칙

> $(a + b) \mod m = ((a \mod m) + (b \mod m)) \mod m$
>
> $(a \times b) \mod m = ((a \mod m) \times (b \mod m)) \mod m$


### 분할 정복을 이용한 거듭제곱 구하기 $\mathcal{O}(\log N)$

> * $b$가 짝수인 경우: $a^b = (a^{b/2})(a^{b/2})$
> * $b$가 홀수인 경우<sub>($b-1$은 짝수이다.)</sub>: $a^b = a^{(b-1)+1} = (a^{(b-1)/2})(a^{(b-1)/2})a$
>
> ```c
> int mul(int a, int b) {
>     return a * b;
> }
>
> int pow(int a, int b) {
>     int n;
>     if (b == 0) return 1;
>     n = pow(a, b/2);
>     n = mul(n, n); // 자기 자신을 곱해 제곱으로 만든다. 이렇게 하면 pow() 재귀 호출은 1회만 해도 된다.
>     if (b % 2 == 1) n = mul(n, a); // b가 홀수인 경우 처리
>     return n;
> }
> ```

### 분할 정복을 이용한 피보나치 수열 $\mathcal{O}(\log N)$

> <https://namu.wiki/w/피보나치%20수열#s-8.1>
>
> 앞서 다룬 분할 정복을 이용한 거듭제곱의 응용편.
> 피보나치 수로 이루어진 2x2 행렬을 이용하면 다음과 같은 식이 성립한다.
>
> ```math
> \begin{pmatrix} 1&1\\1&0 \end{pmatrix} \begin{pmatrix} F_{n+1}&F_n \\ F_n&F_{n-1} \end{pmatrix} = \begin{pmatrix} 1F_{n+1}+1F_n&1F_n+1F_{n-1} \\ 1F_{n+1}+0F_{n}&1F_n+0F_{n-1} \end{pmatrix} = \begin{pmatrix} F_{n+2}&F_{n+1} \\ F_{n+1} &F_{n} \end{pmatrix}
> ```
>
> 위의 식을 일반화 하면 아래와 같다.
>
> ```math
> \begin{pmatrix} 1&1\\1&0 \end{pmatrix}^n = \begin{pmatrix} F_{n+1}&F_n \\ F_n&F_{n-1} \end{pmatrix}
> ```
>
> 이 때, 행렬 $A$와 $B$의 곱은 다음과 같이 구할 수 있다.
>
> ```math
> (AB)_{ij}=\sum_{k} A_{ik}B_{kj}
> ```
>
> 행렬 곱 구현 예시)
> ```c
> void matmul(int A[5][7], int B[7][9], int C[5][9]) {
>     // C = AB 를 수행한다
>     for (int i = 0; i < 5; i++) {
>         for (int j = 0; j < 9; j++) {
>             C[i][j] = 0;
>             for (int k = 0; k < 7; k++) {
>                 C[i][j] += A[i][k] * B[k][j];
>             }
>         }
>     }
>     return;
> }
> ```

## 스터디 진행 중 풀이

| 난이도 | 번호 | 제목 | 링크                |
| ------ | ---- | ---- | ------------------- |
| ![S1]  | 1629 | 곱셈 | https://boj.kr/1629 |

## 찾아온 문제들

#### 김동주

| 난이도 | 번호 | 제목 | 링크             |
| ------ | ---- | ---- | ---------------- |
| ![??]  | -    | -    | https://boj.kr/- |

#### 정우현

| 난이도 | 번호 | 제목 | 링크             |
| ------ | ---- | ---- | ---------------- |
| ![??]  | -    | -    | https://boj.kr/- |

#### 서동혁

| 난이도 | 번호 | 제목 | 링크             |
| ------ | ---- | ---- | ---------------- |
| ![??]  | -    | -    | https://boj.kr/- |

#### 손영준

| 난이도 | 번호 | 제목 | 링크             |
| ------ | ---- | ---- | ---------------- |
| ![??]  | -    | -    | https://boj.kr/- |

#### 권동균

| 난이도 | 번호 | 제목 | 링크             |
| ------ | ---- | ---- | ---------------- |
| ![??]  | -    | -    | https://boj.kr/- |

#### 박준석

| 난이도 | 번호 | 제목 | 링크             |
| ------ | ---- | ---- | ---------------- |
| ![??]  | -    | -    | https://boj.kr/- |

#### 양효인

| 난이도 | 번호 | 제목 | 링크             |
| ------ | ---- | ---- | ---------------- |
| ![??]  | -    | -    | https://boj.kr/- |

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
