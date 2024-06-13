class InvalidInputError(Exception):
    pass

def solve_fizzbuzz(start, end, fizz_num, buzz_num):
    results = []
    for i in range(start, end + 1):
        result = ""
        if i % fizz_num == 0:
            result += "Fizz"
        if i % buzz_num == 0:
            result += "Buzz"
        if result == "":
            result = i
        results.append(result)
    return results

try:
    while True:
        start_input = input("Enter the start number: ")
        end_input = input("Enter the end number: ")
        fizz_input = input("Enter the Fizz number (Default is 3): ") or "3"
        buzz_input = input("Enter the Buzz number (Default is 5): ") or "5"

        start = int(start_input)
        end = int(end_input)
        fizz_num = int(fizz_input)
        buzz_num = int(buzz_input)
        
        if not all(isinstance(i, int) and i >= 0 for i in [start, end, fizz_num, buzz_num]):
            raise InvalidInputError("Please enter non-negative integers as start and end numbers, and positive integers for Fizz and Buzz numbers.")
        
        if start >= end:
            raise InvalidInputError("Start number must be less than the end number.")
        
        fizz_buzz_results = solve_fizzbuzz(start, end, fizz_num, buzz_num)
        
        if fizz_buzz_results:
            for result in fizz_buzz_results:
                print(result)

except KeyboardInterrupt:
    print("Program terminated. Goodbye!")

except ValueError:
    raise InvalidInputError("Please enter valid integers.")
