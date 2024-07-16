# 출력 형식이 잘못되었습니다

import sys
import re


TOKENS = re.compile(r'(\(|\)|\{|\}|\[|\]|\,|\;|\:|\.)')
WHITESPACES = re.compile(r'\s+')
PARENTHESIS_OPENER = re.compile(r'\(|\{|\[')
PARENTHESIS_CLOSER = re.compile(r'\)|\}|\]')


def compress(s: str) -> str:
    # 대소문자 구분하지 않음
    s = s.lower()
    # 각 토큰의 앞 뒤로 공백을 추가
    s = TOKENS.sub(r' \1 ', s)
    # 중복된 공백을 하나로 통일
    s = WHITESPACES.sub(' ', s)
    # 괄호의 종류를 구분하지 않음 -> 소괄호로 통일
    s = PARENTHESIS_OPENER.sub('(', s)
    s = PARENTHESIS_CLOSER.sub(')', s)
    # 세미콜론과 컴마는 구분하지 않음 -> 컴마로 통일
    s = s.replace(';', ',')
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
