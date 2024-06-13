try:
    upper_bound = int(input("Enter the upper bound of the sequence: "))
    if upper_bound <= 0:
        raise ValueError("Upper bound must be a positive integer.")
    if upper_bound > 1000:
        raise ValueError("Upper bound is too large. Please enter a value below 1000.")
except ValueError as e:
    print(f"Error: {e}")
else:
    def fizzbuzz(num):
        if num % 3 == 0 and num % 5 == 0:
            return "fizzbuzz"
        elif num % 3 == 0:
            return "fizz"
        elif num % 5 == 0:
            return "buzz"
        else:
            return num

    output = [fizzbuzz(i) for i in range(1, upper_bound)]

    for item in output:
        print(item)
