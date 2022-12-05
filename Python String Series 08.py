# split, rsplit,rsplit,splitlines
str1 = "Hello, I am Rayhan, I love Python"
str2 = "Hello, I am Rayhan,\n I love Python"

print(str1.split())
print(str1.split(','))
print(str1.split(',', maxsplit=1))
print(str2.splitlines())