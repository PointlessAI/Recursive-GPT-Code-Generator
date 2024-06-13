def solve_fizzbuzz(start, end, fizz_num=3, buzz_num=5):
    for i in range(start, end+1):
        if i % fizz_num == 0 and i % buzz_num == 0:
            print("FizzBuzz")
        elif i % fizz_num == 0:
            print("Fizz")
        elif i % buzz_num == 0:
            print("Buzz")
        else:
            print(i)

start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
fizz_num = int(input("Enter the Fizz number: "))
buzz_num = int(input("Enter the Buzz number: "))
solve_fizzbuzz(start, end, fizz_num, buzz_num)
