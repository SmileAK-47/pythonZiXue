prompt = "\nTell me something ,and Iwill repeat it back to you:"
prompt += "\nEntter 'quit to end the program:"
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)


# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active =False
#     else:
#         print(message)
#

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("i'd love to go to "+ city.title() +"!")