str1 = "Python is awesome, isn't it?"
# check total len of the string
print('The len of string is: ', len(str1))

# check specifics word in string is how many times
substring = 'awesome'
print("The substring ", substring, " present in", str1.count(substring), 'times')
substring2 = 'i'
print(str1.count(substring2, 8))  # count 'i' after first 8 characters
print(str1.count(substring2, 8, 20))  # count 'i' in 8 to 20 characters