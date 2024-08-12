# 두라무리 휴지


from collections import Counter


def is_aeiou(c: str):
    return c in 'aeiou'


def is_duramuri(w1: str, w2: str) -> bool:
    """
    >>> is_duramuri('durumari', 'duramuri')
    True
    >>> is_duramuri('durumari', 'darmurui')
    True
    >>> is_duramuri('durumari', 'dumurari')
    False
    >>> is_duramuri('durumari', 'darumari')
    False
    >>> is_duramuri('durumari', 'abcdefgh')
    False
    """
    # 1. 한 단어를 재배열해 다른 단어를 만들 수 있어야 한다.
    # O(N)
    if Counter(w1) != Counter(w2):
        return False
    # 2. 두 단어의 첫 글자와 마지막 글자는 서로 동일해야 한다.
    # O(1)
    if w1[0] != w2[0] or w1[-1] != w2[-1]:
        return False
    # 3. 각 단어에서 모음(a, e, i, o, u)을 제거한 문자열은 동일해야 한다.
    # O(N)
    i1 = 0
    i2 = 0
    while i1 < len(w1) and i2 < len(w2):
        while i1 < len(w1) and is_aeiou(w1[i1]):
            i1 += 1
        while i2 < len(w2) and is_aeiou(w2[i2]):
            i2 += 1
        if i1 < len(w1) and i2 < len(w2) and w1[i1] != w2[i2]:
            return False
        i1 += 1
        i2 += 1
    return True


if __name__ == "__main__":
    input() # 필요 없다.
    w1 = input().strip()
    w2 = input().strip()
    if is_duramuri(w1, w2):
        print('YES')
    else:
        print('NO')
