upper_bound = int(input("Enter the upper bound of the sequence: "))

def is_divisible_by_3(num):
    return num % 3 == 0

def is_divisible_by_5(num):
    return num % 5 == 0

def fizzbuzz(num):
    if is_divisible_by_3(num) and is_divisible_by_5(num):
        return "fizzbuzz"
    elif is_divisible_by_3(num):
        return "fizz"
    elif is_divisible_by_5(num):
        return "buzz"
    else:
        return num

output = [fizzbuzz(i) for i in range(1, upper_bound)]

for item in output:
    print(item)
