# Sieve of Eratosthenes (에라토스테네스의 체)

## 소스코드 예시

```python
# N 이하의 소수를 찾는다.

is_prime = [True] * (N+1)
is_prime[0] = False
is_prime[1] = False

for x in range(2, int(N**0.5)+1):
    if is_prime[x]:
        # x를 제외한 N 이하의 x의 배수는 모두 소수가 아닌 것으로 표시.
        for j in range(2*x, N+1, x):
            is_prime[x] = False

# N 이하의 수들에 대해 각각 소수인지 (체에서) 살펴본다.
for x in range(N+1):
    if is_prime[x]:
        print(x)
```

## 왜 $\sqrt{N}$개만 검사하는가?

어떤 양의 정수 $x$의 약수 중 임의의 수 $a$에 대해, $a \leq \sqrt{x}$ 임이 보장된다.

소수이려면 약수 중에 $1$과 자기 자신을 제외한 수가 없으면 되므로, 최대 $\sqrt{N}$개만 검사하면 된다.

## 시간 복잡도는?

$O(n \log \log n)$

### 증명

에라토스테네스의 체에서 코드상의 핵심 부분은 아래의 부분이다.

```python
is_prime = [True] * (N+1)
is_prime[0] = False
is_prime[1] = False

for x in range(2, int(N**0.5)+1):
    # (A)
    if is_prime[x]:
        # (B)
        for j in range(2*x, N+1, x):
            # (C)
            is_prime[x] = False
```

(A), (B), (C) 부분을 각각 몇 번씩 접근하는지를 차례대로 세어보면 시간 복잡도의 근삿값을 구할 수 있다.

$$\text{(시간 복잡도)} = O(T(A)+T(B)+T(C))$$

* $T(A)$: $\sqrt{N}$번 접근한다.

* $T(B)$: $\pi(\sqrt{N})$번 접근한다.
    * $\pi(x)$는 소수 계량 함수로, $x$이하의 소수의 개수를 세는 함수이다.

* $T(C)$: $\sqrt{N}$이하의 소수들 $X$에 대해 각각 $O(\frac{N}{x}) (x \in X)$번 접근한다.
    * $O(\frac{N}{x})$은 $N$ 이하인 $x$의 배수의 개수.

이를 정리하여 전반적인 시간복잡도를 구하면 다음과 같다:

$$O(T(A)+T(B)+T(C)) \\ = O(\sqrt{N} + \sum_{x \text{ prime }}^{\sqrt{N}}{1} + \sum_{x \text{ prime }}^{\sqrt{N}}{\frac{N}{x}}) \\ = O(\sqrt{N} + \sum_{x \text{ prime }}^{\sqrt{N}}{\frac{N}{x}}) \\ = O(\sqrt{N} + N \sum_{x \text{ prime }}^{\sqrt{N}}{\frac{1}{x}}) \\ = O(N \sum_{x \text{ prime }}^{\sqrt{N}}{\frac{1}{x}})$$

위 식에서 다음의 부분을 보자.

$$\sum_{x \text{ prime }}^{\sqrt{N}}{\frac{1}{x}}$$


[소수 역수의 합의 발산성](https://ko.wikipedia.org/wiki/소수의_역수의_합의_발산성) 문서를 참고하면 다음의 사실이 알려져있다고 한다.

$$\sum_{p \text{ prime}}^{p \leq n}{\frac {1}{p}}\geq \ln \ln(n+1)-\ln {\frac {\pi ^{2}}{6}}$$

![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Sum_of_reciprocals_of_primes.svg/600px-Sum_of_reciprocals_of_primes.svg.png)

위 그래프를 보면, $n$ 이하의 소수의 역수의 합을 빅-오 표기법으로 $O(\log \log n)$으로 정리 할 수 있다고 볼 수 있을 것 같다.

이 정리를 응용하여 앞서 보았던 부분을 로그 방정식으로 근사해보자.

$$O(N \sum_{x \text{ prime }}^{\sqrt{N}}{\frac{1}{x}}) = O(N \log \log \sqrt{N}) = O(N \log \log N^\frac{1}{2}) \\ = O(N \log \log N)$$

자, 에라토스테네스의 체를 이용한 소수를 찾는 알고리즘의 시간 복잡도를 분석해보았다.
