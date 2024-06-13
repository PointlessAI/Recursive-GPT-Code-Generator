def validate_input(user_input):
    if not user_input.isdigit():
        return "Invalid input: Input must be an integer."
    if int(user_input) <= 0:
        return "Invalid input: Input must be a positive integer."
    if int(user_input) >= 1000:
        return "Invalid input: Input must be less than 1000."
    return None

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "fizzbuzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return num

user_input = input("Enter the upper bound of the sequence: ")
validation_result = validate_input(user_input)

if validation_result:
    print(validation_result)
else:
    upper_bound = int(user_input)
    result = [fizzbuzz(i) for i in range(1, upper_bound)]
    
    for item in result:
        print(item)
