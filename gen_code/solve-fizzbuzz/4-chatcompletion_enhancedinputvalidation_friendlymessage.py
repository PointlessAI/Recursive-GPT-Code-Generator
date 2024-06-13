def solve_fizzbuzz(start, end, fizz_num=3, buzz_num=5):
    if not all(isinstance(i, int) and i >= 0 for i in [start, end, fizz_num, buzz_num]):
        print("Please enter non-negative integers as start and end numbers, and positive integers for Fizz and Buzz numbers.")
        return
    
    if start > end:
        print("Start number cannot be greater than the end number.")
        return
    
    result = []
    for i in range(start, end+1):
        if i % fizz_num == 0 and i % buzz_num == 0:
            result.append("FizzBuzz")
        elif i % fizz_num == 0:
            result.append("Fizz")
        elif i % buzz_num == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result

try:
    start_input = input("Enter the start number: ")
    end_input = input("Enter the end number: ")
    fizz_input = input("Enter the Fizz number (or press Enter for default 3): ")
    buzz_input = input("Enter the Buzz number (or press Enter for default 5): ")

    start = int(start_input) if start_input else 0
    end = int(end_input) if end_input else 0
    fizz_num = int(fizz_input) if fizz_input else 3
    buzz_num = int(buzz_input) if buzz_input else 5
except ValueError:
    print("Please enter valid integers.")
else:
    fizz_buzz_results = solve_fizzbuzz(start, end, fizz_num, buzz_num)
    if fizz_buzz_results:
        for result in fizz_buzz_results:
            print(result)
