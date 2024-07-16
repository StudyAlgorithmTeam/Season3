# 정답 비율 계산하기

import dataclasses
import sys
import typing


ADMIN_ID = 'megalusion'


@dataclasses.dataclass
class User:
    id: str
    has_accepted: bool
    tries: int


def solve(N: int, lines: list) -> float:
    """
    >>> solve(1, ['7964219 megalusion 4 4086 920 3 7212'])
    0.0
    >>> solve(1, ['7964219 baekjoon 4 4086 920 3 7212'])
    100.0
    >>> solve(1, ['7964219 baekjoon 6 4086 920 3 7212'])
    0.0
    >>> solve(2, ['7964219 baekjoon 6 4086 920 3 7212', '7964220 baekjoon 4 4086 920 3 7212'])
    50.0
    >>> solve(24, ['7884922 megalusion 4 2180 0 88 1141', '7884988 megalusion 4 9424 124 3 1395', '7885291 junodeveloper 4 2144 0 88 1146', '7885327 doju 4 1312 0 49 756', '7886288 moonrabbit2 4 2372 0 88 1247', '7886486 koosaga 11 0 0 84 1452', '7886490 koosaga 4 2300 0 84 1423', '7886858 yclock 4 2224 0 49 911', '7888812 seok9311 6 1116 0 1 1049', '7888907 seok9311 6 1116 0 1 1050', '7888917 seok9311 7 1116 1000 1 888', '7889119 seok9311 6 1116 508 1 1033', '7889125 seok9311 6 1116 0 1 1052', '7889184 seok9311 4 1120 0 1 2245', '7895033 jinsub8682 4 9576 120 3 1326', '7898896 khj94811 4 1988 0 88 1585', '7901927 rkm0959 4 2424 0 88 2318', '7908183 woong10sae 6 2068 0 88 1454', '7908251 woong10sae 6 2860 4 88 1610', '7908353 woong10sae 4 2044 0 88 829', '7931699 y305205 6 29656 64 28 340', '7931803 y305205 6 29656 68 28 341', '7945503 chogahui05 4 1384 0 0 361848', '7951273 subinium 4 1116 0 49 527'])
    60.0
    >>> solve(45, ['7786805 megalusion 4 39328 424 88 2802', '7787032 megalusion 4 97920 752 88 2955', '7848292 jwvg0425 4 39252 400 88 2802', '7853562 smu201111192 6 67676 48 49 3136', '7853604 smu201111192 6 65860 216 49 3152', '7853625 onjo0127 6 12100 76 49 1867', '7853662 smu201111192 4 65860 464 49 3110', '7853677 onjo0127 4 34144 484 49 1881', '7855282 y2k2 6 2092 8 88 649', '7855328 y2k2 6 2092 8 88 651', '7855589 whoru 6 10332 44 12 883', '7855639 bh_17 7 47240 12000 28 403', '7855640 bh_17 7 240816 12000 73 403', '7855652 headkn 8 262268 276 88 1163', '7855742 headkn 7 160200 2000 88 1156', '7855814 august14 4 85184 68 88 1158', '7855852 khsoo01 4 10776 80 49 802', '7855917 whoru 6 10332 48 12 1380', '7855989 whoru 6 13840 52 12 1430', '7855996 y2k2 6 2092 12 88 661', '7856081 whoru 6 8956 52 12 1458', '7856134 whoru 6 9212 80 12 1509', '7856145 whoru 6 10332 48 12 1505', '7856201 whoru 6 9212 80 12 1603', '7856208 whoru 6 13312 48 12 1599', '7856436 whoru 6 16144 48 12 1710', '7856587 qkqkfo 6 4880 32 88 572', '7856678 qkqkfo 6 4880 36 88 583', '7856725 nevergiveup936 7 430096 7000 3 1190', '7856850 tlwpdus 6 117628 420 49 3197', '7856877 tlwpdus 4 117628 608 49 3238', '7859281 myungwoo 6 85972 80 49 1002', '7859301 myungwoo 4 85972 80 49 1014', '7859440 doju 4 7952 16 49 1243', '7861554 dbflwla 6 11760 72 49 744', '7861696 dbflwla 6 11760 76 49 751', '7865485 jh05013 6 204180 252 32 1181', '7865517 jh05013 4 260576 632 32 1202', '7865536 yclock 6 36464 404 49 1397', '7866132 yclock 4 36464 388 49 1411', '7882931 jwvg0425 4 120988 168 88 2604', '7883041 jwvg0425 6 128796 112 88 2517', '7883053 jwvg0425 6 128796 160 88 2526', '7883055 jwvg0425 6 128800 120 88 2578', '7883128 jwvg0425 4 128796 148 88 2619'])
    58.82352941176470588235
    >>> solve(4, ['7960654 megalusion 4 90100 868 88 1674', '7960868 dogeon01 11 0 0 88 124', '7963152 appa 4 55928 284 49 2070', '7964434 koosaga 4 31924 124 84 3403'])
    100.0
    >>> solve(23, ['7736757 megalusion 4 5792 4 88 1673', '7737007 junodeveloper 4 5984 4 88 544', '7738353 jh05013 4 64744 1076 28 306', '7740562 kks227 4 5032 16 84 550', '7740651 portableangel 4 5064 24 49 618', '7746734 zych1751 7 5916 2000 49 554', '7746737 zych1751 4 5916 16 49 588', '7793275 kesakiyo 4 5136 28 49 827', '7825114 jason9319 4 5972 16 49 606', '7854814 worn1215 6 10372 132 3 804', '7854828 worn1215 9 46144 1808 3 934', '7854829 worn1215 6 8716 128 3 796', '7854840 worn1215 4 13552 148 3 802', '7859465 ljg9574 4 9544 120 3 1049', '7871836 jjim9417 11 0 0 1 826', '7871840 jjim9417 6 2968 4 1 847', '7871902 jjim9417 4 5904 4 1 846', '7889581 ntopia 4 5900 4 84 703', '7896433 iljimae 7 10108 2000 88 877', '7896434 iljimae 4 9704 4 88 2044', '7902462 cheetose 4 5900 16 49 2095', '7909935 cpp05013 4 5932 4 88 747', '7936103 dotorya 4 6296 4 88 1630'])
    68.18181818181818181818181818181818
    """
    user_repository: typing.Dict[str, User] = {}
    # 유저 데이터베이스 초기화
    for user_id, is_correct in map(extract_id_correctness, lines):
        if user_id == ADMIN_ID:
            continue
        if user_id not in user_repository:
            user_repository[user_id] = User(user_id, False, 0)
        user = user_repository[user_id]
        if is_correct:
            user.has_accepted = True
        if not user.has_accepted:
            user.tries += 1
    # 데이터베이스 내용을 바탕으로 정답 비율을 계산
    ac_users = 0
    ac_user_tries = 0
    for user in user_repository.values():
        if user.has_accepted:
            ac_users += 1
            ac_user_tries += user.tries
    try:
        return 100 * ac_users / (ac_users + ac_user_tries)
    except ZeroDivisionError:
        return 0.0


def extract_id_correctness(line: str):
    tokens = line.split()
    return tokens[1], (tokens[2] == '4')


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    lines = sys.stdin.readlines()
    print(solve(N, lines))
