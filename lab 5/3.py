import re

text=input()

def test(text):
    pat= r'[a-z]+(?:_[a-z]+)+'
    m=re.findall(pat,text)
    return m
m=test(text)
print(m)

#ex4
import re

text=input()

def test(text):
    pat=r'[A-Z][a-z]+'
    m=re.findall(pat,text)
    return m
m=test(text)
print(m)

#ex5
import re
txt=input()
def stend(txt):
    pattern=r"a.*b$"
    m=re.findall(pattern,txt)
    print(m)
stend(txt)

#ex6
import re
txt=input()
x=re.sub(" ", ":" , txt)
y=re.sub(" ", ",", txt)
print(x)
print(y)

#ex7
import re
def camel(txt):
    def capitals(match):
        return match.group(1).upper()
    return re.sub(r"_([a-zA-Z])",capitals,txt)
camls=camel(input())
print(camls)

#ex8
import re

def split_at_uppercase(text):
    words = re.findall('[A-Z][^A-Z]*', text)
    return words


text = input()
result = split_at_uppercase(text)
print(result)

#ex9
import re

def insert_spaces(text):
    pattern = r'(?<!^)(?=[A-Z])'
    result = re.sub(pattern, ' ', text)
    return result

text = input()
result = insert_spaces(text)
print(result)

#ex10
import re

def camel_to_snake_case(camel_case_string):
    snake_case_string = re.sub(r'(?<!^)(?=[A-Z])', '*', camel_case_string).lower()
    return snake_case_string


camel_case_string =  input()
snake_case_string = camel_to_snake_case(camel_case_string)
print(snake_case_string)

