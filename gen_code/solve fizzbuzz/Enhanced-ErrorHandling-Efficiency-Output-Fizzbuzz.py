def get_upper_bound():
    while True:
        try:
            user_input = int(input("Enter the upper bound of the sequence (an integer less than 1000): "))
        
            if 0 < user_input < 1000:
                return user_input
            else:
                print("Invalid input: Input must be an integer less than 1000.")
        except ValueError:
            print("Invalid input: Input must be a positive integer.")

def fizzbuzz(num):
    if num % 15 == 0:
        return 'fizzbuzz'
    elif num % 3 == 0:
        return 'fizz'
    elif num % 5 == 0:
        return 'buzz'
    else:
        return num

if __name__ == '__main__':
    upper_bound = get_upper_bound()
    results = [fizzbuzz(i) for i in range(1, upper_bound + 1)]
    
    print(*results, sep=', ')
