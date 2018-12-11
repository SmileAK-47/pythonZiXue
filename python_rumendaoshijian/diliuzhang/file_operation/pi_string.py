filename = 'G:\\webderiver\\python_rumendaoshijian\\diliuzhang\\file_operation\\pi_digits.txt'

with open(filename) as file_object:
    lins = file_object.readlines()

pi_string = ''
for line in lins:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))

