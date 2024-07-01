MOD = int(1e9 + 7)


class Matrix:
    @classmethod
    def zeroes(cls, rows: int, cols: int) -> 'Matrix':
        return cls([[0] * cols for _ in range(rows)])

    @classmethod
    def copy(cls, other: 'Matrix') -> 'Matrix':
        return cls([[x for x in row] for row in other.data])

    def __init__(self, data):
        self.rows = len(data)
        self.cols = len(data[0])
        self.data = data

    def __matmul__(self, other) -> 'Matrix':
        """Python 3.5에 추가된 행렬 곱셈 연산자(@) 오버로딩"""
        if len(self.data[0]) != len(other.data):
            raise ValueError("Matrix inner dimensions must agree")
        result = Matrix.zeroes(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                for k in range(self.rows):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
                    result.data[i][j] %= MOD # MOD로 나눈 나머지를 취함
        return result

    def __getitem__(self, key):
        """행렬 인덱싱 연산자([]) 오버로딩"""
        return self.data[key]

    def __pow__(self, n: int) -> 'Matrix':
        """행렬 거듭제곱 연산자(**) 오버로딩

        분할 정복을 이용한 행렬 거듭제곱 알고리즘으로 구현됨."""
        if n <= 0:
            raise ValueError("Matrix power must be a positive integer")
        if n == 1:
            return Matrix.copy(self)
        result = self ** (n // 2)
        result = result @ result
        if n % 2 == 1:
            result = result @ self
        return result

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return '\n'.join(' '.join(map(str, row)) for row in self.data)


if __name__ == '__main__':
    N = int(input())
    F_n = Matrix([[1, 1], [1, 0]]) ** N
    print(F_n[0][1])
