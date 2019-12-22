from pathlib import Path

standard_file_path = "calculations.txt"


def main():
    file = get_standard_logging_file()
    while True:
        question = "What would you like to do?\n" \
                   "[0] Add two numbers\n" \
                   "[1] Subtract two numbers\n" \
                   "[2] Multiply two numbers\n" \
                   "[3] Divide one number by another number\n" \
                   "[4] Print history\n" \
                   "[5] Delete history\n" \
                   "[6] Quit"
        choice = get_number_user_input(question, 0, 6)

        result_string = None

        if choice <= 3:
            first_number = get_number_user_input("First number:", None, None)
            second_number = get_number_user_input("Second number:", None, None)

            if choice == 0:  # Adding
                result_string = str(first_number) + " + " + str(second_number) + " = " + \
                                str(add(first_number, second_number))
            if choice == 1:  # Subtracting
                result_string = str(first_number) + " - " + str(second_number) + " = " + \
                                str(subtract(first_number, second_number))
            if choice == 2:  # Multiplying
                result_string = str(first_number) + " * " + str(second_number) + " = " + \
                                str(multiply(first_number, second_number))
            if choice == 3:  # Dividing
                result_string = str(first_number) + " / " + str(second_number) + " = " + \
                                str(divide(first_number, second_number))
        if choice == 4:  # Printing history
            print_file_content(file)
        if choice == 5:  # Deleting history
            open(standard_file_path, "w").close()  # Overrides everything in the file
        if choice == 6:  # Exiting
            break

        # If we calculated sth we print the result and write that to our file
        if result_string is not None:
            print(result_string)
            write_line_to_file(file, result_string)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


# Checks if a file exists at the given path
def does_file_exist(file_path):
    path = Path(file_path)
    if path.is_file():
        return True
    return False


def get_standard_logging_file():
    if does_file_exist(standard_file_path):
        print("The standard logging file does already exist")
        user_choice = get_yes_no_user_input("Would you like to override the current file?")
        if user_choice:
            open(standard_file_path, "w").close()
    return standard_file_path


def write_line_to_file(file, message):
    file_opened = open(file, "a")
    file_opened.write(message)
    file_opened.write("\n")
    file_opened.close()


def print_file_content(file):
    file_opened = open(file, "r")
    print("Contents of the file:")
    for line in file_opened:
        print(line.replace("\n", ""))  # Removing new line breaks
    file_opened.close()


def get_yes_no_user_input(question):
    while True:
        print(question)
        user_input = input("[y / N]\n").lower()
        if user_input == "y":
            return True
        elif user_input == "n":
            return False


def get_number_user_input(question, lowest_number, highest_number):
    while True:
        print(question)
        user_input = input("Choice:\n")
        if user_input.isnumeric():
            user_number = int(user_input)
            if lowest_number is None and highest_number is None:
                return user_number
            if lowest_number <= user_number <= highest_number:
                return user_number


if __name__ == "__main__":
    main()
