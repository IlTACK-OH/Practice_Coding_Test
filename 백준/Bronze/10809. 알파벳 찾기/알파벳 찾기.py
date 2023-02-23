# 알파벳의 아스키 코드의 번호(10진수)
alphabet = list(range(97,123))
# input word
in_str = input()
result = []
for i in alphabet:
    result.append(str(in_str.find(chr(i))))

print(' '.join(result))