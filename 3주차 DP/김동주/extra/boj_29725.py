total_score = 0

for c in open(0).read():
    score = 0
    match c.lower():
        case 'p':
            score = 1
        case 'n' | 'b':
            score = 3
        case 'r':
            score = 5
        case 'q':
            score = 9
    if c.isupper():
        total_score += score
    else:
        total_score -= score

print(total_score)