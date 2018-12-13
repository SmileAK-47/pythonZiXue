print("Give to me numbers , and I'll divide them.")
print("Enter 'q ' to quit ")

while True:
    first_number = input("\nFirst nmuber:")
    if first_number == 'q':
        break
    second_number = input("Second nmuber:")
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("you cant divide by 0!")
    else:
        print(answer)

