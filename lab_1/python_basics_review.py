def read_str(prompt):
    return input(prompt).strip()

def read_int(prompt):
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Please enter a valid integer.")

def read_int_list(prompt):
    s = input(prompt).strip()
    if not s:
        return []
    try:
        return [int(x) for x in s.split()]
    except ValueError:
        print("Invalid numbers; returning empty list.")
        return []

def add(a, b):
    return a + b

def factorial(n):
    # iterative factorial to show loops and arithmetic
    result = 1
    i = 2
    while i <= n:
        result *= i
        i += 1
    return result

def main():
    # basic string and numeric input
    name = read_str("What's your name? ")
    age = read_int("How old are you? ")
    print("Hello,", name)
    print("In 5 years you will be", age + 5)  # arithmetic

    # reading lists from keyboard
    numbers = read_int_list("Enter some integers separated by spaces: ")
    print("Numbers:", numbers)

    # basic list operations
    numbers.append(42)                 # add single item
    numbers.extend([7, 8])             # add multiple items
    if numbers:
        first = numbers.pop(0)         # remove by index and return
        print("Removed first element:", first)
    # safe remove by value
    if 7 in numbers:
        numbers.remove(7)

    # slicing and indexing
    print("First three:", numbers[:3])
    print("Last item:", numbers[-1] if numbers else None)

    # list comprehension (map + filter style)
    squares = [x * x for x in numbers]
    positives = [x for x in numbers if x > 0]
    print("Squares:", squares)
    print("Positive numbers:", positives)

    # built-in aggregates
    if numbers:
        print("Sum:", sum(numbers), "Min:", min(numbers), "Max:", max(numbers))
    else:
        print("No numbers to aggregate.")

    # sorting & reversing (non-destructive and in-place)
    sorted_numbers = sorted(numbers)
    numbers.sort(reverse=True)
    print("Sorted (new):", sorted_numbers)
    print("Sorted (in place, descending):", numbers)

    # map & filter using lambdas
    doubled = list(map(lambda x: x * 2, numbers))
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print("Doubled:", doubled)
    print("Evens:", evens)

    # enumerate and zip
    for i, val in enumerate(numbers):
        print(f"Index {i} -> Value {val}")
    letters = list("abcde")
    print("Zip example:", list(zip(letters, numbers)))

    # dictionaries
    person = {"name": name, "age": age}
    person["country"] = read_str("Where are you from? ")
    print("Person keys:", list(person.keys()))
    print("Person items:", list(person.items()))

    # function usage
    print("3 + 4 =", add(3, 4))
    n = read_int("Compute factorial of which non-negative integer? ")
    if n >= 0:
        print(f"{n}! =", factorial(n))
    else:
        print("Factorial not defined for negative numbers.")

    # boolean expressions and comparisons
    print("Age >= 18?", age >= 18)
    print("Name starts with A?", name.startswith("A"))

    # while loop example: simple countdown
    count = 5
    print("Countdown:")
    while count > 0:
        print(count)
        count -= 1
    print("Liftoff!")

if __name__ == "__main__":
    main()