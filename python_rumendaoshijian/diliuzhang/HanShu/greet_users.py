def greet_users(names):
    for name in names :
        msg = "hello "+ name.title() + '!'
        print(msg)
usernames = ['hh','ll','dd']
greet_users(usernames)