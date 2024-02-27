import re
txt = input() 
def test1(txt):
    m = re.findall("ab*",txt)
    print(m)

test1(txt)