total = 0
count = 0

while True:
    user_input = input("Enter an integer (or 'done' to finish): ")
    if user_input == 'done':
        break
    try:
        total += int(user_input)
        count += 1
    except ValueError:
        print('Invalid input. Please enter an integer.')
if count > 0:
    print(f'Total: {total}, Count: {count}, Average: {total / count}')
else:
    print("No valid integers entered.")
