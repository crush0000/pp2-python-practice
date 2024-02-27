import re

text=input()

def test(text):
    pat = "ab{2,3}"
    m = re.findall(pat, text)
    return m
m=test(text)
print(m)
