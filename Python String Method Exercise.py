# write a python function to convert string to url

# str1 = 'Md Rayhan Hossain'
# lowercase = str1.lower()  # convert str1 to lowercase
# url = lowercase.replace(' ', '-')  # replace space to -
# print(url)

def strtourl(string):
    '''
    this fuction convert string to lower
    :param string:
    :return: url
    '''

    strip_string = string.strip()
    lowercase = strip_string.lower()
    url = lowercase.replace(' ', '-')
    return url


print(strtourl('Md Rayhan Hossain '))
