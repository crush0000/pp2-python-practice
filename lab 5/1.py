# import re
# txt = input() 
# def test1(txt):
#     pat=r'ab*'
#     m = re.findall(pat,txt)
#     print(m)

# test1(txt)



import re
txt = input()
def test(txt):
    pat='[A-Z]+[a-z]*[0-9]+'
    m=re.findall(pat,txt)
    # return m
    print(m)
test(txt)