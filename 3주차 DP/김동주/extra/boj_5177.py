# 출력 형식이 잘못되었습니다

import sys
import re


WHITESPACES = re.compile(r'\s+')

PARENTHESIS_OPENER = re.compile(r'\(|\{|\[')
PARENTHESIS_CLOSER = re.compile(r'\)|\}|\]')


def compress(s: str) -> str:
    # 대소문자 구분하지 않음 -> 소문자로 통일
    s = s.lower()
    # 괄호끼리는 종류를 구분하지 않음 -> 소괄호로 통일
    s = PARENTHESIS_OPENER.sub(' ( ', s)
    s = PARENTHESIS_CLOSER.sub(' ) ', s)
    # 세미콜론과 컴마는 구분하지 않음 -> 컴마로 통일
    s = s.replace(',', ' , ')
    s = s.replace(';', ' , ')
    # 특수 문자의 바로 앞이나 바로 뒤에 나오는 공백도 있으나 없어도 된다 -> 있는 것으로 통일
    s = s.replace('.', ' . ')
    s = s.replace(':', ' : ')
    # 공백이 하나 이상이라면 공백의 크기는 관계 없다. -> 하나의 공백만 남기고 제거
    s = WHITESPACES.sub(' ', s)
    return s


def solve(s1: str, s2: str) -> bool:
    """
    >>> solve("( 1, 4 ) (2,3) (2,4)", "{ 1; 4 )   {2;3)  {2;4)")
    True
    >>> solve("Data Set 1: equal", "data   set 1 :  EQUAL")
    True
    >>> solve("Data Set 1: equal", "DataSet 1: equal")
    False
    """
    s1 = compress(s1)
    s2 = compress(s2)
    return s1 == s2


if __name__ == "__main__":
    K = int(sys.stdin.readline())
    for i in range(1, K+1):
        s1 = sys.stdin.readline().strip()
        s2 = sys.stdin.readline().strip()
        if solve(s1, s2):
            sys.stdout.write(f"Data Set {i}: equal\n\n")
        else:
            sys.stdout.write(f"Data Set {i}: not equal\n\n")
