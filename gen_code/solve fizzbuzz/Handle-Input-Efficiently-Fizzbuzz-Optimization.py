def get_upper_bound():
    while True:
        user_input = input("Enter the upper bound of the sequence (an integer less than 1000): ")
    
        if user_input.isdigit():
            value = int(user_input)
            if 0 < value < 1000:
                return value
            else:
                print("Invalid input: Input must be an integer less than 1000.")
        else:
            print("Invalid input: Input must be a positive integer.")

def fizzbuzz(num):
    value = ''
    if num % 3 == 0:
        value += 'fizz'
    if num % 5 == 0:
        value += 'buzz'
    return value if value else num

if __name__ == '__main__':
    upper_bound = get_upper_bound()
    results = [fizzbuzz(i) for i in range(1, upper_bound + 1)]
    
    for item in results:
        print(item)
