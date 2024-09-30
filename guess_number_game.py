import random
import sys


def get_valid_input(prompt: str, allow_blank: bool = False) -> int | None:
    input_value = input(prompt)

    if allow_blank and input_value == "":
        return None

    try:
        return int(input_value)
    except ValueError:
        sys.stderr.write("Invalid input: Input must be an integer.")
        raise ValueError


def get_range() -> tuple:
    min_number = get_valid_input("Min number: ")
    max_number = get_valid_input("Max number: ")

    if min_number > max_number:
        sys.stderr.write(
            "Invalid input: Min number must be less than or equal to the max number."
        )

        raise ValueError

    return min_number, max_number


def get_number_of_attempts(min_number: int, max_number: int) -> int:
    number_of_attempts = max_number - min_number + 1

    number_of_attempts_input = get_valid_input(
        f"Number of attempts (default is {number_of_attempts}): ", allow_blank=True
    )

    if number_of_attempts_input is None:
        return number_of_attempts

    if number_of_attempts_input < 1:
        sys.stderr.write(
            "Invalid input: Number of attempts must be a positive integer."
        )

    return number_of_attempts_input


def play_game(min_number: int, max_number: int, number_of_attempts: int):
    answer = random.randint(min_number, max_number)

    for _ in range(0, number_of_attempts):
        guess = get_valid_input("Enter your guess: ")

        if guess == answer:
            print("Correct answer!")

            return

        print("Wrong answer. ", end="")

    print(f"You've reached the limit! The correct answer was {answer}")


def main():
    try:
        min_number, max_number = get_range()
        number_of_attempts = get_number_of_attempts(min_number, max_number)
        play_game(min_number, max_number, number_of_attempts)
    except ValueError:
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
