def solve_fizzbuzz(start, end, fizz_num=3, buzz_num=5):
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
    start = int(input("Enter the start number: "))
    end = int(input("Enter the end number: "))
    fizz_num = int(input("Enter the Fizz number: "))
    buzz_num = int(input("Enter the Buzz number: "))
except ValueError:
    print("Please enter valid integers.")
else:
    fizz_buzz_results = solve_fizzbuzz(start, end, fizz_num, buzz_num)
    for result in fizz_buzz_results:
        print(result)
