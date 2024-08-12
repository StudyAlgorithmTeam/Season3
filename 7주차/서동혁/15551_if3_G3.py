N = int(input())

temp1 = ">>"
temp2 = "=]"
# 끝에 두 문자열은 31과 1이 곱해짐
# S * 31 + S = 32S
# S-1 * 31 + (S+31) = 32S

if N == 2:
    s1 = temp1
    s2 = temp2
else:
    s1 = "A"*(N-2) + temp1
    s2 = "A"*(N-2) + temp2

print(s1)
print(s2)

def hash(string):
    length = len(string)
    result = 0

    for i in range(length):
        result = result + ord(string[i]) * 31**(length-1-i)
    
    return result

# s1_hash = hash(s1)
# s2_hash = hash(s2)

# if s1 != s2 and s1_hash == s2_hash:
#     print("true")
# else:
#     print("false")

# print(ord(">"))
# print(ord("="))
# print(ord("]"))