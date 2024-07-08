# 타일 채우기


STATE_MACHINE = {
    0b000: [0b111],
    0b001: [0b110],
    0b010: [0b101],
    0b011: [0b100, 0b111],
    0b100: [0b011],
    0b101: [0b010],
    0b110: [0b001, 0b111],
    0b111: [0b110, 0b011, 0b000],
}


if __name__ == "__main__":
    N = int(input())
    dp_curr = [0] * 8
    dp_prev = [0] * 8
    dp_curr[0b111] = 1

    for i in range(N):
        dp_prev, dp_curr = dp_curr, dp_prev
        for curr_state in range(8):
            dp_curr[curr_state] = sum(dp_prev[prev_state] for prev_state in STATE_MACHINE[curr_state])

    print(dp_curr[0b111])
