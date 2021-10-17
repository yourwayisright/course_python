user_answer = 'no'
counter = 0


for i in range (1, 101):
    counter += 1
    if user_answer == 'no':
        print(f'Is {i} guessed number? yes/no')
        received_answer = input()
        user_answer = received_answer
    else:
        print(f"The number was guessed with {counter-1} attempts!")
        break
