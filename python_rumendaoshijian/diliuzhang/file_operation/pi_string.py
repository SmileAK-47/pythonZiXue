filename = 'G:\\webderiver\\python_rumendaoshijian\\diliuzhang\\file_operation\\pi_digits.txt'

with open(filename) as file_object:
    lins = file_object.readlines()

pi_string = ''
for line in lins:
    pi_string += line.strip()

birthday = input("Enter your birthday in the form mmddyy: ")


if birthday in pi_string:
    print("Your birthady appears in the first million digits of pi")

else:
    print("Your birthday does not appera in the first million gigitsios pi")


# print(pi_string)
# print(len(pi_string))
#
# print(pi_string[:50]+'...')