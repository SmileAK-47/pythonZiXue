'''
def greet_user():
    print("hello")
greet_user()

def greet_user(username):
    print("hello "+ username.title() + "!")

greet_user('ganggang')
'''
def get_formatted_name(first_naem,last_naem):
    full_name = first_naem + ' ' + last_naem
    return full_name.title()

while True:
    print("\n palce neter your name:")
    # print("(enter 'q' at time to quiet)")

    f_name = input("first_naem:")
    if f_name == 'q':
        break
    l_name = input("lasst_name:")
    if l_name =='q':
        break
    formatted_name = get_formatted_name(f_name,l_name)
    print("\nHello" + formatted_name + "!")