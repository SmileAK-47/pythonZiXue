'''
def get_formateede_name(first_name,last_name):
    full_naem = first_name + ' '+ last_name
    return  full_naem.title()
musician = get_formateede_name('jimi','hendrix')
print(musician)


def get_formateede_name(first_name,middle_name,last_name):
    full_name = first_name +' '+middle_name + ' '+ last_name
    return full_name.title()
musician = get_formateede_name('john','lee','hooker')
print(musician)

'''
def get_formateede_name(first_name,last_name,middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' '+ last_name
    return  full_name.title()
musician = get_formateede_name('john','hookerd')
print(musician)

musician = get_formateede_name('john','hooker','lee')
print(musician)