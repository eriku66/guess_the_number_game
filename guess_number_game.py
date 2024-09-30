import sys, random

def castToIntWithCheck(value: str) -> int:
    if not str.isdigit(value):
        sys.stderr.write("Invalid input: Input must be an integer.")
        sys.exit(1)

    return int(value)

min_number_input = input("Min number: ")
min_number = castToIntWithCheck(min_number_input)

max_number_input = input("Max number: ")
max_number = castToIntWithCheck(max_number_input)

number_of_attempts_input = input("Number of attempts (default is range): ")

if min_number > max_number:
    sys.stderr.write("Invalid input: Min number must be less than or equal to the max number")
    sys.exit(1)

answer = random.randint(min_number, max_number)

attempts_count = 0

number_of_attempts = max_number - min_number + 1

if str.isdigit(number_of_attempts_input):
     number_of_attempts = castToIntWithCheck(number_of_attempts_input)

while True:
    input_number = castToIntWithCheck(input("Enter your answer: "))

    if input_number == answer:
        print("Correct answer!")
        sys.exit(0)

    attempts_count += 1

    if attempts_count == number_of_attempts:
        print("Reach limit!")
        sys.exit(0)

    print("Wrong answer, please type again.")
