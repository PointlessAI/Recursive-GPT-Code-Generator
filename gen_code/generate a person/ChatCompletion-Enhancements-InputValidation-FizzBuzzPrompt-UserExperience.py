def validate_input(user_input):
    try:
        user_input_int = int(user_input)
        if user_input_int <= 0:
            return "Invalid input: Input must be a positive integer."
        if user_input_int >= 1000:
            return "Invalid input: Input must be less than 1000."
        return None
    except ValueError:
        return "Invalid input: Input must be an integer."

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "fizzbuzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    else:
        return num

user_input = input("Enter the upper bound of the sequence (an integer less than 1000): ")

validation_result = validate_input(user_input)

if validation_result:
    print(validation_result)
else:
    upper_bound = int(user_input)
    result = [fizzbuzz(i) for i in range(1, upper_bound + 1)]
    
    for item in result:
        print(item)
