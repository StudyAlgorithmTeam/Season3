import sys


HASH_TO_NUM = {
    0b111111000111111: 0,
    0b000000000011111: 1,
    0b101111010111101: 2,
    0b101011010111111: 3,
    0b111000010011111: 4,
    0b111011010110111: 5,
    0b111111010110111: 6,
    0b100001000011111: 7,
    0b111111010111111: 8,
    0b111011010111111: 9,
}


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    W = N // 5

    signal = sys.stdin.readline()
    signal_2d = [signal[offset:offset+W]+'.' for offset in range(0, N, W)]

    h = 0
    for x in range(W+1):
        for y in range(5):
            h = h << 1 | (1 if signal_2d[y][x] == '#' else 0)
        if h & 0b11111 == 0 and h:
            # end of digit
            h >>= 5
            sys.stdout.write(str(HASH_TO_NUM[h]))
            h = 0
