# if 3

# A, Z: 65, 90
# a, z: 97, 122
# a-A: 32


def hash_code(value: bytes) -> int:
    # Java의 String.hashCode(byte[] value) 와 동일
    h = 0
    for v in value:
        h = 31 * h + (v & 0xff)
    return h


if __name__ == "__main__":
    N = int(input())

    S1 = 'Aa'+'A'*(N-2)
    S2 = 'BB'+'A'*(N-2)

    # assert hash_code(bytes(S1, encoding='utf8')) == hash_code(bytes(S2, encoding='utf8'))

    print(S1)
    print(S2)
