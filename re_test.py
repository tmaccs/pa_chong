import re
pattern = re.compile(r'[\s\d\\\;]')

m = pattern.split(r'aa bb\ds;ya5ng')
print(m)

pattern1 = re.compile(r'(\w+) (\w+)')
str = 'hello 123, hello 456'
m1 = pattern1.sub('hello world',str)
print(m1)