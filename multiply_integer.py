# This program asks the user to enter positive integer
# The program will multiply all the positive numbers up to the integer


def main():
    # this tells the user the answer of
    # all the positive numbers from the integer

    # vars
    answer = 1

    # input
    number_count = input("Please enter a positive integer: ")

    # process & output
    try:
        integer_as_number = int(number_count)

        while integer_as_number > 0:
            answer = answer * integer_as_number
            integer_as_number = integer_as_number - 1

        print("The answer from all the positive numbers is {0}.".format(answer))

    except Exception:
        print("This is not a positive integer!")

    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
