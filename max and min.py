numbers = []

while True:
    user_input = input("Enter an integer (or 'done' to finish): ")

    if user_input == 'done':
        break

    try:
        numbers.append(int(user_input))
    except ValueError:
        print('Invalid input. Please enter an integer.')

if numbers:
    print(f"Maximum: {max(numbers)}, Minimum: {min(numbers)}")
else:
    print("No valid integers entered.")