def get_upper_bound():
    print("FizzBuzz is a program that prints numbers from 1 to a specified upper bound. If the number is divisible by 3, it prints 'fizz'. If the number is divisible by 5, it prints 'buzz'. If the number is divisible by both 3 and 5, it prints 'fizzbuzz'.")
    
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
